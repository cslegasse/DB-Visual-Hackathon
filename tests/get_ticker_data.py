import requests
import json

def test_api():
    # Test with default ticker (AAPL)
    response = requests.get('http://localhost:5000/api/data')
    assert response.status_code == 200
    data = response.json()
    assert data['ticker'] == 'AAPL'
    assert 'shortName' in data
    assert 'firstTradeDateEpochUtc' in data
    assert 'longBusinessSummary' in data
    
    # Test with a different ticker
    response = requests.get('http://localhost:5000/api/data?ticker=GOOGL')
    assert response.status_code == 200
    data = response.json()
    assert data['ticker'] == 'GOOGL'
    
    print("All tests passed!")

if __name__ == '__main__':
    test_api()