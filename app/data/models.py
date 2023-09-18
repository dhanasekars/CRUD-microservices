""" 
Created on : 18/09/23 5:39 am
@author : ds  
"""

from typing import Optional
from pydantic import BaseModel, Field, constr, model_validator

class TodoItem(BaseModel):
    """Base model for to-do list"""

    title: constr(min_length=1, strip_whitespace=True)
    description: Optional[str] = None
    doneStatus: bool = Field(default=False)


class ReturnTodo(TodoItem):
    """extending TodoItem class with UUID"""

    id: str


class UpdateTodo(BaseModel):
    """Model with optional fields where at least one must have a value."""

    title: Optional[constr(min_length=1, strip_whitespace=True)] = None
    description: Optional[str] = None
    doneStatus: Optional[bool] = None

    @model_validator(mode="before")
    def check_blank_fields(cls, values):
        """function to check at least one of the three fields is given"""
        num_fields_with_values = sum(
            1 for value in values.values() if value is not None
        )
        if num_fields_with_values < 1:
            raise ValueError(
                "At least one of 'title', 'description', or 'doneStatus' must have a value"
            )
        return values
