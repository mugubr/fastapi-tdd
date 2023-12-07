from datetime import datetime
import uuid
from pydantic import UUID4, BaseModel, Field, SkipValidation


class CreateBaseModel(BaseModel):
    id: UUID4 = Field(default_factory=uuid.uuid4)
    created_at: SkipValidation[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: SkipValidation[datetime] = Field(default_factory=datetime.utcnow)
