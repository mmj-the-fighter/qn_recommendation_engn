from dataclasses import dataclass
from typing import List


@dataclass
class Question:
    difficulty: str
    text: str
    options: List[str]
    answer: int