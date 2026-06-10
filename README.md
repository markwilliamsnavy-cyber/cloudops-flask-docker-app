# CloudOps Flask Docker App

## Project Overview

This project is a Dockerized Python Flask application built to demonstrate containerization, application health checks, environment variables, and local container testing.

The goal of this project was to build a small cloud-ready application that can run locally in Docker and later be deployed to AWS using services such as EC2 and Amazon ECR.

## Technologies Used

* Python
* Flask
* Docker
* Dockerfile
* Docker health checks
* Environment variables
* macOS Terminal
* GitHub

## Application Features

* Flask home page
* `/health` endpoint for health checks
* `/status` endpoint for application status
* Environment variable support
* Docker container health check
* Local port mapping from host to container
* Container logs for troubleshooting

## Project Structure

```text
cloudops-flask-docker-app/
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── README.md
└── screenshots/
    ├── home-page.png
    ├── health-endpoint.png
    ├── status-endpoint.png
    └── docker-healthy.png
```

## Screenshots

### Home Page

![Home Page](screenshots/home-page.png)

### Health Endpoint

![Health Endpoint](screenshots/health-endpoint.png)

### Status Endpoint

![Status Endpoint](screenshots/status-endpoint.png)

### Docker Health Check

![Docker Healthy](screenshots/docker-healthy.png)

## How to Run Locally Without Docker

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
PORT=5001 python app.py
```

Open the app in the browser:

```text
http://localhost:5001
```

Test the endpoints:

```text
http://localhost:5001/health
http://localhost:5001/status
```

## How to Build the Docker Image

Build the image:

```bash
docker build -t cloudops-flask-app .
```

## How to Run the Docker Container

Run the container:

```bash
docker run -d -p 5001:5000 --name cloudops-flask-app -e APP_NAME="CloudOps Flask App" -e ENVIRONMENT="docker-local" cloudops-flask-app
```

Open the app in the browser:

```text
http://localhost:5001
```

## Docker Commands Practiced

View running containers:

```bash
docker ps
```

View container logs:

```bash
docker logs cloudops-flask-app
```

Inspect the container:

```bash
docker inspect cloudops-flask-app
```

Stop and remove the container:

```bash
docker rm -f cloudops-flask-app
```

View local Docker images:

```bash
docker images
```

## Health Check

The Dockerfile includes a container health check that calls the `/health` endpoint:

```dockerfile
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" || exit 1
```

When the container is running correctly, `docker ps` shows the container status as:

```text
Up ... (healthy)
```

## Troubleshooting Notes

During testing, port `5000` was already in use locally, so the application was run on host port `5001`.

The Docker container maps host port `5001` to container port `5000`:

```text
localhost:5001 → container:5000
```

This helped validate port mapping and basic container troubleshooting.

## Skills Demonstrated

* Python Flask application development
* Docker image creation
* Dockerfile configuration
* Container deployment
* Port mapping
* Environment variable usage
* Docker health checks
* Container log review
* Local application troubleshooting
* GitHub documentation

## Next Steps

Future improvements for this project include:

* Push the Docker image to Amazon ECR
* Deploy the containerized application on AWS EC2
* Configure EC2 security groups for HTTP access
* Add CloudWatch monitoring and logging
* Document the AWS deployment process
