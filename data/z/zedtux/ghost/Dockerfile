#  
# Ghost Dockerfile  
#  
# https://github.com/dockerfile/ghost  
#  
# Pull base image.  
FROM node:6.9.4-slim  
MAINTAINER Guillaume Hain, zedtux@zedroot.org  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV GHOST_VERSION 0.11.11  
# Install Ghost  
RUN \  
apt-get update && \  
apt-get install -y unzip wget patch && \  
cd /tmp && \  
wget -q
https://github.com/TryGhost/Ghost/releases/download/${GHOST_VERSION}/Ghost-${GHOST_VERSION}.zip
-O ghost.zip && \  
unzip -q ghost.zip -d /ghost && \  
rm -f ghost.zip && \  
cd /ghost && \  
npm install --production && \  
sed 's/127.0.0.1/0.0.0.0/' /ghost/config.example.js > /ghost/config.js && \  
useradd ghost --home /ghost  
  
# Add files.  
COPY start.bash /ghost-start  
  
# Set environment variables.  
ENV NODE_ENV production  
  
# Define mountable directories.  
VOLUME ["/data", "/ghost-override"]  
  
# Define working directory.  
WORKDIR /ghost  
  
# ~~~~ Patches ~~~~~  
RUN mkdir /ghost/patches/  
  
# Add Google Analytics script  
COPY patches/google_analytics.patch /ghost/patches/google_analytics.patch  
RUN patch -p0 -u < patches/google_analytics.patch  
  
# Define default command.  
CMD ["bash", "/ghost-start"]  
  
# Expose ports.  
EXPOSE 2368  

