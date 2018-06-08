FROM node:0.10  
RUN npm install -g statsd@0.7.2  
  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod a+x /docker-entrypoint.sh  
RUN mkdir /opt/statsd  
ENTRYPOINT ["/docker-entrypoint.sh"]  

