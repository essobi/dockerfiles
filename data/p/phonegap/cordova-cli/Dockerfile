FROM node:8.0.0-alpine  
MAINTAINER goya "rudd@adobe.com"  
# install global npm module 'cordova' at version 7.0.1  
RUN apk add \--update git && \  
npm install -g cordova@7.0.1  
  
# change user to non-priveleged user  
USER node  
  
# turn telemetry on by default  
RUN cordova telemetry on  
  
# default location is /workspace  
WORKDIR /workspace  
  
# 'cordova' is the default command  
ENTRYPOINT ["cordova"]

