from pytube import YouTube

def download_video(url, audio_only=False):
    try:
        yt = YouTube(url)
        print(f"📹 Title: {yt.title}")
        print(f"📁 Author: {yt.author}")
        print(f"⏱ Duration: {yt.length // 60} minutes")

        if audio_only:
            stream = yt.streams.filter(only_audio=True).first()
            output = stream.download()
            print(f"✅ Audio downloaded: {output}")
        else:
            stream = yt.streams.get_highest_resolution()
            output = stream.download()
            print(f"✅ Video downloaded: {output}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    url = input("🎥 Enter YouTube URL: ")
    mode = input("🎧 Download as audio only? (y/n): ").lower()
    download_video(url, audio_only=(mode == 'y'))
