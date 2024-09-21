from image_generation import process_folder
# Define your folder paths
input_folder_path = './frames/initial'   # Pose images folder
# Output folder for generated human images
output_folder_path = './frames/final'

# Start processing


# First the text transcripts are sent to the server and saved in the text file.

def pipelin():

    process_folder(input_folder_path, output_folder_path)
