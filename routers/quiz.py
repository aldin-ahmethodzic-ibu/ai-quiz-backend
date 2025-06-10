from fastapi import APIRouter, HTTPException, status, Depends
from schemas.quiz import (
    QuizGenerateRequest,
    QuizGenerateResponse,
    QuizSubmitRequest,
    QuizSubmitResponse,
    GetQuizResponse
)
from services.openai_service import generate_quiz_ai
from models.quiz import Quiz, Question
from auth.deps import get_current_user, get_current_user_id

router = APIRouter(prefix="/quiz", tags=["quiz"])

@router.post("/generate", response_model=QuizGenerateResponse, status_code=status.HTTP_201_CREATED)
async def generate_quiz(quiz_request: QuizGenerateRequest, created_by: str = Depends(get_current_user_id)) -> QuizGenerateResponse:
    return await generate_quiz_ai(
        topic=quiz_request.topic,
        difficulty=quiz_request.difficulty,
        number_of_questions=quiz_request.number_of_questions,
        created_by=created_by
    )

@router.post("/submit", response_model=QuizSubmitResponse, status_code=status.HTTP_200_OK)
async def submit_quiz(quiz_submit_request: QuizSubmitRequest) -> QuizSubmitResponse:
    quiz_id = quiz_submit_request.quiz_id
    
    quiz = await Quiz.get(quiz_id)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    
    correct_answers = {q.question_id: q.correct_option for q in quiz.questions}
    submitted_answers = quiz_submit_request.answers
    
    score = sum(1 for qid, ans in submitted_answers.items() if correct_answers.get(qid) == ans)
    
    return QuizSubmitResponse(
        score=score,
        total=quiz.number_of_questions,
        message="Quiz submitted successfully"
    )

@router.get("/{quiz_id}", response_model=GetQuizResponse)
async def get_quiz(quiz_id: int) -> GetQuizResponse:
    quiz = await Quiz.find_one(Quiz.quiz_id == quiz_id)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")

    return GetQuizResponse(
        quiz_id=quiz.quiz_id,
        topic=quiz.topic,
        difficulty=quiz.difficulty.value,  # if enum
        number_of_questions=quiz.number_of_questions,
        questions=[Question(
            question_id=q.question_id,
            question_text=q.question_text,
            options=q.options,
            correct_option=q.correct_option,
        ) for q in quiz.questions],
        created_at=quiz.created_at,
        created_by=quiz.created_by,
    )