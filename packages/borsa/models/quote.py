from dataclasses import dataclass

@dataclass(slots=True)
class Quote:
  text: str
  author: str