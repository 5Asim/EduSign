from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pose_to_animated_video import merge_pose_videos
import time
import requests
import os
from selenium.webdriver.chrome.options import Options

def init_browser(download_folder):
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', {
        "download.default_directory": download_folder,  # Set download directory
        "download.prompt_for_download": False,  # Disable download prompt
        "download.directory_upgrade": True,  # Allow directory upgrade
        "safebrowsing.enabled": True  # Enable safe browsing
    })
    # Initialize the browser with the specified options
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    browser.get('https://sign.mt')  # URL of the website being scraped
    time.sleep(5)  # Wait for the page to load
    return browser


def download_video(browser, video_index):
    # Enter text in the input field
    # Only give small inputs    

    # Wait for the video to load
    time.sleep(200)
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

    current_folder = os.path.dirname(os.path.abspath(__file__))  # Get the current script's directory
    browser = init_browser(current_folder)
    
    for index, text in enumerate(segments):
        input_field = browser.find_element(By.XPATH, '//*[@id="desktop"]')
        input_field.clear()  # Clear any existing text
        input_field.send_keys(text.strip())  # Send the new segment text
        
        time.sleep(10)  # Adjust this based on how long it takes to generate the video

        download_video(browser, index)
        time.sleep(5)  # Wait for the download to initiate

    browser.quit()
    
def run_background_task():
    print("Starting background task for text-to-pose scrapper...")
    text_to_pose_scrapper()
    file_names = [os.path.join('./final_videos', file) for file in os.listdir('./final_videos')]
    merge_pose_videos(file_names)
    print("Background task completed.")

# if __name__ == "__main__":
#     file_names = [os.path.join('./final_videos', file) for file in os.listdir('./final_videos')]
    # merge_pose_videos(file_names)

    