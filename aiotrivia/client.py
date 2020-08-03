"""
-*- coding: utf-8 -*-
Async Wrapper for the OpenTDBAPI
"""

from aiotrivia.question import Question
from aiotrivia.exceptions import *
import aiohttp
import requests
from random import choice
from typing import List

CATEGORIES = {}
request = requests.get('https://opentdb.com/api_category.php').json()
for i in request['trivia_categories']:
    CATEGORIES[i.get('id')] = i.get('name')


class TriviaClient:

    @staticmethod
    async def get_random_question(difficulty=choice(['easy', 'medium', 'hard'])) -> Question:
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://opentdb.com/api.php",
                              params={"amount": 1, "difficulty": difficulty}) as r:
                data = await r.json()
            await cs.close()
        difficulties = ('easy', 'medium', 'hard')
        if difficulty not in difficulties:
            raise InvalidDifficulty("%s is not a valid difficulty!" % difficulty)
        return Question(data=data.get('results')[0])

    @staticmethod
    async def get_specific_question(**kwargs) -> List[Question]:
        valid_kwargs = ['amount', 'type', 'category', 'difficulty']
        params = {}
        questions = []
        if any(item not in valid_kwargs for item in kwargs.keys()):
            raise InvalidKwarg(
                "You have passed an invalid keyword argument! Valid keyword arguments include: %s" % ', '.join(
                    valid_kwargs))
        amount = kwargs.get('amount', 1)
        type = kwargs.get('type')
        category = kwargs.get('category')
        difficulty = kwargs.get('difficulty')
        if not 0 < amount < 50 or not isinstance(amount, int):
            if amount:
                raise InvalidAmount()
            else:
                pass
        else:
            params['amount'] = amount
        if type not in ['multiple', 'boolean']:
            if type:
                raise InvalidType()
            else:
                pass
        else:
            params['type'] = type
        if not isinstance(category, int) or category not in [*CATEGORIES.keys()]:
            if category:
                raise InvalidCategory()
            else:
                pass
        else:
            params['category'] = category
        if difficulty not in ['easy', 'medium', 'hard']:
            if difficulty:
                raise InvalidDifficulty()
            else:
                pass
        else:
            params['difficulty'] = difficulty
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://opentdb.com/api.php", params=params) as r:
                data = await r.json()
            await cs.close()
        if data['response_code'] == 1:
            raise ResponseError()
        for item in data.get('results'):
            questions.append(Question(data=item))
        return questions
