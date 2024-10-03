import unittest
from src.utils import validate_ticker, fetch_financial_data
from src.API_Data_for_ticker import get_ticker_data

class TestAPIFunctionality(unittest.TestCase):

    def test_valid_nyse_tickers(self):
        valid_tickers = ['AAPL', 'MSFT', 'JPM', 'GE', 'XOM']
        for ticker in valid_tickers:
            with self.subTest(ticker=ticker):
                self.assertTrue(validate_ticker(ticker))
                data = get_ticker_data(ticker)
                self.assertIsNotNone(data)
                self.assertIn('revenue_per_share', data)
                self.assertIn('net_income_per_share', data)
                self.assertIn('free_cash_flow_per_share', data)
                self.assertIn('tangible_book_value_per_share', data)

    def test_invalid_tickers(self):
        invalid_tickers = ['INVALID', 'NOT_A_TICKER', '123', 'TEST']
        for ticker in invalid_tickers:
            with self.subTest(ticker=ticker):
                self.assertFalse(validate_ticker(ticker))
                with self.assertRaises(Exception):
                    get_ticker_data(ticker)

    def test_edge_cases(self):
        edge_cases = ['', ' ', 'A', 'AA', 'AAAA', 'aapl', 'msft']
        for ticker in edge_cases:
            with self.subTest(ticker=ticker):
                if validate_ticker(ticker):
                    data = get_ticker_data(ticker)
                    self.assertIsNotNone(data)
                else:
                    with self.assertRaises(Exception):
                        get_ticker_data(ticker)

    def test_data_consistency(self):
        ticker = 'AAPL'
        data1 = get_ticker_data(ticker)
        data2 = get_ticker_data(ticker)
        self.assertEqual(data1, data2, "Data should be consistent for the same ticker")

if __name__ == '__main__':
    unittest.main()