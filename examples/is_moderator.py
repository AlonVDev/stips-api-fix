"""
An example script to check if a user is a moderator
"""

from stips import StipsClient
from stips.enums import Badge

api = StipsClient()


def is_moderator(username: str):
  user = api.search_profile(username)

  if not user:
    raise ValueError(f"User {username} not found")

  profile = user.get_profile()  # get access to badges

  return any(badge in profile.badges for badge in (Badge.moderator, Badge.senior_moderator))


print(is_moderator("Hela"))  # True
print(is_moderator("*Lili*"))  # False
