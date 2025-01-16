import requests
import os

# Read video links from links.txt
with open('links.txt', 'r') as file:
    video_links = [line.strip() for line in file if line.strip()]

# Folder to save the videos
output_folder = "TikTokVideos"
os.makedirs(output_folder, exist_ok=True)

for idx, link in enumerate(video_links):
    try:
        response = requests.get(link, stream=True)
        response.raise_for_status()

        # Create a filename based on index
        filename = os.path.join(output_folder, f"video_{idx + 1}.mp4")
        with open(filename, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Failed to download {link}: {e}")