from fastapi import FastAPI

app = FastAPI()
@app.get('/')
async def dIndex():
   return {"FIO: Горбунова А.С"}

@app.get('/users')
async def d_Index():
   return "email: anIs@mail.ru"

@app.get('/tools')
async def dIndexY():
   return " опыт работы с HTML5, CSS3, JS"
