"""
The files containing question data
"""

from html import unescape


class Question:
    __slots__ = ('category', 'type', 'question', 'answer', '_incorrect_answers')

    def __init__(self, data):
        self.category = data.get('category')
        self.type = data.get('type')
        self.question = unescape(str(data.get('question')))
        self.answer = unescape(str(data.get('correct_answer')))
        self._incorrect_answers: list = data.get('incorrect_answers')

    def __repr__(self):
        return f"<aiotrivia.question.Question: question={self.question}, category={self.category}, type={self.type}>"

    @property
    def incorrect_answers(self) -> list:
        return self._incorrect_answers

    def add_incorrect_answers(self, *args):
        for item in args:
            self._incorrect_answers.append(item)
