import requests


async def api_calculate(expression):
    try:
        r = requests.post("http://api:8000/calculate", json={
            "expr": expression
        }, headers = {
            "Content-Type": "application/json"
        }, )

        if r.status_code == 200:
            return r.json()["result"]
    except Exception as e:
        print(e)
        return None