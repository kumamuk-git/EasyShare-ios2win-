import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):

    def on_created(self, event):
        if event.is_directory:
            return None
        elif event.src_path.endswith(".heic"):
            time.sleep(1)
            self.convert_heic_to_png(event.src_path)
            
        elif event.src_path.endswith(".mov"):
            time.sleep(1)
            self.convert_mov_to_mp4(event.src_path)

    @staticmethod
    def convert_heic_to_png(file_path):
        output_file_path = os.path.splitext(file_path)[0] + ".png"
        subprocess.run(["magick", "mogrify", "-format", "png", "./uploads/*.HEIC"], check=True)
        os.remove(file_path)

    @staticmethod
    def convert_mov_to_mp4(file_path):
        output_file_path = os.path.splitext(file_path)[0] + ".mp4"
        size = -1
        while size != os.path.getsize(file_path):
            size = os.path.getsize(file_path)
            time.sleep(1)
        subprocess.run(["ffmpeg", "-i", file_path, "-pix_fmt", "yuv420p", output_file_path], check=True)
        os.remove(file_path)

if __name__ == "__main__":
    path_to_watch = "C:/Users/maaso/Documents/JavaScript/uploads"  # 監視するディレクトリを指定

    event_handler = Handler()
    observer = Observer()
    observer.schedule(event_handler, path_to_watch, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
