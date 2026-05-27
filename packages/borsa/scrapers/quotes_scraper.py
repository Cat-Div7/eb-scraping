from bs4 import BeautifulSoup

from ..core.http.client import session
from .base import BaseScraper


class QuotesScraper(BaseScraper):
  URL = 'https://quotes.toscrape.com'

  def scrape(self):
    response = session.get(self.URL)

    snap = BeautifulSoup(response.text, 'html.parser')

    quotes = []
    for item in snap.select('.quote'):
      text = item.select_one('.text').get_text()
      author = item.select_one('.author').get_text()

      quotes.append({
        'text': text,
        'author': author
      })

    return quotes