# Stips API

> A rich API wrapper for [**stips.co.il**](https://stips.co.il) written in Python. <br>

## ⛲ Install

Install using pip:

```bash
pip install stipspy
```

## 🪴 Usage

You can choose to use the API with or without logging in,
but some methods will be unavailable without authentication.

#### Example without user authentication

```python
# see the latest question

from stips import StipsClient

api = StipsClient()

questions = api.get_new_questions()
latest = questions[0]

print(f'{latest.title=}')
print(f'author: {latest.author.name if not latest.anonymous else "anonymous"}')
print(f'{latest.answer_count=}')
```

<br>

#### Example with authentication

```python
# print unread messages

from stips import StipsClient

api = StipsClient(email=email, password=password)
# or
api = StipsClient(cookies=cookies)

new_messages_count = api.get_notifications_count().messages

print(f'Found {new_messages_count} unread message(s)')

if new_messages_count > 0:
  # this only covers first 28 chats
  # for better searching see pagetools.iterpages
  messages_list = api.get_messages_list(page=1)

  for direct in messages_list:
    if direct.new_messages_count > 0:
      print(f'{direct.new_messages_count} message(s) from {direct.from_user.name}: {direct.last_message}')
```

More examples in the [/examples directory](examples)

## 📃 Documentation

You can find the documentation here:<br/>
https://stips-py.readthedocs.io/en/latest/

## 🛣️ Roadmap

- [x] 🦸 Support all API endpoints
- [x] 🐥 Easy to use API
- [x] 📃 Create documentation
- [ ] 🚏 Handle API Ratelimit

## 🙏 Contributing

Feel free to post a pull request or an issue if you
have any ideas, suggestions, or if you've found any bugs.