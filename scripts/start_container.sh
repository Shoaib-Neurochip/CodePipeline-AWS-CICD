#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
docker pull neurosba/simple-python-flask-app

# Run the Docker image as a container
docker run -d -p 8000:5000 neurosba/simple-python-flask-app

