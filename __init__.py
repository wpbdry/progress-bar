import sys

class ProgressBar:
    def __init__(self, name="Progress"):
        self.name = name

    def set_progress(self, progress):
        self.progress = progress
        self.done = '#' * self.width * progress
        self.to_do = ' ' * (self.width - done)

    def update(self, progress=None):
        if progress:
            self.set_progress(progress)
        percent = str(self.progress * 100)
        sys.stdout.write(f'\r{name}: [{done}{to_do}] {percent}%')

    def start(self):
        # TODO: Read terminal width
        self.width = 60
        self.update(0)
