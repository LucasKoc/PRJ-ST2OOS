# Description: Dockerfile for the database image
FROM mongo:8

# Environment variables
ENV GRPC_MONGODB_CONTAINER_NAME=${GRPC_MONGODB_CONTAINER_NAME}
ENV GRPC_MONGODB_USER=${GRPC_MONGODB_USER}
ENV GRPC_MONGODB_PASSWORD=${GRPC_MONGODB_PASSWORD}
ENV GRPC_MONGODB_DATABASE=${GRPC_MONGODB_DATABASE}
ENV GRPC_MONGODB_HOST=${GRPC_MONGODB_HOST}
ENV GRPC_MONGODB_PORT=${GRPC_MONGODB_PORT}
ENV MONGO_INITDB_ROOT_USERNAME=${MONGO_INITDB_ROOT_USERNAME}
ENV MONGO_INITDB_ROOT_PASSWORD=${MONGO_INITDB_ROOT_PASSWORD}

# Copy the database initialization script
COPY mongo-init.js /docker-entrypoint-initdb.d/

# Expose the port
EXPOSE 27017

# Start the database
CMD ["mongod"]