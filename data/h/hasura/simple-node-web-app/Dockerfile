# simple-node-web-app  
FROM mhart/alpine-node:4.4  
MAINTAINER Shahidh <shahidh@hasura.io>  
RUN mkdir /app  
COPY app/runserver.sh /runserver.sh  
COPY app/src/package.json /app/package.json  
RUN cd /app && npm install  
RUN mv /app/node_modules /node_modules  
COPY app/src/server.js /app/server.js  
COPY app/src/index.html /app/index.html  
ENV NODE_PATH /node_modules:$NODE_PATH  
CMD ["/runserver.sh"]  

