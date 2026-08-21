from pydantic import BaseModel, ConfigDict, Field 
# BaseModel is used to define the schema for the data that will be sent and received by the API. 
# ConfigDict is used to configure the behavior of the model. 
# Field is used to provide additional metadata for the fields in the model.

class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1, max_length=100)
    author: str = Field(min_length=1, max_length=100)

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    date_posted: str
