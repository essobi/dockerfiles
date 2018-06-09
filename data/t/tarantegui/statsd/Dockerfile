FROM node  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y --no-install-recommends \  
curl \  
#git \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /usr/src/app  
  
RUN \  
npm install git://github.com/markkimsal/statsd-elasticsearch-backend.git  
  
RUN \  
git clone https://github.com/etsy/statsd.git  
  
ADD config.js statsd/config.js  
  
CMD [ "node", "statsd/stats.js", "statsd/config.js" ]  

