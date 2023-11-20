# iRoute

This system provides a versatile application that combines a route planner, an interactive map of bus stops, and an active implementation of real-time information about BiciMAD stations.

## System Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/estergsancho/iroute.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your_project
    ```

3. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    # or
    .\venv\Scripts\activate  # Windows
    ```

4. Install project requirements:

    ```bash
    pip install -r requirements.txt
    ```

## Key Features

### 1. Route Planner

- Enter starting and destination points to receive detailed route instructions.
- Utilizes the Nominatim geocoding service to convert addresses into coordinates.

### 2. Interactive Map of Bus Stops

- Displays an interactive map with bus stops.
- Allows users to add, remove, and obtain detailed information about stops.
- Uses Leaflet for map visualization.

### 3. Active BiciMAD Map

- Integrates real-time information about BiciMAD stations.
- Displays bike and free space availability at each station.
- Plans routes that include stops at BiciMAD stations.

## Usage

1. Activate your virtual environment:

    ```bash
    source venv/bin/activate  # Linux/Mac
    # or
    .\venv\Scripts\activate  # Windows
    ```

2. Run the Django application:

    ```bash
    python manage.py runserver
    ```

3. Access the application in your browser: [http://localhost:8000](http://localhost:8000)

Enjoy the functionalities provided by this Django project!
