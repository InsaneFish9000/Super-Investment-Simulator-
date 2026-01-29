from datetime import datetime as dt
from fastapi import FastAPI, Body
from typing import Optional
import pandas as pd
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# --- CORS Configuration ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vue dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Data Loading ---
df = pd.read_csv("data/sp500_aligned.csv")

# --- Pydantic Models (The "Glue" for Vue) ---
class LumpSumSchema(BaseModel):
    start_date: str
    start_amount: float

class DCASchema(BaseModel):
    start_date: str
    initial_contribution: float
    recurring_contribution: float

class ValidationSchema(BaseModel):
    start_date: str
    initial_contribution: Optional[float] = None
    recurring_contribution: Optional[float] = None
    start_amount: Optional[float] = None

# --- Endpoints ---

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/calculate_lump_sum")
def calculate_lump_sum(data: LumpSumSchema):
    # Extract data from the schema
    start_date = data.start_date
    start_amount = data.start_amount

    init_price_row = df[df["Date"] == start_date]
    init_price = init_price_row["SP500_Close"].iloc[0]
    curr_price = df.iloc[-1]["SP500_Close"]

    return_percent_value = curr_price / init_price
    real_return = start_amount * return_percent_value

    return {
        "start_date": start_date,
        "initial_investment": start_amount,
        "current_value": real_return,
        "total_return": real_return - start_amount,
        "return_percentage": (return_percent_value - 1) * 100
    }

@app.post("/calculate_growth_lump_sum")
def calculate_growth_lump_sum(data: LumpSumSchema):
    start_date = data.start_date
    start_amount = data.start_amount

    idx = df.index[df["Date"] == start_date][0]
    current_balance = start_amount
    growth_overtime = []
    old_price = df["SP500_Close"].iloc[idx]

    for i in range(idx, len(df)):
        new_price = df["SP500_Close"].iloc[i]
        current_balance = current_balance * (new_price / old_price)
        growth_overtime.append(round(current_balance, 2))
        old_price = new_price

    return {"growth_overtime": growth_overtime}

@app.post("/calculate_dca_growth")
def calculate_dca_growth(data: DCASchema):
    start_date = data.start_date
    initial_contribution = data.initial_contribution
    recurring_contribution = data.recurring_contribution

    idx = df.index[df["Date"] == start_date][0]
    current_balance = initial_contribution
    growth_overtime = []
    old_price = df["SP500_Close"].iloc[idx]
    contribution = initial_contribution

    for i in range(idx, len(df)):
        new_price = df["SP500_Close"].iloc[i]
        current_balance = current_balance * (new_price / old_price)
        current_balance = current_balance + recurring_contribution
        contribution = contribution + recurring_contribution
        growth_overtime.append(round(current_balance, 2))
        old_price = new_price
    
    current_balance = round(current_balance, 2)
    your_contribution = round(contribution, 2)
    total_interest_earned = round(current_balance - contribution, 2)
    
    return {
        "growth_overtime": growth_overtime,
        "current_balance": current_balance,
        "your_contribution": your_contribution,
        "total_interest_earned": total_interest_earned
    }

@app.get("/get_valid_date_range")
def get_valid_date_range():
    first_date = df["Date"].iloc[0]
    last_date = df["Date"].iloc[-1]
    return {"first_date": first_date, "end_date": last_date}

@app.post("/validate_inputs")
def validate_inputs(data: ValidationSchema):
    start_date = data.start_date
    initial_contribution = data.initial_contribution
    recurring_contribution = data.recurring_contribution
    start_amount = data.start_amount
    
    error_messages = []
    first_date = df["Date"].iloc[0]
    last_date = df["Date"].iloc[-1]
    format_string = "%Y-%m-%d"
    
    given_date_object = dt.strptime(start_date, format_string)
    first_date_object = dt.strptime(first_date, format_string)
    last_date_object = dt.strptime(last_date, format_string)

    if (given_date_object < first_date_object or given_date_object > last_date_object):
        error_messages.append("Date is outside valid range")
    if (initial_contribution is not None and initial_contribution < 0):
        error_messages.append("Initial Contribution is negative")
    if (recurring_contribution is not None and recurring_contribution < 0):
        error_messages.append("Recurring Contribution is negative")
    if (start_amount is not None and start_amount < 0):
        error_messages.append("Start Amount is negative")
    
    return {
        "valid": len(error_messages) == 0,
        "errors": error_messages
    }