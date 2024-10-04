# DB-Visual-Hackathon

## Overview - Solution to Prompt 2

This project is a visualization tool for key financial metrics of publicly traded companies, developed as part of the DB-Visual-Hackathon. It uses Streamlit for the frontend, Flask for the backend API, and the yfinance library to fetch financial data.

## Tools Used

- Streamlit
- Python
- Flask
- yfinance API
- Plotly

## Key Features

When a user inputs a company ticker, the application retrieves and displays the following key metrics:

1. Company's name
2. Company's mission statement (if available)
3. Qualitative description of what the company does
4. Revenue Per Share
5. Net Income Per Share
6. Free Cash Flow Per Share
7. Tangible Book Value Per Share

## Project Structure

The project is structured as follows:

- `src/`: Contains the main application code
  - `streamlit_app.py`: Streamlit frontend application
  - `app.py`: Flask backend API
  - `utils.py`: Utility functions for data processing
- `tests/`: Contains test files
- `docs/`: Contains documentation files
- `assets/`: Contains static assets like images and CSS

## Setup and Installation

1. Clone the repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask backend:
   ```bash
   python src/app.py
   ```
4. In a separate terminal, run the Streamlit frontend:
   ```bash
   streamlit run src/streamlit_app.py
   ```

## Usage

1. Open the Streamlit app in your browser (usually at `http://localhost:8501`)
2. Enter a stock ticker symbol in the sidebar
3. View the financial metrics and visualizations

## Testing

Run the tests using pytest:
```bash
pytest tests/
```

## Future Additions

1. SQL backend for data persistence to avoid submitting repeated requests for the same ticker
2. Features for analysts to copy metrics to update their models
3. Enhanced error handling and input validation
4. More comprehensive financial metrics and visualizations

## CI/CD Pipeline

We use tried to set up GitHub Actions for our CI/CD pipeline. Ultimately we began using branches to clean up our additions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.