from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 剩余可抽的数字池
numbers = [str(i).zfill(2) for i in range(100)]
# 抽取记录
history = []

@app.get("/draw")
def draw_number():
    if not numbers:
        return {"error": "已抽完"}

    num = random.choice(numbers)
    numbers.remove(num)
    history.append(num)

    return {
        "number": num,
        "left": len(numbers),
        "history": history
    }

@app.get("/reset")
def reset():
    global numbers, history
    numbers = [str(i).zfill(2) for i in range(100)]
    history = []
    return {"status": "reset"}
