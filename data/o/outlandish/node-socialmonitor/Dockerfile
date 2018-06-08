FROM node:6-alpine  
  
RUN apk update && apk add git  
  
RUN apk --no-cache add --virtual native-deps \  
g++ gcc libgcc libstdc++ linux-headers make python && \  
npm install --quiet node-gyp -g &&\  
npm install --quiet && \  
apk del native-deps  

