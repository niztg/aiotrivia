"""
-*- coding: utf-8 -*-
Async Wrapper for the OpenTDBAPI
"""

import json
from random import choice
from typing import List
from aiohttp import ClientSession

from aiotrivia.exceptions import *
from aiotrivia.question import Question

with open('categories.json', 'r') as f:
    data = json.load(f)

CATEGORIES = {int(key): value for key, value in data.items()}


class TriviaClient:
    """
    The main trivia client used to get questions from the API
    """
    url = 'https://opentdb.com/api.php'

    async def get_random_question(self, difficulty=choice(['easy', 'medium', 'hard'])) -> Question:
        difficulties = ('easy', 'medium', 'hard')
        if difficulty not in difficulties:
            raise InvalidDifficulty("%s is not a valid difficulty!" % difficulty)
        async with ClientSession() as cs:
            async with cs.get(self.url, params={"amount": 1, "difficulty": difficulty}) as r:
                data = await r.json()
            await cs.close()
        return Question(data=data.get('results')[0])

    async def get_specific_question(self, **kwargs) -> List[Question]:
        valid_kwargs = ['amount', 'type', 'category', 'difficulty']
        params = {}
        questions = []
        if any(item not in valid_kwargs for item in kwargs.keys()):
            raise InvalidKwarg(
                "You have passed an invalid keyword argument! Valid keyword arguments include: %s" % ', '.join(
                    valid_kwargs))
        amount, type, category, difficulty = kwargs.get('amount', 1), kwargs.get('type'), kwargs.get(
            'category'), kwargs.get('difficulty')
        if amount:
            if not isinstance(amount, int) or not 0 < amount < 50:
                raise InvalidAmount()
            else:
                params['amount'] = amount
        if type:
            if type.lower() not in ['multiple', 'boolean']:
                raise InvalidType()
            else:
                params['type'] = type
        if category:
            if not isinstance(category, int) or category not in CATEGORIES:
                raise InvalidCategory()
            else:
                params['category'] = category
        if difficulty:
            if difficulty.lower() not in ['easy', 'medium', 'hard']:
                raise InvalidDifficulty()
            else:
                params['difficulty'] = difficulty
        async with ClientSession() as cs:
            async with cs.get(self.url, params=params) as r:
                data = await r.json()
            await cs.close()
            if data['response_code'] == 1:
                raise ResponseError()
            for item in data.get('results'):
                questions.append(Question(data=item))
        return questions
