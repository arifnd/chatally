FROM python:3.9-slim-buster

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set environment variables
ENV PORT=5000
ENV WORKERS=2
ENV TIMEOUT=60

# Start the application with Gunicorn
CMD exec gunicorn --bind :$PORT --workers $WORKERS --timeout $TIMEOUT app:app
