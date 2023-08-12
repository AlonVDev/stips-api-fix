"""
This example shows how to use the pagetools.iter_pages function to iterate over
a response that is paginated (like user thanks, or questions list...).
"""

from stips import StipsClient
from stips.pagetools import iter_pages

bot = StipsClient()

wall_user = bot.search_profile('Headless', fuzz=True).get_user()
search_user = bot.search_profile('Hela', fuzz=True).get_user()

for i, thank in iter_pages(bot.get_user_thanks, user_id=wall_user.id, yield_index=True):
  if thank.author.id == search_user.id:
    print(f'#{i} [{thank.time}] {thank.text}')
    input('Show next?')
