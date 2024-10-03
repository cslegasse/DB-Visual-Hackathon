import yfinance as yf

# Initialize the ticker for Apple (AAPL)
ticker = yf.Ticker("AAPL")

# Retrieve quarterly financials (Income Statement and Cash Flow)
quarterly_financials = ticker.quarterly_financials
quarterly_cashflow = ticker.quarterly_cashflow
balance_sheet = ticker.quarterly_balance_sheet

# Get the number of shares outstanding
shares_outstanding = ticker.info['sharesOutstanding']

# Extract relevant data for the calculations
# Revenue and Net Income
revenue = quarterly_financials.loc['Total Revenue']
net_income = quarterly_financials.loc['Net Income']
free_cash_flow = quarterly_cashflow.loc['Free Cash Flow']

# Handle missing values for 'Goodwill', 'Other Intangible Assets', and 'Total Liab'
goodwill = balance_sheet.loc['Goodwill'] if 'Goodwill' in balance_sheet.index else 0
other_intangible_assets = balance_sheet.loc['Other Intangible Assets'] if 'Other Intangible Assets' in balance_sheet.index else 0
total_assets = balance_sheet.loc['Total Assets']

# Check for 'Total Liab'
total_liabilities = balance_sheet.loc['Total Liabilities Net Minority Interest'] if 'Total Liabilities Net Minority Interest' in balance_sheet.index else \
                    balance_sheet.loc['Total Liabilities Net Minority Interests'] if 'Total Liabilities Net Minority Interests' in balance_sheet.index else \
                    balance_sheet.loc['Total Liabilities'] if 'Total Liabilities' in balance_sheet.index else 0

# Calculate Tangible Book Value
tangible_book_value = total_assets - goodwill - other_intangible_assets - total_liabilities

# Calculate per share metrics
revenue_per_share = revenue / shares_outstanding
net_income_per_share = net_income / shares_outstanding
free_cash_flow_per_share = free_cash_flow / shares_outstanding
tangible_book_value_per_share = tangible_book_value / shares_outstanding

# Display the calculated per share values
print("Revenue Per Share (Quarterly):")
print(revenue_per_share)

print("\nNet Income Per Share (Quarterly):")
print(net_income_per_share)

print("\nFree Cash Flow Per Share (Quarterly):")
print(free_cash_flow_per_share)

print("\nTangible Book Value Per Share (Quarterly):")
print(tangible_book_value_per_share)
