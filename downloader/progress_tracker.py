class ProgressTracker:

    def __init__(self):
        self.current = 0
        self.total = 0

    def start(self, total):
        self.total = total
        self.current = 0

    def update(self):
        self.current += 1

    def percentage(self):

        if self.total == 0:
            return 0

        return (
            self.current /
            self.total
        ) * 100