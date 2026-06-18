from typing import Optional

from pydantic import BaseModel


class UpdateProfile(BaseModel):
    name: str
    phone: Optional[str] = None
    company: Optional[str] = None
