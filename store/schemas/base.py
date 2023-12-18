from datetime import datetime
from pydantic import UUID4, BaseModel, Field


class BaseSchemaMixin(BaseModel):
    class Config:
        from_attributes = True


class OutMixin(BaseModel):
    id: UUID4 = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()
