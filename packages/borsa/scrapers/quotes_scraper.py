from ..core.http.client import session
from ..parsers.quotes_parser import QuotesParser
from .base import BaseScraper


class QuotesScraper(BaseScraper):
  URL = 'https://quotes.toscrape.com'

  def __init__(self):
    self.parser = QuotesParser()
    
  def scrape(self):
    response = session.get(self.URL)

    return self.parser.parse(response.text)