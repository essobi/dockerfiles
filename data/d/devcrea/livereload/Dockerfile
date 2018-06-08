FROM node:latest  
MAINTAINER "VAILLANT Jérémy" <vaillant.jeremy@dev-crea.com>  
  
WORKDIR /usr/src/app  
RUN git clone https://github.com/jsonfry/node-livereload.git .  
RUN npm install  
  
ENTRYPOINT node bin/livereload.js /usr/src/livereload-watch -u true -d -e
"haml yml"  

