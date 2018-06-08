FROM mhart/alpine-node  
  
RUN npm install -g statsd@0.7.2 --no-optional  
  
# Setup config  
COPY statsd-config.js /opt/statsd/config.js  
  
EXPOSE 8125/udp  
  
CMD statsd /opt/statsd/config.js  

