FROM node:5.10-slim  
MAINTAINER mateuszmoneta@gmail.com  
  
RUN wget https://github.com/etsy/statsd/archive/master.tar.gz && \  
npm install --no-optional master.tar.gz && \  
npm cache clear && \  
rm master.tar.gz  
  
COPY config.js /etc/statsd.js  
ONBUILD COPY config.js /etc/statsd.js  
  
EXPOSE 8125/udp  
  
CMD ["/node_modules/statsd/bin/statsd", "/etc/statsd.js"]  

