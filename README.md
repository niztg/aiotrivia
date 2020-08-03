# aiotrivia
Async Wrapper for the OpenTDB API


### Example Usage
```py
from aiotrivia.client import TriviaClient
import asyncio

client = TriviaClient()

async def main():
    question = await client.get_random_question('easy')
    print("Question: %s | Answer: %s" % (question.question, question.answer))

asyncio.get_event_loop().run_until_complete(main())
```

#### Returns:
`Question: In Big Hero 6, what fictional city is the Big Hero 6 from? | Answer: San Fransokyo`
