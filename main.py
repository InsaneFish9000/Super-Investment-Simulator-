from fastapi import FastAPI

app = FastAPI()

import pandas as pd
df = pd.read_csv("data/sp500_aligned.csv")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/calculate")
def calculate_investment(start_date:str, start_amount:float):

    # TODO: Load data from CSV - Loaded in memory once

    # TODO: Find price at start_date 
    init_price_row = df[df["Price"] == start_date]
    init_price = init_price_row["SP500_Close"].iloc[0]

    # TODO: Find current price
    
    curr_price = df.iloc[-1]["SP500_Close"]

    # TODO: Calculate returns
    return_percent_value = curr_price/init_price
    real_return = start_amount * return_percent_value

    return {
        "start_date": start_date,
        "initial_investment": start_amount,
        "current_value": real_return,
        "total_return": real_return - start_amount,
        "return_percentage": (return_percent_value - 1)*100
    }

