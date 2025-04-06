from fastapi import APIRouter, HTTPException, status

from app.schemas.quiz import QuizGenerateRequest, QuizGenerateResponse, QuestionOptions, QuizQuestion, QuizSubmitRequest, QuizSubmitResponse

router = APIRouter(prefix="/quiz", tags=["quiz"])

@router.post("/generate", response_model=QuizGenerateResponse, status_code=status.HTTP_201_GENERATED)
async def generate_quiz(quiz_request: QuizGenerateRequest) -> QuizGenerateResponse:
    b = 1
    # Logic missing

@router.post("/submit", response_model=QuizSubmitResponse, status_code=status.HTTP_200_OK)
async def submit_quiz(quiz_submit_request: QuizSubmitRequest) -> QuizSubmitResponse:
    a = 1
    # Logic missing