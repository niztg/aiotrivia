# aiotrivia
Async Wrapper for the OpenTDB API

<<<<<<< HEAD
#### aiotrivia.client.TriviaClient
<p>The trivia client used to fetch questions</p>
<ul>
<li>aiotrivia.client.TriviaClient.get_random_question(difficulty=random.choice(['easy', 'medium', 'hard'])) - Gets a random trivia question</li>
<li></li>
<li></li>
</ul>

#### <em>aiotrivia.question.Question</em>
<p>The question type returned when fetching a question</p>
<ul>
<li></li>
<li></li>
<li></li>
<li></li>
</ul>
=======

### Example Usage
```py
from aiotrivia import TriviaClient
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
from aiotrivia import TriviaClient, InvalidDifficulty
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
         final_answers = '\n'.join([f"{index}. {value}" for index, value in enumerate(answers, 1)])
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

         
>>>>>>> baf24ba000c6f222fca3385bfb5a29ef4fce68b2
