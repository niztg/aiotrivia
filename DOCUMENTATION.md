
# Documentation for aiotrivia
#### Async Python Wrapper for The OpenTDB API
> <a href=https://github.com/niztg/aiotrivia/blob/master/DOCUMENTATION.md#aiotriviaclienttriviaclient>TriviaClient</a><br><a href=https://github.com/niztg/aiotrivia/blob/master/DOCUMENTATION.md#aiotriviaquestionquestion>Question</a><br><a href=https://github.com/niztg/aiotrivia/blob/master/DOCUMENTATION.md#exceptions>Exceptions</a><br><a href=https://github.com/niztg/aiotrivia/blob/master/DOCUMENTATION.md#categories>CATEGORIES</a>


## aiotrivia.client.TriviaClient
The main trivia client used to get questions from the API. Start by creating an instance of this:
```py
from aiotrivia import TriviaClient

trivia = TriviaClient()
```
<em>Note: You can call your instance whatever you want. For the sake of this example, we will call it `trivia`.</em>

### *await* trivia.get_random_question(*difficulty*)
Returns a random trivia question.

#### Parameters:
**difficulty**[optional]: The difficulty of question you want. Defaults to a random choice between 'easy', 'medium' and 'hard'

#### Returns Type:
<a href=https://github.com/niztg/aiotrivia/blob/master/DOCUMENTATION.md#aiotriviaquestionquestion>Question</a>

#### Raises:
**InvalidDifficulty**: If the difficulty you passed in is not 'easy', 'medium' or 'hard'

#### Example Usage:
```py
question = await trivia.get_random_question('medium')
print(f"{question.question} | Answer: {question.answer}")
```
returns => <br>
`In the episode of SpongeBob SquarePants, "Survival of the Idiots", Spongebob called Patrick which nickname? | Answer: Pinhead`

### *await* trivia.get_specific_question(*\**kwargs*)
Gets a specific question based on the kwargs you passed in. 

#### Parameters:
**kwargs**: Key word arguments used to get a specific question.

#### Valid kwargs:
- amount: The amount of questions you want. Must be between 0-50.
- type: The type of question you want. Must be either "multiple" (For 4 choices) or "boolean" (For true/false answers)
- category: The category of question you want. Must be a valid category integer. View CATEGORIES for int to string category mapping.
- difficulty: The difficulty of the question you want. Must be either easy, medium or hard.

#### Raises:
**InvalidKwarg**: If a kwarg you passed in was not in the valid kwargs.
**InvalidAmount**: If your amount is too large, or <= 0.
**InvalidType**: If your type is not 'boolean' or 'multiple'.
**InvalidCategory**: If your category is not an integer, or your category is not in the valid category list.
**InvalidDifficulty**: If your difficulty is not 'easy', 'medium' or 'hard'
**ResponseError**: If the api does not have enough questions to accommodate your parameters. 
 
## aiotrivia.question.Question


## Exceptions


## CATEGORIES
