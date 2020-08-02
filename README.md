# aiotrivia
Async Wrapper for the OpenTDB Api.

### Usage
```python
from aiotrivia.client import TriviaClient
import asyncio

client = TriviaClient()

async def main():
    question = await client.get_random_question(difficulty='easy')
    return question.question, question.answer, question.incorrect_answers

asyncio.get_event_loop().run_until_complete(main())
```
