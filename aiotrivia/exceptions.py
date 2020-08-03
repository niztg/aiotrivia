class InvalidDifficulty(Exception):
    def __init__(self, error='That is not a valid difficulty! Valid difficulties include %s' % ', '.join(
        ['easy', 'medium', 'hard'])):
        self.error = error

    def __str__(self):
        return self.error


class InvalidAmount(Exception):
    def __init__(self, error='Invalid amount! The amount must be in between 0 and 50.'):
        self.error = error

    def __str__(self):
        return self.error


class InvalidType(Exception):
    def __init__(self, error='Invalid type! The type must be either "multiple" or "boolean".'):
        self.error = error

    def __str__(self):
        return self.error


class InvalidKwarg(Exception):
    def __init__(self, error='You passed in invalid kwargs!'):
        self.error = error

    def __str__(self):
        return self.error


class InvalidCategory(Exception):
    def __init__(self,
                 error='You passed in an invalid category. Note that the category must be a number. See aiotrivia.CATEGORIES for valid category numbers.'):
        self.error = error

    def __str__(self):
        return self.error


class ResponseError(Exception):
    def __init__(self,
                 error='The API does not have enough questions to accomodate your request. Perhaps be less specific?'):
        self.error = error

    def __str__(self):
        return self.error
