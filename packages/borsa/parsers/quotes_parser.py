from bs4 import BeautifulSoup
from ..models.quote import Quote

class QuotesParser:
  def parse(self, html: str):
    snap = BeautifulSoup(html, 'html.parser')

    quotes = []
    for item in snap.select('.quote'):
      text = item.select_one('.text').get_text()
      author = item.select_one('.author').get_text()

      quotes.append(
        Quote(
          text=text,
          author=author,
      ))

    return quotes