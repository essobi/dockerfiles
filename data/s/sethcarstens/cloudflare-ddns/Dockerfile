FROM node:5.8.0-wheezy  
MAINTAINER Seth Carstens <seth.carstens@gmail.com>  
  
# set terminal environment  
ENV TERM=xterm  
  
# Install DNS utilities for public IP lookup  
RUN apt-get update  
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y dnsutils  
RUN npm install -g cloudflare-cli  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#Test IP resolver  
RUN dig +short myip.opendns.com @resolver1.opendns.com ;  
  
# Copy application files to container  
ADD app/ /app  
RUN chmod -R 775 /app  
  
# Run default container shell script  
COPY /docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
ENTRYPOINT ["/bin/bash", "-c", "/docker-entrypoint.sh"]

