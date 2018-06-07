# Base image from Ruby docker hub  
FROM debian:jessie  
  
MAINTAINER kwokhou  
  
# Install essential linux packages  
RUN apt-get update -qq && apt-get install -y libpq-dev nodejs npm  
  
# Define where the application will live inside the image  
ENV WEB_ROOT /var/www/app  
  
# Create application home. App server will need the pids dir  
RUN mkdir -p $WEB_ROOT/  
  
# Set our working directory inside the image  
WORKDIR $WEB_ROOT  
  
# Use the package.json as Docker cache markers. Always install before copying
app src.  
COPY package.json package.json  
  
# Restore npm packages  
RUN npm install --production  
  
# Copy the Rails application into place  
COPY . .  
  
# Define the script we want run once the container boots  
# Use the "exec" form of CMD so our script shuts down gracefully on SIGTERM
(i.e. `docker stop`)  
CMD [ "exec node app.js" ]  

