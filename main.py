"""
Stock API - 股票数据查询
"""
from fastapi import FastAPI
import requests

app = FastAPI(title="Stock API", version="1.0.0")

@app.get("/")
def root():
    return {"message": "Stock API", "endpoints": ["/quote/{symbol}"]}

@app.get("/quote/{symbol}")
def get_quote(symbol: str):
    """获取股票报价"""
    # 使用免费API示例
    return {"symbol": symbol.upper(), "price": 100.0, "currency": "USD"}

@app.get("/list")
def list_stocks():
    return {"stocks": ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
