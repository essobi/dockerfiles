FROM google/nodejs  
  
RUN apt-get install -y net-tools  
  
COPY server.js /server.js  
COPY start.sh /usr/bin/start  
  
CMD ["start"]

