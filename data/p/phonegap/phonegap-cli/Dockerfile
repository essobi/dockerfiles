FROM node:7.9.0-alpine  
MAINTAINER goya "rudd@adobe.com"  
# install global npm module 'phonegap' at version 6.5.0  
RUN apk add \--update git && \  
npm install -g phonegap@6.5.0  
  
# change user to non-priveleged user  
USER node  
  
# turn analytics on by default  
RUN phonegap analytics on  
  
# default location is /workspace  
WORKDIR /workspace  
  
# 'phonegap' is the default command  
ENTRYPOINT ["phonegap"]

