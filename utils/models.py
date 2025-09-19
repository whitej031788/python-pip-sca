from pydantic import BaseModel, Field


class EchoPayload(BaseModel):
    message: str = Field(min_length=1, max_length=200)
    count: int = Field(ge=1, le=100)
