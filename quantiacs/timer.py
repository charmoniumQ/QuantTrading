from datetime import datetime

class Timer(object):
    def __init__(self, name):
        self.name = name
        self.start = datetime.now()

    def stop(self):
        self.stop = datetime.now()
        t = (self.stop - self.start).total_seconds() * 1e6
        with open('timer.csv', 'a') as file:
            file.write('{self.name},{t:.0f}\n'.format(**locals()))
