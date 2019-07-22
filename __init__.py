import sys

class ProgressBar:
    def __init__(self, name="Progress", char='#'):
        self.name = name
        self.char = char

    def set_progress(self, progress):
        self.progress = progress
        width_done = int(self.width * progress)
        self.done_str = self.char * width_done
        self.to_do_str = ' ' * (self.width - width_done)

    def update(self, progress=None):
        if progress != None:
            self.set_progress(progress)
        percent = str(int(self.progress * 100))
        ret = sys.stdout.write(f'\r{self.name}: [{self.done_str}{self.to_do_str}] {percent}%')

    def start(self):
        # TODO: Read terminal width
        # TODO: Move width reading into update method
        self.width = 60
        self.update(progress=0)
