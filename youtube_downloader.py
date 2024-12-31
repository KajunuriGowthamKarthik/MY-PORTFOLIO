from pytube import YouTube

# Function to download a YouTube video
def download_video(video_url):
    try:
        yt = YouTube(video_url)  # Create YouTube object
        stream = yt.streams.get_highest_resolution()  # Get highest resolution
        print(f"Downloading: {yt.title}")
        stream.download()  # Download the video
        print("Download complete!")
    except Exception as e:
        if "410" in str(e):
            print("The video is no longer available (HTTP 410: Gone). Try another video.")
        else:
            print(f"An error occurred: {e}")


# Input: YouTube video URL
video_url = input("Enter the YouTube video URL: ")
download_video(video_url)  # Call the function
