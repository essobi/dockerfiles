FROM node:8-slim  
MAINTAINER Joel Noyce Barnham <joelnbarnham@gmail.com>  
  
RUN npm install -g tiddlywiki  
  
RUN mkdir /tiddlywiki  
VOLUME ["/tiddlywiki"]  
  
ENTRYPOINT ["tiddlywiki", "/tiddlywiki", "--server"]  

