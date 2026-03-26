FROM python:3.10-slim

# Work directory
WORKDIR /app

# Requirements copy
COPY requirements.txt .

# Dependencies install
RUN pip install --no-cache-dir -r requirements.txt

# Project copy
COPY . .

# Port
EXPOSE 8000

# Run server
CMD ["python", "weather_site/manage.py", "runserver", "0.0.0.0:8000"]