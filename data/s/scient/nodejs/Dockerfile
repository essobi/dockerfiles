# Base image  
FROM debian:jessie  
  
# Maintainer  
MAINTAINER Ivo Krooswijk "ivo@krooswijk.com"  
# Install libraries  
RUN apt-get update && apt-get install -y \  
curl \  
python \  
make \  
nano \  
git-core \  
g++  
  
# Get the latest node.js and npm versions and install  
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash -  
RUN apt-get update && apt-get install -y \  
nodejs  
  
# Create web folder  
RUN mkdir -p /var/www/default \  
&& echo "console.log('NodeJS base image running...');" >>
/var/www/default/app.js  
  
# Volumes  
VOLUME ["/var/www/default"]  
  
# Expose ports  
#EXPOSE 5000  
# Run command  
CMD ["node", "/var/www/default/app.js"]  

