# Base image — Python 3.11 (slim = lightweight version)
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script into the container
COPY sim.py .

# Create the figures folder inside the container
RUN mkdir -p figures

# Run the script when the container starts
CMD ["python", "sim.py"]
