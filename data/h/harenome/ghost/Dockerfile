# Dockerfile for Ghost.  
# See https://www.ghost.org  
# DOCKER-VERSION 1.2.0  
# Start from official Node image, v0.10.31  
FROM node:0.10.31  
# Install wget and unzip to download and extract ghost.  
RUN apt-get update && apt-get install -y wget unzip  
  
# Download and unpack Ghost v0.5.1, perform installation steps.  
RUN wget https://ghost.org/zip/ghost-0.5.0.zip -O /tmp/ghost.zip \  
&& unzip /tmp/ghost.zip -d /opt/ghost \  
&& rm /tmp/ghost.zip \  
&& cd /opt/ghost \  
&& npm install --production \  
&& sed 's/127.0.0.1/0.0.0.0/' /opt/ghost/config.example.js >
/opt/ghost/config.js  
  
# Set the Workdir to the installation directory.  
WORKDIR /opt/ghost  
  
# Set environment variables.  
ENV NODE_ENV production  
ENV GHOST_VERSION 0.5.0  
# Expose default port.  
EXPOSE 2368  
# Add startup script and configure related options  
VOLUME [ "/data" ]  
ADD start /opt/ghost/start  
ENTRYPOINT [ "/opt/ghost/start" ]  

