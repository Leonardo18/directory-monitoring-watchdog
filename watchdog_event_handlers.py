from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os


monitoring_directory = os.getcwd() + '/monitoring-folder/'


def run():
    w = Watcher()
    w.run()


class Watcher:
    directory_to_monitoring = monitoring_directory


    def __init__(self):
        self.observer = Observer()


    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.directory_to_monitoring, recursive=True)
        self.observer.start()
        self.observer.join()


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
        elif event.event_type == 'created':
            print("Created event - %s." % event.src_path)
        elif event.event_type == 'modified':
            print("Modified event - %s." % event.src_path)
        elif event.event_type == 'deleted':
            print("Deleted event - %s." % event.src_path)


if __name__ == '__main__':
    run()
