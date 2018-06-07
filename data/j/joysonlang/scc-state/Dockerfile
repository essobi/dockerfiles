FROM node:6.11.0-slim  
MAINTAINER Joyson Dsouza  
  
LABEL version="1.2.0"  
LABEL description="Docker file for Lemoney State Server"  
  
# Install PM2  
RUN npm install -g pm2  
  
RUN mkdir -p /usr/src/  
WORKDIR /usr/src/  
COPY . /usr/src/  
  
RUN npm install .  
  
EXPOSE 7777  
CMD pm2 start --no-daemon processes.json  

