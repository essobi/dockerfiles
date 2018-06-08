FROM ghost:0.7.6  
MAINTAINER Kha Nguyen <nlhkha@gmail.com>  
COPY config.js /usr/src/ghost/config.example.js  
RUN cp /usr/src/ghost/config.example.js /var/lib/ghost/config.js  
ENV NODE_ENV production  

