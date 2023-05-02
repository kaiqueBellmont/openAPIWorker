"""
Base model for code_list
"""
from pydantic import BaseModel
from typing import Dict, List


class CodeListRequest(BaseModel):
    code_list: List[Dict[str, str]]