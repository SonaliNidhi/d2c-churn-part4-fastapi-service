
from pydantic import BaseModel, Field

class CustomerRequest(BaseModel):

    recency_days: int = Field(..., ge=0)

    frequency_180d: int = Field(..., ge=0)

    monetary_180d: float = Field(..., ge=0)

    ticket_count_90d: int = Field(..., ge=0)

    sessions_30d: int = Field(..., ge=0)

class BatchRequest(BaseModel):

    customers: list[CustomerRequest]
