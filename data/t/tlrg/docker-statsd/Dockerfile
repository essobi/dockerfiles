FROM node:4.2  
EXPOSE 8125/udp  
  
RUN git clone git://github.com/etsy/statsd.git /opt/statsd  
  
ADD ./statsdConfig.js /opt/statsd/config.js  
  
ENTRYPOINT ["node", "/opt/statsd/stats", "/opt/statsd/config.js"]  

