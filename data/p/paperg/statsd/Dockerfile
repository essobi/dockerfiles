# Dockerfile for statsd  
FROM dockerfile/nodejs  
MAINTAINER Kyle Tilman <kyle.tilman@paperg.com>  
  
RUN git clone https://github.com/etsy/statsd.git /statsd  
  
ADD config.js /statsd/  
  
EXPOSE 8125  
EXPOSE 8125/udp  
EXPOSE 8126/tcp  
  
# CMD sleep 1000  
CMD /usr/local/bin/node /statsd/stats.js /statsd/config.js  

