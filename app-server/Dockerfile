# app-server/Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install required packages
RUN pip install --no-cache-dir schedule

# Copy log generation script
COPY log_generator.py .

# Run the log generator
CMD ["python", "log_generator.py"]
