FROM node:4.2  
EXPOSE 8125/udp  
  
RUN git clone https://github.com/etsy/statsd.git /opt/statsd \  
&& npm install https://github.com/markkimsal/statsd-elasticsearch-backend.git
\  
&& npm install statsd-elasticsearch-backend-tlrg-formatter  
  
ADD ./statsdConfig.js /opt/statsd/config.js  
  
ENTRYPOINT ["node", "/opt/statsd/stats", "/opt/statsd/config.js"]  

