# Use a slim base image for smaller size and improved security
FROM python:3.9.1-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Set environment variables to optimize Python runtime
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies required for Python packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential libssl-dev libffi-dev libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install Python dependencies
COPY requirements.txt /usr/src/app/
RUN pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache/pip

# Copy the project files into the container
COPY . /usr/src/app/