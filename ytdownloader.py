from mutagen.easyid3 import EasyID3
import youtube_dl
import os
import time
import threading

class YTDownloader:
    """
    Class for downloading videos from YouTube.
    """

    def __init__(self):
        """
        Initialize the class with the URL of the video and the path to save the video.
        """
        self.queue = []
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def add_to_queue(self, data):
        """
        Add a video to the queue.
        """
        self.queue.append(data)

    def get_queue(self):
        """
        Return the queue.
        """
        return self.queue

    def run(self):
        """
        Run the downloader.
        """
        while True:
            if len(self.queue) > 0:
                self.download()
            else:
                pass
            # sleep for a second
            time.sleep(1)

    def download(self):
        data = self.queue.pop(0)
        """
        Download the video.
        """
        
        path = f"{data['title']} - {data['artists'][0]['name']}.mp4"
        path2 = f"{data['title']} - {data['artists'][0]['name']}.mp3"

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': path,
            'postprocessors': [],
        }
        
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([f"https://youtu.be/{data['videoId']}"])
                # convert to mp3
                os.system(f"ffmpeg -i \"{path}\" -codec:a libmp3lame -qscale:a 2 \"{path2}\"")
                # Add Metadata
                audio = EasyID3(path2)
                audio['title'] = data['title']
                audio['artist'] = data['artists'][0]["name"]
                audio['album'] = data['album']["name"]
                audio.pprint()
                audio.save()
                os.remove(path)
        except Exception as e:
            # If it fails, add the video back to the queue
            self.queue.append(data)