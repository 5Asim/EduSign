import cv2
import os
import shutil
import re
from os.path import isfile, join
import fnmatch

def extract_images_from_pose_video(video_filepath):
    # Open the video file
    merged_output = video_filepath
    # Open the video file
    video = cv2.VideoCapture(merged_output)
    path = "./frames/initial"

    # Delete any previous frames in the folder
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    # Check if the video file was opened successfully
    if not video.isOpened():
        print("Error opening video file")
        exit()

    # Set the frame number to start with
    frame_num = 0

    # Loop through the video frames
    while True:
        # Read the next frame from the video
        ret, frame = video.read()

        # Check if the frame was read successfully
        if not ret:
            break

        # Save the frame as an image file
        # cv2.imwrite(f"frame{frame_num}.png", frame)
        cv2.imwrite(os.path.join(path, f"frame{frame_num}.png"), frame)

        # Increment the frame number
        frame_num += 1

    # Release the video object
    video.release()

def merge_pose_videos(video_files, output_path="final_video.mp4"):
    # List to hold all the frames from the videos
    all_frames = []

    # Loop through each video file
    for video_file in video_files:
        # Open the video file
        video = cv2.VideoCapture(video_file)

        # Check if the video file was opened successfully
        if not video.isOpened():
            print(f"Error opening video file: {video_file}")
            continue

        # Read frames from the video and append them to the frame list
        while True:
            ret, frame = video.read()
            if not ret:
                break
            all_frames.append(frame)

        # Release the video object after reading all frames
        video.release()

    # Check if we have frames to write to the output
    if len(all_frames) == 0:
        print("No frames were found to write to the output video.")
        return

    # Get the size of the first frame (assuming all frames are the same size)
    height, width, layers = all_frames[0].shape
    size = (width, height)

    # Initialize the video writer object
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'MP4V'), 10, size)

    # Write all frames to the output video
    for frame in all_frames:
        out.write(frame)

    # Release the video writer object
    out.release()

    print(f"Merged video saved as {output_path}")

def cropImage():
    # Set the paths for the input folder containing images and the output folder
    input_folder = './frames/initial'
    output_folder = './frames/test_A'

    # Delete any previous frames in the folder
    for filename in os.listdir(output_folder):
        file_path = os.path.join(output_folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    # Desired crop dimensions and offset
    crop_width = 400
    crop_height = 336
    offset = 40

    # Loop over the images in the input folder
    for filename in os.listdir(input_folder):
        # Read the image
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)
        # Calculate the crop coordinates
        image_height, image_width = img.shape[:2]
        start_x = max(0, int((image_width - crop_width) / 2))
        start_y = max(0, int((image_height - crop_height) / 2)) - offset

        # Perform the crop
        cropped_image = img[start_y:start_y +
                            crop_height, start_x:start_x + crop_width]

        # Create the output path for the cropped image
        output_path = os.path.join(output_folder, filename)

        # Save the cropped image
        cv2.imwrite(output_path, cropped_image)


def convert(text): return int(text) if text.isdigit() else text.lower()


def alphanum_key(key):
    return [convert(c) for c in re.split('([0-9]+)', key)]


def sorted_alphanumeric(data):
    return sorted(data, key=alphanum_key)


def create_video():
    pathIn = './frames/final'
    pathOut = 'GAN_generated_new.mp4'
    fps = 10
    frame_array = []
    files = []

    for filename in os.listdir(pathIn):
        # Check if the filename starts with 'generated_'
        if filename.startswith('generated_'):
            # Append the file path to the list of generated files
            files.append(os.path.join(pathIn, filename))
    # for sorting the file names properly
    files.sort(key=lambda x: int(re.search(r'generated_frame(\d+)', x).group(1)))            

    for file in files:
        if fnmatch.fnmatch(file, '*_synthesized_image.jpg'):
            filename = pathIn + '/' + file
            # reading each files
            img = cv2.imread(filename)
            height, width, layers = img.shape
            size = (width, height)

        # inserting the frames into an image array
        frame_array.append(img)
        out = cv2.VideoWriter(
            pathOut, cv2.VideoWriter_fourcc(*'MP4V'), fps, size)
        for i in range(len(frame_array)):
            # writing to a image array
            out.write(frame_array[i])
        out.release()