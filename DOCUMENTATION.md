
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
```
In the episode of SpongeBob SquarePants, "Survival of the Idiots", Spongebob called Patrick which nickname? | Answer: Pinhead
```

### *await* trivia.get_specific_question(*\**kwargs*)
Gets a specific question based on the kwargs you passed in. 

#### Parameters:
**kwargs**: Key word arguments used to get a specific question.

#### Valid kwargs:
- amount: The amount of questions you want. Must be between 0-50.
- type: The type of question you want. Must be either "multiple" (For 4 choices) or "boolean" (For true/false answers)
- category: The category of question you want. Must be a valid category integer. View CATEGORIES for int to string category mapping.
- difficulty: The difficulty of the question you want. Must be either easy, medium or hard.

#### Returns Type
List[<a href=https://github.com/niztg/aiotrivia/blob/master/DOCUMENTATION.md#aiotriviaquestionquestion>Question</a>]

#### Raises:
**InvalidKwarg**: If a kwarg you passed in was not in the valid kwargs.<br>
**InvalidAmount**: If your amount is too large, or <= 0.<br>
**InvalidType**: If your type is not 'boolean' or 'multiple'.<br>
**InvalidCategory**: If your category is not an integer, or your category is not in the valid category list.<br>
**InvalidDifficulty**: If your difficulty is not 'easy', 'medium' or 'hard'<br>
**ResponseError**: If the api does not have enough questions to accommodate your parameters. <br>

#### Example Usage:
```py
questions = await trivia.get_specific_question(amount=3, category=15, difficulty='easy', type='boolean')
for question in questions:
     print(f"{question.question} => {question.type} | {question.category}")
```
returns => 
```
The 2005 video game "Call of Duty 2: Big Red One" is not available on PC. => boolean | Entertainment: Video Games
In Team Fortress 2, being disguised as a scout or medic results in a speed boost. => boolean | Entertainment: Video Games
The main playable character of the 2015 RPG "Undertale" is a monster. => boolean | Entertainment: Video Games
``` 
 
## aiotrivia.question.Question
The question type returned when getting a question from the API. 

### `Question.category`
The string of the question's category.

Type: str

### `Question.type`
Returns the question's type. (`mutiple` or `boolean`)

Type: str

### `Question.question`
The question text itself.

Type: str

### `Question.answer`
The correct answer to the question

Type: str

### `Question.incorrect_answers`
The incorrect answers of the question.

Type: list

### `Question.responses`
Returns a random shuffled list of all the responses to the question, including the correct answer, incorrect answers, and custom incorrect answers

### Question.add_incorrect_answers(*\*args*)

#### Parameters:
args: The incorrect answers you want to append to the incorrect answers list.

#### Example Usage:
```py
question = await client.get_specific_question(category=11)
question = question[0]
question.add_incorrect_answers('bruh', 'moment')
print(question.responses)
```
returns => 
```
['A New Hope', 'The Force Awakens', 'bruh', 'moment', 'Revenge of the Sith', 'The Phantom Menace']
```

## Exceptions
All of the custom aiotrivia exceptions (InvalidAmount, InvalidDifficulty, InvalidType, InvalidCategory, InvalidKwarg, ResponseError) are subclasses of AiotriviaException. This means that:
```py
try:
     # code
except AiotriviaException as e:
     raise e
```
Can raise all 6 of these errors. (Depending on the situation.)

#### Example Usage:
```py
try:
     q = await trivia.get_random_question('fake_difficulty')
except AiotriviaException as error:
     print(f"{error.__class__.__name__}: {error}")

```
returns => 
```
InvalidDifficulty: fake_difficulty is not a valid difficulty!
```

## CATEGORIES
