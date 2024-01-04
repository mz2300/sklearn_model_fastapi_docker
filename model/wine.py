from pydantic import BaseModel, conlist


class Wine(BaseModel):
    data: list[conlist(float, 
                       min_length = 13, 
                       max_length = 13)]