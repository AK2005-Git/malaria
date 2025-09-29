# Use official Python 3.9 image as base
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements file to container
COPY requirements.txt .

# Install dependencies and upgrade pip and setuptools
RUN pip install --upgrade pip setuptools wheel setuptools_scm

# Install all python packages from requirements
RUN pip install -r requirements.txt

# Copy rest of the app code
COPY . .

# Expose the port your Flask app runs on
EXPOSE 8080

# Command to run your Flask app
CMD ["python", "app.py"]
