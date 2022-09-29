
from fastapi import FastAPI  ,Query
from fastapi.middleware.cors import CORSMiddleware
from logger import customLogger

log = customLogger.getInstance()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#test
@app.get('/api/test1')
def test1(num: int = Query(default=1)):
    for i  in range(num):
        log.showLog(f'{i} 번째 로그 입니다.')
    return {
        'code':200
    }







