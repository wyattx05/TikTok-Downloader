import requests
import os
from time import sleep

# Read video links from links.txt
with open('links.txt', 'r') as file:
    video_links = [line.strip() for line in file if line.strip()]

# Folder to save the videos
output_folder = "TikTokVideos"
os.makedirs(output_folder, exist_ok=True)

# Function to download a video with retries
def download_video(link, filename, retries=3, timeout=10):
    for attempt in range(retries):
        try:
            response = requests.get(link, stream=True, timeout=timeout)
            response.raise_for_status()
            with open(filename, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f"Downloaded: {filename}")
            return
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                sleep(2)  # Wait before retrying
            else:
                print(f"Failed to download {link} after {retries} attempts")

for idx, link in enumerate(video_links):
    filename = os.path.join(output_folder, f"video_{idx + 1}.mp4")
    download_video(link, filename)
