# Use an official Python runtime as a base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the local files to the container at /app
COPY . /app

# Install Flask and pymongo (and any other dependencies) using pip
# RUN pip install flask pymongo pytest pytest-flask

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Run tests
# RUN pytest testapp.py

# Expose the port "2101"
EXPOSE 2101

# Define the command to run when the container starts
CMD ["python", "main.py"]
