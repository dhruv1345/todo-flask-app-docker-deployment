# Use Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install flask pymongo

# Expose the port Flask runs on
EXPOSE 5000

# Start the Flask application
CMD ["python", "app.py"]

