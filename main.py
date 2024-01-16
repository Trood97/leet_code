

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def home_page():
	return {'message':'HI there , Anand greets you lol,'}

@app.get('/add')
async def add_two_numbers(a:int,b:int)-> int:
	return a+b