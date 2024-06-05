from fastapi import FastAPI

# 创建FastAPI实例
app = FastAPI()

# async def 定义异步函数的方法
# @app.get("/") 定义路由
# @app路由装饰器 get()请求方法 ""访问路径
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


#运行服务器
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)