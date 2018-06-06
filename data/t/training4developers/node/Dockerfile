from ubuntu:latest  
  
MAINTAINER Eric Greene <eric@training4developers.com>  
  
ENV NODE_VERSION 4.4.0  
ENV NODE_ARCHIVE node-v$NODE_VERSION-linux-x64.tar.xz  
  
# Update & Install Ubuntu Packages  
RUN apt-get update && apt-get install -y \  
curl \  
xz-utils  
  
# Download Binary Node.js Files  
RUN mkdir /opt/downloads; mkdir /opt/app  
RUN curl -o /opt/downloads/$NODE_ARCHIVE \  
https://nodejs.org/dist/v$NODE_VERSION/$NODE_ARCHIVE  
  
# Extract and Install Node.js Files  
RUN tar -C /usr/local \--strip-components 1 -xf /opt/downloads/$NODE_ARCHIVE  
  
EXPOSE 3000  

