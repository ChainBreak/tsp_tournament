from pydantic import BaseModel
from typing import List, Optional

class Submission(BaseModel):
    user_name      : str
    algorithm_name : Optional[str]
    message        : Optional[str]
    city_order     : List[int]


class SubmissionResponse(BaseModel):
    path_length: float
    success    : bool
    error_msg  : str


class Cities(BaseModel):
    city_locations : List[List[float]]

class LeaderBoardEntry(BaseModel):
    user_name      : str
    algorithm_name : Optional[str]
    message        : Optional[str]
    path_length    : Optional[float]
    city_order     : List[int]

class LeaderBoard(BaseModel):
    total_submission_count : int
    city_locations         : List[List[float]]
    leading_submissions    : List[LeaderBoardEntry]