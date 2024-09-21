from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests

# Function to initialize the browser
def init_browser():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get('https://sign.mt')
    time.sleep(5)  # wait for the page to load
    return browser

# Enter text in the input field
# Only give small inputs
input_field = init_browser().find_element(By.XPATH, '//*[@id="desktop"]')
text = "Hello, how are you? I am fine."
input_field.send_keys(text)

# Wait for the video to load
time.sleep(1000)


def download_video(browser, video_index):
    # Find the video element and download it
    video = browser.find_element(
        By.XPATH, '//*[@id="content"]/app-spoken-to-signed/app-signed-language-output/video')
    video_url = video.get_attribute('src')
    print("video_url: " + video_url)

    browser.execute_script("""
        const videoElement = arguments[0];
        const videoIndex = arguments[1];
        const blobUrl = videoElement.src;
        
        fetch(blobUrl)
            .then(response => response.blob())
            .then(blob => {
                const a = document.createElement('a');
                a.href = URL.createObjectURL(blob);
                a.download = 'video_' + videoIndex + '.mp4';
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
            });
    """, video, video_index)

def read_text_segments(file_path):
    with open(file_path, 'r') as file:
        segments = file.readlines()
    return segments

def text_to_pose_scrapper():
    # Path to the file containing the text segments
    file_path = './transcript.txt'
    segments = read_text_segments(file_path)
    
    browser = init_browser()

    for index, text in enumerate(segments):
        input_field = browser.find_element(By.XPATH, '//*[@id="desktop"]')
        input_field.clear()  # Clear any existing text
        input_field.send_keys(text.strip())  # Send the new segment text
        
        time.sleep(10)  # Adjust this based on how long it takes to generate the video

        download_video(browser, index)
        time.sleep(5)  # Wait for the download to initiate

    browser.quit()