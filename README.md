# Weather Backend

A simple containerized Weather API backend built using Python and Flask.

## Application Details

- Language: Python
- Framework: Flask
- Containerization: Docker
- Application Port: 5000
- Container Name: weather-backend
- ECR Repository: weather-backend
- ECS Cluster: weather-cluster
- ECS Task Definition: weather-task
- ECS Service: weather-service
- ECS Launch Type: Fargate

## API Endpoints

### Home

GET /

Response:

Weather API Server is running

### Health Check

GET /health

Example response:

{
    "status": "healthy",
    "service": "weather-backend"
}

### Weather

GET /weather

Example response:

{
    "city": "Bengaluru",
    "temperature": "28°C",
    "condition": "Partly Cloudy",
    "humidity": "65%",
    "wind_speed": "12 km/h"
}

## Run Locally

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

The application will run on:

http://localhost:5000

## Run Using Docker

Build the Docker image:

docker build -t weather-backend:latest .

Run the container:

docker run -d --name weather-backend -p 5000:5000 weather-backend:latest

Test the application:

curl http://localhost:5000

Expected response:

Weather API Server is running
