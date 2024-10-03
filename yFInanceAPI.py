#Here is where you can test the company ticker and see the relevant data. 
import yfinance as yf

# Prompt the user for the ticker symbol
ticker_symbol = input("Enter the ticker symbol (e.g., AAPL for Apple): ")

# Initialize the ticker
ticker = yf.Ticker(ticker_symbol)

# Retrieve quarterly financials (Income Statement and Cash Flow)
quarterly_financials = ticker.quarterly_financials
quarterly_cashflow = ticker.quarterly_cashflow
balance_sheet = ticker.quarterly_balance_sheet

# Get company name, IPO date, and mission statement
company_name = ticker.info.get('longName', 'N/A')  # Default to 'N/A' if not found
ipo_date = ticker.info.get('ipoDate', 'N/A')  # Default to 'N/A' if not found
mission_statement = ticker.info.get('longBusinessSummary', 'N/A')  # Default to 'N/A' if not found

# Get the number of shares outstanding
shares_outstanding = ticker.info.get('sharesOutstanding', 0)  # Default to 0 if not found

# Extract relevant data for the calculations
# Revenue and Net Income
revenue = quarterly_financials.loc['Total Revenue'] if 'Total Revenue' in quarterly_financials.index else 0
net_income = quarterly_financials.loc['Net Income'] if 'Net Income' in quarterly_financials.index else 0
free_cash_flow = quarterly_cashflow.loc['Free Cash Flow'] if 'Free Cash Flow' in quarterly_cashflow.index else 0

# Handle missing values for 'Goodwill', 'Other Intangible Assets', and 'Total Liab'
goodwill = balance_sheet.loc['Goodwill'] if 'Goodwill' in balance_sheet.index else 0
other_intangible_assets = balance_sheet.loc['Other Intangible Assets'] if 'Other Intangible Assets' in balance_sheet.index else 0
total_assets = balance_sheet.loc['Total Assets'] if 'Total Assets' in balance_sheet.index else 0

# Check for 'Total Liab'
total_liabilities = balance_sheet.loc['Total Liabilities Net Minority Interest'] if 'Total Liabilities Net Minority Interest' in balance_sheet.index else \
                    balance_sheet.loc['Total Liabilities Net Minority Interests'] if 'Total Liabilities Net Minority Interests' in balance_sheet.index else \
                    balance_sheet.loc['Total Liabilities'] if 'Total Liabilities' in balance_sheet.index else 0

# Calculate Tangible Book Value
tangible_book_value = total_assets - goodwill - other_intangible_assets - total_liabilities

# Calculate per share metrics
revenue_per_share = revenue / shares_outstanding if shares_outstanding > 0 else 0
net_income_per_share = net_income / shares_outstanding if shares_outstanding > 0 else 0
free_cash_flow_per_share = free_cash_flow / shares_outstanding if shares_outstanding > 0 else 0
tangible_book_value_per_share = tangible_book_value / shares_outstanding if shares_outstanding > 0 else 0

 
# Display the calculated per share values
print(f"\nFinancial Data for {company_name}({ticker_symbol}):")
print(f"IPO Date: {ipo_date}/n")
print(f"Mission Statement: {mission_statement}/n")
print("Quarterly Financial Metrics")
print("Revenue Per Share:")
print(revenue_per_share)

print("\nNet Income Per Share:")
print(net_income_per_share)

print("\nFree Cash Flow Per Share:")
print(free_cash_flow_per_share)

print("\nTangible Book Value Per Share:")
print(tangible_book_value_per_share)
