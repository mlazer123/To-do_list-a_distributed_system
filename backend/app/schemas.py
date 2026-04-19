from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str


class TaskResponse(BaseModel):
    id: int
    title: str

    class Config:
        from_attributes = True


class MessageResponse(BaseModel):
    message: str