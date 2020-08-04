
# Documentation for aiotrivia
#### Async Python Wrapper for The OpenTDB API
> <a href=https://github.com/niztg/aiotrivia/blob/master/DOCUMENTATION.md#aiotriviaclienttriviaclient>TriviaClient</a><br><a href=https://github.com/niztg/aiotrivia/blob/master/DOCUMENTATION.md#aiotriviaquestionquestion>Question</a><br><a href=https://github.com/niztg/aiotrivia/blob/master/DOCUMENTATION.md#aiotriviaquestionquestion>Exceptions</a><br><a href=https://github.com/niztg/aiotrivia/blob/master/DOCUMENTATION.md#aiotriviaquestionquestion>CATEGORIES</a>


## aiotrivia.client.TriviaClient
The main trivia client used to get questions from the API. Start by creating an instance of this:
```py
from aiotrivia import TriviaClient

trivia = TriviaClient()
```
<em>Note: You can call your instance whatever you want. For the sake of this example, we will call it `trivia`.</em>

### `await trivia.get_random_question(difficulty)`
Returns a random trivia question.

#### Parameters:
**difficulty**[optional]: The difficulty of question you want. Defaults to a random choice between 'easy', 'medium' and 'hard'

#### Raises:
**InvalidDifficulty**: If the difficulty you passed in is not 'easy', 'medium' or 'hard'

FIX:
Pass in a valid difficulty.
 
## aiotrivia.question.Question


## Exceptions


## CATEGORIES
