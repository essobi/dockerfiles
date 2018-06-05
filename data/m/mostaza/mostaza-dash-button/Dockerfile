FROM node:7  
RUN set -ex; \  
apt-get update; \  
apt-get install -y --no-install-recommends \  
libpcap-dev \  
sudo  
  
RUN mkdir -p /app  
COPY . /app  
WORKDIR /app  
RUN npm install  
  
CMD [ "npm", "run", "start" ]  

