# Housing Data Analysis App

### Overview

The Housing Data Analysis App is a data visualization tool built using Streamlit, a Python library for creating interactive web applications. This app allows users to explore and analyze housing data from a CSV file, providing various statistics and visualizations to gain insights into housing trends.

### Features

Data Visualization: Display various statistics and graphs based on the provided housing dataset.
Interactive Interface: User-friendly interface with interactive controls for exploring the data.
Prometheus Integration: Tracks button clicks using Prometheus client library to monitor user interactions.
Docker Support: Dockerfile included for easy deployment as a Docker container.

### Requirements

- Python 3.9 or higher
- Docker (optional, for containerized deployment)

### Installation

To run the Housing Data Analysis App locally, follow these steps:

1. Clone the repository to your local machine:

``` bash
Copy code
git clone <repository-url>
```

2. Navigate to the project directory:

```bash
Copy code
cd housing-data-analysis-ap
``` 

3. Install dependencies using Poetry:

```bash
Copy code
poetry install
```

### Usage

To start the app, run the following command:

```bash
Copy code
poetry run streamlit run app.py
This will launch the Streamlit app in your default web browser. You can then interact with the app to explore the housing data and view various statistics and visualizations.
```

### Docker Deployment

Alternatively, you can deploy the app as a Docker container. First, build the Docker image:

```bash
Copy code
docker build -t housing-data-app .
```

Then, run the Docker container:

```bash
Copy code
docker run -p 8501:8501 housing-data-app
```

The app will be accessible at http://localhost:8501 in your web browser.

### Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.