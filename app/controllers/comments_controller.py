from fastapi import APIRouter
from fastapi.exceptions import HTTPException
import uuid
from pydantic import UUID4

from app.schemas.comments import NewComment, ProcessedComment, FeedbackOnComment
from app.schemas.comment_types import CommentTypes

comments_router = APIRouter(prefix='/comments')

comments_router.tags = ["Comments"]


@comments_router.post("/process_comment", response_model=ProcessedComment)
async def process_comment(comment: NewComment):

    response = ProcessedComment(id=uuid.uuid4(), type=CommentTypes.positive.name)
    return response


@comments_router.get("/feedback_on_comment/{comment_id}", response_model=FeedbackOnComment)
async def process_comment(comment_id: UUID4):
    print(comment_id)
    response = FeedbackOnComment(comment="str", feedback="str")
    return response
