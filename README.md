# Sample Dashboard

A simple interactive dashboard built with **Dash** and **Plotly**, displaying a sample line chart.

## Overview

This project demonstrates how to create a basic web dashboard using the Dash framework. The application displays a line chart with sample data and serves it through a local web server.

## Features

* Simple Dash application structure
* Interactive line chart visualization
* Automatic browser updates when running in debug mode
* Easy to customize and extend

## Technologies Used

* Python 3.x
* Dash
* Plotly

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-folder>
```

2. Install the required dependencies:

```bash
pip install dash
```

## Running the Application

Start the dashboard by running:

```bash
python app.py
```

The application will be available at:

```text
http://127.0.0.1:8050/
```

## Project Structure

```text
project/
│
├── app.py
└── README.md
```

## Dashboard Components

### Header

The dashboard includes a main title:

```python
html.H1(children='Sample Dashboard')
```

### Graph

A line chart is displayed using Dash's `dcc.Graph` component.

Sample data:

| X | Y  |
| - | -- |
| 1 | 10 |
| 2 | 15 |
| 3 | 13 |
| 4 | 17 |

## Customization

You can modify:

* Chart type (`line`, `bar`, `scatter`, etc.)
* Data points
* Chart title
* Dashboard layout and styling

Example:

```python
'layout': {
    'title': 'Custom Chart Title'
}
```

## Development Mode

The application runs with:

```python
app.run_server(debug=True)
```

Debug mode enables:

* Automatic code reloading
* Error reporting
* Faster development workflow

## License

This project is provided for educational and demonstration purposes.
