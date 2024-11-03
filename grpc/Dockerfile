# Use an official Python runtime as a base image
FROM python:3.12-slim

# Set environment variables for MongoDB
ENV GRPC_MONGODB_USER=${GRPC_MONGODB_USER}
ENV GRPC_MONGODB_PASSWORD=${GRPC_MONGODB_PASSWORD}
ENV GRPC_MONGODB_DATABASE=${GRPC_MONGODB_DATABASE}
ENV GRPC_MONGODB_HOST=${GRPC_MONGODB_CONTAINER_NAME}
ENV GRPC_MONGODB_PORT=${GRPC_MONGODB_PORT}

# Copy source code
WORKDIR /app
COPY . /app

# Create a virtual environment
RUN python -m venv /app/venv

# Upgrade pip and install dependencies via requirements.txt file
RUN /app/venv/bin/pip install --upgrade pip && \
    /app/venv/bin/pip install -r requirements.txt

RUN /app/venv/bin/python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. school.proto

# Expose the gRPC server port
EXPOSE 50051

# Run the gRPC server
CMD ["/app/venv/bin/python", "grpc_server.py"]
