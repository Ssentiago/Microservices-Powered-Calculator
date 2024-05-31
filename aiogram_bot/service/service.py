import requests


async def api_calculate(expression):
    r = requests.post("http://127.0.0.1:8000/calculate", json={
        "expr": expression
    }, headers = {
        "Content-Type": "application/json"
    }, )

    if r.status_code == 200:
        return r.json()["result"]
    return ""
