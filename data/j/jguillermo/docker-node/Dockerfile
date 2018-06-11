FROM node:6.12.3-slim  
  
MAINTAINER Jose Guillermo <jguillermo@outlook.com>  
  
ENV VERSION 1.1  
  
ENV SRC_DIR=/usr/src  
  
RUN mkdir -p $SRC_DIR && chmod 777 -R $SRC_DIR && \  
mkdir /nodecache && chmod 777 -R /nodecache && npm config set cache /nodecache
--global  
  
WORKDIR $SRC_DIR

