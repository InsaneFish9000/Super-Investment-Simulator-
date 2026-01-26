




# Error handling - return proper error messages when things go wrong
from datetime import datetime as dt
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

import pandas as pd
df = pd.read_csv("data/sp500_aligned.csv")

@app.get("/")
async def root():
	return {"message": "Hello World"}


# Lump sum calculation without growth data 
@app.post("/calculate_lump_sum")
def calculate_lump_sum(
	start_date:str, 
	start_amount:float):

	# TODO: Load data from CSV - Loaded in memory once
	# TODO: Find price at start_date 
	init_price_row = df[df["Date"] == start_date]
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

# Lump sum calculation with growth data 
@app.post("/calculate_growth_lump_sum")
def calculate_growth_lump_sum(
	start_date:str, 
	start_amount:float):

	# Use formula New_Balance:  
	# 	Current_Balance x (New_Price/Old_Price)
	# store the growth of the lump_sum deposit

	idx = df.index[df["Date"] == start_date][0]
	current_balance = start_amount
	growth_overtime = []
	old_price = df["SP500_Close"].iloc[idx]

	for i in range(idx, len(df)):
		new_price = df["SP500_Close"].iloc[i]
		current_balance = current_balance * (new_price/old_price)
		growth_overtime.append(round(current_balance,2))
		old_price = new_price

	return {
		"growth_overtime": growth_overtime
	}

# Dollar-cost averaging (DCA) simulator - monthly investments over time
@app.post("/calculate_dca_growth")
def calculate_dca_growth(
	start_date:str, 
	initial_contribution:float, 
	recurring_contribution:float):

	# initial amount -> Growth -> Add contribution -> new_amount 
	#  |------------------------------------------------------|
	idx = df.index[df["Date"] == start_date][0]
	current_balance = initial_contribution
	growth_overtime = []
	old_price = df["SP500_Close"].iloc[idx]
	contribution = initial_contribution

	for i in range(idx, len(df)):
		new_price = df["SP500_Close"].iloc[i]
		current_balance = current_balance * (new_price/old_price)
		current_balance = current_balance + recurring_contribution
		contribution = contribution + recurring_contribution
		growth_overtime.append(round(current_balance, 2))
		old_price = new_price
	
	current_balance = round(current_balance,2)
	your_contribution = round(contribution, 2)
	total_interest_earned = round(current_balance - contribution,2)
	return {
		"growth_overtime": growth_overtime,
		"current_balance": current_balance,
		"your_contribution": your_contribution,
		"total_interest_earned": total_interest_earned
	}

# Get available date range - so users know valid dates
@app.get("/get_valid_date_range")
def get_valid_date_range():
	first_date = df["Date"].iloc[0]
	end_date = df["Date"].iloc[-1]

	return {
		"first_date": first_date,
		"end_date": end_date
	}

# Input validation - handle invalid dates, negative amounts, dates outside your data range
@app.post("/validate_inputs")
def validate_inputs(
	start_date:str, 
	initial_contribution: Optional[float] = None, 
	recurring_contribution: Optional[float] = None, 
	start_amount: Optional[float] = None):
	
	error_messages = []
	first_date = df["Date"].iloc[0]
	last_date = df["Date"].iloc[-1]
	format_string = "%Y-%m-%d"
	given_date_object = dt.strptime(start_date, format_string)
	first_date_object = dt.strptime(first_date, format_string)
	last_date_object = dt.strptime(last_date, format_string)

	if (given_date_object < first_date_object or given_date_object > last_date_object):
		error_messages.append("Date is outside valid range")
		
	if (initial_contribution != None and initial_contribution < 0 ):
		error_messages.append("Initial Contribution is negative")
	
	if(recurring_contribution != None and recurring_contribution < 0):
		error_messages.append("Recurring Contribution is negative")
	
	if(start_amount != None and start_amount < 0):
		error_messages.append("Start Amount is negative")
	
	if(error_messages == []):
		return {
		"valid": True,
		"errors": []
		}
	if(error_messages != []):
		return {
		"valid": False,
		"errors": error_messages
		}
	









		
		 




