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
import asyncio
import random

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
         answers = [f"{index}. {value}" for index, value in enumerate(answers, 1)]
         final_answers = '\n'.join(answers)
         await ctx.send(f"**{question.question}**\n{final_answers}\n{question.type.capitalize()} Question about {question.category} of {question.difficulty} difficulty")
         try:
            msg = await self.bot.wait_for('message', timeout=15)
            if str(answers.index(question.answer)+1) in msg.content.lower():
                return await ctx.send(f'{msg.author} got it! The answer was {question.answer}')
          except asyncio.TimeoutError:
            return await ctx.send(f"The correct answer was {question.answer}")

def setup(bot):
    bot.add_cog(TriviaCog(bot))
```

         
