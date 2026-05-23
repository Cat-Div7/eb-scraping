from dataclasses import dataclass
from datetime import datetime

@dataclass
class BaseModel:
  created_at: datetime = datetime.now()