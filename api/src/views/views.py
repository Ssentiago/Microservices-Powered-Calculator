import os
import sys

from fastapi import APIRouter, Body
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '..', 'service'))

from service import calculate_expression

router = APIRouter()


@router.post("/calculate")
async def calculate(expr: str = Body(embed = True)):
    result = await calculate_expression(expr)
    return {"result": result}