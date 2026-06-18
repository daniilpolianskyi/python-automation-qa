from enum import Enum

from pydantic import BaseModel


class NoteCategory(str, Enum):
    HOME = "Home"
    WORK = "Work"
    PERSONAL = "Personal"

class CreateNote(BaseModel):
    title: str
    description: str
    category: str

class UpdateNote(BaseModel):
    title: str
    description: str
    completed: bool
    category: str

class UpdateNoteCompleteStatus(BaseModel):
    completed: bool
