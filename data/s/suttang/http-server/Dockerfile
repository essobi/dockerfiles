FROM node:8.7.0  
RUN apt-get update \  
&& npm install -g http-server  
  
WORKDIR /docroot  
  
CMD http-server /docroot -p 80  

