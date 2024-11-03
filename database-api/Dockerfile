# Description: Dockerfile for the database image
FROM postgres:17.0

# Set the environment variables
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_DB=${POSTGRES_DB}
ENV POSTGRES_SCHEMA=${POSTGRES_SCHEMA}

ENV POSTGRES_HOST=${POSTGRES_HOST}
ENV POSTGRES_PORT=${POSTGRES_PORT}

# Copy the database schema
COPY ./schema.sql /docker-entrypoint-initdb.d/schema.sql

# Expose the port
EXPOSE 5432

# Start the database
CMD ["postgres"]
