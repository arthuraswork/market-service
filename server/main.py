from fastapi import FastAPI, middleware

app = FastAPI()

@app.middleware
def check_token(request, call_next):
    ...