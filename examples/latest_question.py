"""
An example script to see the latest posted question
"""

from stips import StipsClient

api = StipsClient()

questions = api.get_new_questions()
latest = questions[0]

print(f'{latest.title=}')
print(f'author: {latest.author.name if not latest.anonymous else "anonymous"}')
print(f'{latest.answer_count=}')
