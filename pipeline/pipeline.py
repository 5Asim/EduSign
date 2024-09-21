# from text_to_pose_scrapper import text_to_pose_scrapper
from image_generation import process_folder
from pose_to_animated_video import merge_pose_videos, extract_images_from_pose_video, cropImage, create_video


# Define your folder paths
input_folder_path = './frames/test_A'   # Pose images folder
# Output folder for generated human images
output_folder_path = './frames/final'

# Start processing


# First the text transcripts are sent to the server and saved in the text file.

def pipeline():
    # Convert the transcript file into pose video
    # text_to_pose_scrapper()
    # merge_pose_videos('./')
    # extract_images_from_pose_video('hello.mp4')
    # cropImage()
    process_folder(input_folder_path, output_folder_path)
    # create_video()


if __name__ == '__main__':
    pipeline()
