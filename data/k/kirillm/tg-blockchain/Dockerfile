FROM node:8-alpine  
  
VOLUME /opt/app/tmp/  
  
ADD ./package.json /opt/app/package.json  
  
RUN apk --no-cache add git libgit2-dev python tzdata pkgconfig build-base  
  
WORKDIR /opt/app  
  
RUN BUILD_ONLY=true npm install  
  
ADD . /opt/app  
  
CMD node index.js  

