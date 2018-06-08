# NolimitID docker images with alpine-linux 3.1,  
# nodejs v0.12.9, phantomjs 1.9.8, karma-cli 0.1.0,  
# and webpack 1.9.7  
FROM mhart/alpine-node:0.12.9  
MAINTAINER maman <achmad@mahardi.me>  
  
# Set ENV  
ENV NODE_ENV dev  
ENV PHANTOMJS_VERSION 1.9.8  
ENV BUILD_PACKAGES gcc g++ make python rsync  
  
# Commands  
RUN \  
apk add --update $BUILD_PACKAGES && \  
rm -rf /var/cache/apk/* && \  
npm install webpack@1.9.7 && \  
npm install karma-cli@0.1.0  

