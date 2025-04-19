# Stage 1: Build the React application
FROM node:16 AS build
WORKDIR /app

# Copy package.json and package-lock.json (if present) for caching purposes
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application files and build the app
COPY . .
RUN npm run build

# Stage 2: Set up Nginx to serve the built application
FROM nginx:alpine

# Copy custom nginx config (if needed)
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy built application to Nginx’s public directory
COPY --from=build /app/build /usr/share/nginx/html

# Expose the port Nginx is listening on
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
