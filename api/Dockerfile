FROM python:3.12-slim

# Working directory
WORKDIR /app

# Copy backend files into container
COPY . /app

# Create a virtual environment
RUN python -m venv /app/venv

# Upgrade pip and install dependencies via requirements.txt file
RUN /app/venv/bin/pip install --upgrade pip && \
    /app/venv/bin/pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 3000

# Entry point for the container
CMD ["/app/venv/bin/python", "-m", "api.main"]
