FROM python:3.10-slim

# Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code + model
COPY . .

# Expose container port
EXPOSE 5000

# Run using Gunicorn (production server)
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]
