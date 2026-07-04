# Game Deals Finder

A simple Flask web app that fetches live game deals from the [CheapShark API](https://www.cheapshark.com/api) and lets users search and filter them by title and price range.

## Features

- Fetches real-time deals from CheapShark
- Search games by title
- Filter results by minimum and maximum sale price
- Renders results using a Flask/Jinja2 template

## Requirements

- Python 3.7+
- Flask
- Requests

## Installation

1. Clone or download this repository.
2. (Optional but recommended) create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install flask requests
   ```

## Usage

1. Run the app:
   ```bash
   python app.py
   ```
2. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```
3. Use the query parameters to search and filter deals, for example:
   ```
   http://127.0.0.1:5000/?search=zelda&min_price=5&max_price=20
   ```

## Project Structure

```
.
├── app.py              # Main Flask application
├── templates/
│   └── index.html      # Template rendering the games list
└── README.md
```

## How It Works

- The `/` route accepts optional query parameters: `search`, `min_price`, and `max_price`.
- It calls the CheapShark `/deals` endpoint to get the current list of deals.
- Results are filtered in Python based on the provided query parameters before being passed to the template.

## Possible Improvements

- Add pagination, since CheapShark returns a large list of deals per request
- Add error handling for the external API call (e.g., timeouts, non-200 responses)
- Validate `min_price`/`max_price` inputs to avoid crashes on non-numeric values
- Add sorting options (price, discount percentage, etc.)
- Cache API responses to reduce repeated calls to CheapShark

## License

This project is open source and available for personal or educational use.
