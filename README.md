# Currency Exchange Rate Converter

A robust Python application that provides real-time currency exchange rate conversion using the Open Exchange Rates API. This project demonstrates professional Python development practices including environment management, API integration, caching, and clean code architecture.

## Features

- Real-time currency exchange rate conversion
- Caching mechanism to optimize API calls (15-minute TTL)
- Environment-based configuration
- Clean separation of concerns with modular code structure
- Support for any currency pair conversion

## Prerequisites

- Python 3.7+
- pipenv (for dependency management)

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd <project-directory>
```

2. Install dependencies using pipenv:

```bash
pipenv install
```

3. Create a `.env` file in the root directory with the following variables:

```env
EXCHANGE_API_KEY=your_api_key_here
BASE_URL=https://openexchangerates.org/api/latest.json
```

## Project Structure

```
.
├── app.py              # Main application entry point
├── libs/
│   └── openexchange.py # OpenExchange API client implementation
├── Pipfile            # Python dependencies
├── Pipfile.lock       # Locked dependencies
└── .env               # Environment variables (not tracked in git)
```

## Usage

The application provides a simple interface to convert currencies. Here's a basic example:

```python
from libs.openexchange import OpenExchangeClient

# Initialize the client
client = OpenExchangeClient(app_id="your_api_key")

# Convert USD to GBP
usd_amount = 1000
gbp_amount = client.converter(usd_amount, "USD", "GBP")
print(f'USD{usd_amount} is GBP{gbp_amount:.2f}')
```

## Technical Details

### OpenExchangeClient

The `OpenExchangeClient` class provides the following features:

- **Caching**: Implements a TTL cache (15 minutes) to reduce API calls
- **Rate Conversion**: Supports conversion between any currency pair
- **Error Handling**: Built-in error handling for API responses
- **Environment Configuration**: Secure configuration management

### Dependencies

- `requests`: HTTP client for API calls
- `python-dotenv`: Environment variable management
- `cachetools`: Caching implementation

## Best Practices Implemented

1. **Environment Management**

   - Secure API key storage
   - Configuration through environment variables

2. **Code Organization**

   - Modular design
   - Separation of concerns
   - Clean code principles

3. **Performance Optimization**

   - Caching mechanism
   - Efficient API usage

4. **Security**
   - API key protection
   - Environment-based configuration

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Open Exchange Rates API for providing the exchange rate data
- Python community for the excellent libraries used in this project
