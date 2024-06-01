from fastapi import APIRouter, Body

from .service.service import calculate_expression

router = APIRouter()


@router.post("/calculate")
async def calculate(expr: str = Body(embed = True)):
    result = await calculate_expression(expr)
    return {"result": result}