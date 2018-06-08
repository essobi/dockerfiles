# Use ubuntu artful as parent image  
FROM ubuntu:artful  
# Set maintainer  
LABEL maintainer="Laurens Sion <laurens@sion.info>"  
  
# Set the working directory to /app  
WORKDIR /data  
VOLUME /data  
  
# Update and install texlive-full  
RUN apt-get update -q && \  
apt-get install -qy texlive-full make && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  

