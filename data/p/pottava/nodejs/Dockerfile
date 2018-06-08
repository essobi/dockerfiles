# Node.js v7.7  
# docker run --rm pottava/nodejs:7.7 node -v  
# docker run --rm pottava/nodejs:7.7 npm -v  
FROM alpine:edge  
  
ENV NPM_CONFIG_LOGLEVEL=info \  
NODE_VERSION=7.7.4-r0  
  
RUN apk --no-cache add ca-certificates \  
&& apk --no-cache add nodejs-current=$NODE_VERSION  

