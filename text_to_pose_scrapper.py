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
# Only give small inputs
input_field = browser.find_element(By.XPATH, '//*[@id="desktop"]')
text = "Hello, how are you? I am fine."
input_field.send_keys(text)

# Wait for the video to load
time.sleep(1000)

# Find the video element and download it
video = browser.find_element(
    By.XPATH, '//*[@id="content"]/app-spoken-to-signed/app-signed-language-output/video')
video_url = video.get_attribute('src')
print("video_url: " + video_url)

# Download the video
browser.execute_script("""
    const videoElement = document.querySelector('video');
    const blobUrl = videoElement.src;
    
    // Fetch the blob content from the blob URL
    fetch(blobUrl)
        .then(response => response.blob())
        .then(blob => {
            const a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            a.download = 'video.mp4';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        });
""")

# Close the browser
browser.quit()
