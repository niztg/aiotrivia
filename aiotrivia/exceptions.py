class InvalidDifficulty(Exception):
    def __init__(self, error='That is not a valid difficulty!'):
        self.error = error

    def __str__(self):
        return self.error
