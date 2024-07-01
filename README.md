# Flask Weather Greeting App

This Flask application greets visitors based on their provided name (extracted from query parameters), retrieves their IP address, and fetches current weather information using the WeatherAPI.

## Features

- **Greeting Endpoint**: `/hello`
  - Greets visitors based on their provided name.
  - If no name is provided, a generic greeting is displayed.

- **Weather Information Endpoint**: `/hello`
  - Fetches the visitor's IP address using ipify API.
  - Retrieves current weather information based on the visitor's IP using WeatherAPI.

## Setup

### Prerequisites

- Python 3.x
- Flask
- Requests library
- WeatherAPI API key

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo

2. Install dependencies

    ```pip install -r requirements.txt```


