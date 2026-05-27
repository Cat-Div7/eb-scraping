import sys
from pathlib import Path

# Add the project root to the path so we can import packages
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from packages.borsa.scrapers.quotes_scraper import (
    QuotesScraper,
)


def main():
  scraper = QuotesScraper()
  
  data = scraper.scrape()
  
  for item in data:
    print(item)
    

if __name__ == '__main__':
  main()