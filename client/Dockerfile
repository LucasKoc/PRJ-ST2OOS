FROM node:23.0 AS build

# Working directory
WORKDIR /app

# Copy the package.json file
COPY package.json .

# Install the dependencies
RUN npm install

# Copy the source code
COPY . .

# Build the application
RUN npm run build

FROM nginx:stable AS production
LABEL authors="lucas"

# Copy the build files to the working directory
COPY --from=build /app/build /usr/share/nginx/html

# Expose port - APP Port
EXPOSE 80

# Set the entrypoint to use nginx
CMD ["nginx", "-g", "daemon off;"]