# Pull base image.  
FROM node:7.9.0-alpine  
  
COPY packages.list /opt/packages.list  
  
# Install dependencies  
RUN apk update && \  
apk add wget && \  
apk add alpine-sdk make python && \  
apk add \--quiet --no-cache bash git && \  
yarn global add bower gulp && \  
yarn cache clean && \  
yarn add \--force node-sass && \  
mkdir /opt/offline && rm -rf /var/cache/* /tmp/* && \  
cd /opt/offline && wget --content-disposition --trust-server-names --no-check-
certificate --input-file=/opt/packages.list && \  
yarn config set yarn-offline-mirror /opt/offline  
  
# Define working directory.  
WORKDIR /opt/project

