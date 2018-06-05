FROM ubuntu:trusty  
MAINTAINER Pablo Estrada <pjestradac@gmail.com>  
  
# Prevent Dpkg Errors  
ENV TERM=xterm-256color  
  
# Set mirrors to NZ  
RUN sed -i "s/http:\/\/archive./http:\/\/nz.archive./g" /etc/apt/sources.list  
  
# Install Node JS  
RUN apt-get update && \  
apt-get install curl -y && \  
curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash - && \  
apt-get install -y nodejs  
  
COPY . /app  
WORKDIR /app  
  
RUN npm install -g mocha && \  
npm install  
  
RUN chmod +x /  
ENTRYPOINT ["mocha"]

