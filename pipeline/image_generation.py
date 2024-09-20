import time
import base64
import requests
import os

STABLE_DIFFUSION_API_URL = "https://api.stability.ai/v2beta/stable-image/control/structure"

# API key if needed
API_KEY = ''  # Optional, depending on the API you're using

def call_stable_diffusion_api(image_path):
    """
    Call the Stable Diffusion API with the pose image.
    """
    response = requests.post(
        f"https://api.stability.ai/v2beta/stable-image/control/structure",
        headers={
            "authorization": f"Bearer {API_KEY}",
            "accept": "image/*"
        },
        files={
            "image": open("./frames/initial/image1.png", "rb")
        },
        data={
            "prompt": "Human face of Brad Pitt in the sign language pose given by the image",
            "output_format": "png"
        },
    )

    if response.status_code == 200:
        with open("./frames/final/image1.png", 'wb') as file:
            file.write(response.content)
    else:
        raise Exception(str(response.json()))    


def process_folder(input_folder, output_folder):
    """
    Process all pose images in the input folder by sending them to the Stable Diffusion API
    and saving the generated human images to the output folder.
    """
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all pose images in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('png', 'jpg', 'jpeg')):  # You can add more file types if needed
            image_path = os.path.join(input_folder, filename)
            print(f"Processing: {filename}")

            # Call the Stable Diffusion API
            generated_image = call_stable_diffusion_api(image_path)

            if generated_image:
                # Save the generated image
                output_path = os.path.join(output_folder, f"generated_{filename}")
                with open(output_path, 'wb') as output_file:
                    output_file.write(generated_image)
                print(f"Image saved to {output_path}")
            else:
                print(f"Failed to process {filename}")

# Define your folder paths
input_folder_path = './frames/initial'   # Pose images folder
output_folder_path = './frames/final' # Output folder for generated human images

# Start processing
process_folder(input_folder_path, output_folder_path)

# if __name__ == '__main__':
#     call_stable_diffusion_api("image1.png")