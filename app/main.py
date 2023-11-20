from fastapi import FastAPI

app = FastAPI(title='Date Night API')


@app.get('/')
async def root():
    return {'message': 'test'}
