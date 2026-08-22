from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field
# BaseModel is used to define the schema for the data that will be sent and received by the API.
# ConfigDict is used to configure the behavior of the model.
# Field is used to provide additional metadata for the fields in the model.

class UserBase(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    email: EmailStr
    image_file: Optional[str] = None

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    image_file: Optional[str] = None
    image_path: str

class UserUpdate(BaseModel):
    username: Optional[str] = Field(default=None, min_length=1, max_length=50)
    email: Optional[EmailStr] = Field(default=None, max_length=120)
    image_file: Optional[str] = Field(default=None, min_length=1, max_length=200)

class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1, max_length=100)

class PostUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=100)
    content: Optional[str] = Field(default=None, min_length=1)

class PostCreate(PostBase):
    user_id: int    #temporary solution for now, will be removed when we implement authentication

class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    date_posted: datetime
    author: UserResponse
