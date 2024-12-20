# Use Python 3.10 base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    APP_HOME=/app

# Set the working directory
WORKDIR $APP_HOME

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements file
COPY requirements.txt .
COPY data/ /app/data/
COPY users.json /app/


# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8080

# Command to run the application
CMD ["python", "app.py"]

