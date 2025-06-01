# Straddle/Strangle Options Analyzer

## Goal
This repository loads stock data to analyze how often a stock moves by a given percentage, affecting straddle/strangle options positions.

## Example Data
This repository uses Apple stock's historical data as an example.

## ⚠ WARNING ⚠
### Stocks can exhibit irrational behavior, and past data **DOES NOT** guarantee future results. Please use caution.  
Models are created only to help **get a clue** about potential future outcomes, but nothing is guaranteed.

## Usage
- Ensure you have a **CSV file** containing stock data with the following columns: **Open, High, Low, Close** (volume is ignored).
- Place the CSV file inside your **project directory**.
- Load the CSV file into a **dataframe** as shown in the Jupyter notebook.
- Enter:
  - The **current stock price**.
  - The **call option strike** price you plan to buy.
  - The **call option sale** strike price and their respective costs.
  - The **long put strike** price.
  - The **short put strike** price and their respective cost/credit.
- **num_days**: This parameter defines how many days into the future the program should analyze.  
  - Example: If the options you are analyzing **expire in 10 trading days** (excluding weekends & holidays), set `num_days=10`.
