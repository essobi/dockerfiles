###  
# Copyright (c) Mainflux  
#  
# This file is part of iotagent-json and is published under GNU Affero General
Public License  
# See the included LICENSE file for more details.  
###  
FROM node:6.10.3  
MAINTAINER Daniel Moran Jimenez <daniel.moranjimenez@telefonica.com>  
  
ARG NODEJS_VERSION=  
  
COPY . /opt/iotajson/  
WORKDIR /opt/iotajson  
  
ENV NODE_PATH="${NODE_PATH}:/opt/iotajson/third-party"  
RUN cd /opt/iotajson && npm install --production && cd /opt/iotajson/third-
party/iotagent-node-lib/ && npm install --production  
  
ENTRYPOINT bin/iotagent-json config.js  
  
EXPOSE 4041  

