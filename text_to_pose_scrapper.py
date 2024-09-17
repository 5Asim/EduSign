from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests

# Initialize WebDriver
# driver = webdriver.Chrome(executable_path='path_to_chromedriver')
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get('https://sign.mt')

# Wait for the page to load
time.sleep(5)

# Enter text in the input field
input_field = browser.find_element(By.XPATH, '//*[@id="desktop"]')
text = "Hello, how are you? I am fine."
input_field.send_keys(text)

# Wait for the video to load
time.sleep(240)

# Find the video element and download it
video = browser.find_element(
    By.XPATH, '//*[@id="content"]/app-spoken-to-signed/app-signed-language-output/video')
video_url = video.get_attribute('src')

# Download the video
video_response = requests.get(video_url)
with open('downloaded_video.mp4', 'wb') as f:
    f.write(video_response.content)

# Close the browser
browser.quit()
