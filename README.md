# 🐳 Docker Challenge: Flask, Redis and Load Balancing using Nginx

## Overview
- Multi-container application using Docker Compose
- Includes:
  - Flask web service
  - Redis for storing visit counts
  - Nginx as a reverse proxy and load balancer

## Structure
- `app.py`: Flask app with `/` and `/count` routes
- `Dockerfile`: Builds the Flask container
- `docker-compose.yml`: Defines Flask, Redis, and Nginx services
- `requirements.txt`: Python dependencies
- `nginx.conf`: Nginx config for routing to multiple Flask instances

## Features
- Redis stores visit count data
- Environment variables used for Redis host configuration
- Nginx balances load across multiple Flask containers
- Docker volume for Redis data persistence

## Usage
- Start app: `docker compose up --build`
- Scale Flask: `docker compose up --scale web=3 --build`
- Access app: `http://localhost:5002` and `http://localhost:5002/count`
