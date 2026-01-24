

# Dollar-cost averaging (DCA) simulator - monthly investments over time
# Get available date range - so users know valid dates
# Input validation - handle invalid dates, negative amounts, dates outside your data range
# Error handling - return proper error messages when things go wrong

from fastapi import FastAPI

app = FastAPI()

import pandas as pd
df = pd.read_csv("data/sp500_aligned.csv")

@app.get("/")
async def root():
	return {"message": "Hello World"}


# Lump sum calculator with growth data (what you're building now)
@app.post("/calculate_lumpsum")
def calculate_lumpsum(start_date:str, start_amount:float):

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

@app.post("/calcualte_growth_lumpsum")
def calculate_growth_lumpsum(start_date:str, start_amount:float):
	# Use formula New_Balance:  
	# 	Current_Balance x (New_Price/Old_Price)
	# store the growth of the lumpsum deposit

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

		
		 




