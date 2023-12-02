from pydantic import BaseModel
class Action(BaseModel):
    action_1:str
    action_2:str
class ApiGetLoginResponse(BaseModel):
    name:str = None
    status:int = None
    action:Action = None

