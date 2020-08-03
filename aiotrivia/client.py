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
        amount, type, category, difficulty = kwargs.get('amount', 1), kwargs.get('type'), kwargs.get(
            'category'), kwargs.get('difficulty')
        print(amount)
        print(type)
        print(category)
        print(difficulty)
        if amount:
            if not isinstance(amount, int) or not 0 < amount < 50:
                raise InvalidAmount()
            else:
                params['amount'] = amount
        else:
            pass
        if type:
            if type.lower() not in ['multiple', 'boolean']:
                raise InvalidType()
            else:
                params['type'] = type
        else:
            pass
        if category:
            if not isinstance(category, int) or category not in [*CATEGORIES.keys()]:
                raise InvalidCategory()
            else:
                params['category'] = category
        else:
            pass
        if difficulty:
            if difficulty.lower() not in ['easy', 'medium', 'hard']:
                raise InvalidDifficulty()
            else:
                params['difficulty'] = difficulty
        else:
            pass
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://opentdb.com/api.php", params=params) as r:
                data = await r.json()
            await cs.close()
        if data['response_code'] == 1:
            raise ResponseError()
        for item in data.get('results'):
            questions.append(Question(data=item))
        return questions
