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

### discord.py command usage

```py
from aiotrivia.client import TriviaClient
from aiotrivia.exceptions import InvalidDifficulty
from discord.ext import commands

class TriviaCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.trivia = TriviaClient()
        
    @commands.command()
    async def trivia(self, ctx, difficulty):
        try:
            question = await self.trivia.get_random_question(difficulty)
         except InvalidDifficulty:
            return await ctx.send(f'{difficulty} is not a valid difficulty!') 
         answers = question.incorrect_answers + [question.answer]
         random.shuffle(answers)
         answers = '\n'.join([f"{index}. {value}" for index, value in enumerate(answers, 1)])
         await ctx.send(f"**{question.question}**\n{answers}\n{question.type.capitalize()} Question about {question.category} of {question.difficulty} difficulty")
```

         
