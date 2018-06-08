FROM alpine:latest  
  
MAINTAINER Harianto van Insulinde <hariantoatwork@gmail.com>  
  
RUN apk update && apk upgrade  
RUN apk add --update nodejs \  
make \  
python \  
bash \  
git  
  
WORKDIR /usr/src/app  
RUN git clone https://github.com/jsonfry/node-livereload.git .  
RUN npm install  
  
ENTRYPOINT node bin/livereload.js /usr/src/livereload-watch -u true -d  

