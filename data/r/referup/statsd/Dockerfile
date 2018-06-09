FROM node:6-wheezy  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y --no-install-recommends curl \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /usr/src/app  
  
RUN \  
npm install git://github.com/markkimsal/statsd-elasticsearch-backend.git  
  
ADD config.js config.js  
ADD statsd .  
  
CMD [ "node", "stats.js", "./config.js" ]  

