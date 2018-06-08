FROM node:argon  
  
EXPOSE 3000  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
RUN curl -SLO https://github.com/motepair/motepair-
server/archive/master.tar.gz  
RUN tar xvfz master.tar.gz --strip-components=1  
RUN npm install --production  
  
CMD [ "node", "target/server.js" ]  

