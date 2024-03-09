from fastapi import FastAPI 
from routes.routes import router
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(router)

origins = [
    "chrome-extension://ifonkoabimjngaeomelmfaifpaojiofb",
    "https://commu-net.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET,HEAD,PUT,PATCH,POST,DELETE"],
    allow_headers=["*"],
)




if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=5000 , reload=True)