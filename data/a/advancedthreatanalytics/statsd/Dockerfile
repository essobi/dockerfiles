FROM node:0.10  
  
RUN apt-get -y update && apt-get -y install libavahi-compat-libdnssd-dev  
RUN export USER=root; export npm_config_spin=false && \  
npm install -g statsd@0.8.0 && \  
cd /usr/local/lib/node_modules/statsd && \  
npm install git://github.com/markkimsal/statsd-elasticsearch-backend.git && \  
npm install lodash  
  
COPY formatter.js /usr/local/lib/node_modules/statsd/node_modules/statsd-
elasticsearch-backend/lib/custom_format.js  
COPY config.js /opt/statsd/config.js  
  
EXPOSE 8125/udp  
EXPOSE 8126  
ADD start.sh /opt/start.sh  
ENTRYPOINT ["/opt/start.sh"]  

