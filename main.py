from fastapi import FastAPI

# 创建FastAPI实例
app = FastAPI()

# async def 定义异步函数的方法
# @app.get("/") 定义路由
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
