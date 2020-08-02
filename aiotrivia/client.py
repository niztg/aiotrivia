"""
Async Wrapper for the OpenTDBAPI
"""

from aiotrivia.question import Question
from aiotrivia.exceptions import InvalidDifficulty
import aiohttp


class TriviaClient:

    @staticmethod
    async def get_random_question(difficulty):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://opentdb.com/api.php",
                              params={"amount": 1, "difficulty": difficulty}) as r:
                data = await r.json()
            await cs.close()
        difficulties = ('easy', 'medium', 'hard')
        if difficulty not in difficulties:
            raise InvalidDifficulty("%s is not a valid difficulty!" % difficulty)
        return Question(data=data)
