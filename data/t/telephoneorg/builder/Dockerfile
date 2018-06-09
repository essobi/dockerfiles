FROM debian:stretch  
  
MAINTAINER Joe Black <me@joeblack.nyc>  
RUN apt-get update && \  
apt-get install -y build-essential curl && \  
curl -fsSL get.docker.com -o get-docker.sh && \  
sh get-docker.sh && \  
rm -f get-docker.sh && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  

