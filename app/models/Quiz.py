from beanie import Document
from typing import List, Dict

class Question:
    question_id: int
    question_text: str
    options: Dict[str, str]
    correct_option: str

class Quiz(Document):
    quiz_id: int
    user_id: int
    topic: str
    difficulty: str
    number_of_questions: int
    questions: List[Question]

    class Settings:
        collection = "quizzes"
        indexes = ["quiz_id"]
