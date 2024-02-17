from pydantic import BaseModel, UUID4


class NewComment(BaseModel):
    feedback: str


class ProcessedComment(BaseModel):
    id: UUID4
    type: str


class FeedbackOnComment(BaseModel):
    comment: str
    feedback: str
