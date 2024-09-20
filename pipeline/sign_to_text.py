# # Setup WebDriver (Assuming you're using Chrome)
# browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# browser.get('https://huggingface.co/spaces/hysts/ControlNet-v1-1')


# def upload_and_generate(image_path):
#     # Find the input element for the image upload
#     upload_element = browser.find_element(By.XPATH, '//*[@id="component-8"]/div[3]/button/input')
#     upload_element.send_keys(image_path)  # Upload the image file
    
#     input_field = browser.find_element(By.XPATH, '//*[@id="component-9"]/label/textarea')
#     text = "real human person speaking in sign language with real face"
#     input_field.send_keys(text)
    
#     # Click the 'Run' button to generate the output
#     run_button = browser.find_element(By.XPATH, '//*[@id="component-10"]')
#     run_button.click()
    
#     # Wait for the result to generate (adjust the time depending on processing speed)
#     time.sleep(10)  # Adjust this delay based on average processing time
    
#     # Download the generated image
    
    
#      # Locate the generated image element (make sure to inspect the image element on the site to get its exact XPath or CSS)
#     generated_image = browser.find_element(By.XPATH, 'xpath_to_generated_image')

#     # Get the 'src' attribute of the image (URL or data URI)
#     image_src = generated_image.get_attribute('src')

#     # Save the image locally
#     save_image(image_src, output_folder, os.path.basename(image_path))

# def save_image(image_src, output_folder, original_filename):
#     # If the image source is a data URI, we need to decode and save it
#     if image_src.startswith('data:image'):
#         # Extract base64 data from the data URI
#         image_data = image_src.split(',')[1]
#         image_bytes = base64.b64decode(image_data)

#         # Save the image as a file
#         output_path = os.path.join(output_folder, f"generated_{original_filename}")
#         with open(output_path, 'wb') as f:
#             f.write(image_bytes)
#         print(f"Image saved to {output_path}")
    
#     # If it's a URL, we can directly download the image
#     else:
#         response = requests.get(image_src)
#         output_path = os.path.join(output_folder, f"generated_{original_filename}")
#         with open(output_path, 'wb') as f:
#             f.write(response.content)
#         print(f"Image downloaded to {output_path}")
# # //*[@id="component-25"]/button/button/img

# def scrape_and_process(folder_path):
#     # Get all images from the folder
#     image_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(('png', 'jpg', 'jpeg'))]

#     for image_file in image_files:
#         upload_and_generate(image_file)

# # Define your folder path containing the images
# folder_path = './frames/final'

# # Start scraping and processing
# scrape_and_process(folder_path)

# # Close the browser once done
# browser.quit()
# Define your API URL (Replace with the actual Stable Diffusion API endpoint)