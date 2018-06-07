#FROM node:6.10.0-alpine  
FROM node:6.10.0  
  
MAINTAINER abner <contato@abner.io>  
  
RUN apt-get update && apt-get install --no-install-recommends -y python gcc
g++ make \  
&& npm config set cache /cache/.npm/ \  
&& yarn config set cache-folder /cache/yarn \  
&& rm $(which yarn) \  
&& npm i -g yarn@0.24.4 \  
&& npm i -g node-sass@4.5.3 \  
&& npm i -g ionic@3.15.2 \  
&& yarn global add npm@5.3.0 \  
&& apt-get -y remove python gcc g++ make \  
&& rm -rf /var/lib/apt/lists/*  
#RUN apk add --no-cache --virtual .build-deps ca-certificates make gcc g++ git
build-base \  
# && apk add --no-cache python=2.7.12-r0 \  
# && rm -rf /var/cache/apk/* \  
# && npm config set cache /cache/.npm/ \  
# && yarn config set cache-folder /cache/yarn \  
# && mkdir -p /cache/yarn && mkdir -p /cache/.npm \  
# && npm install -g yarn@0.24.4 \  
# && npm i --global node-sass@4.3.0 \  
# && yarn global add "ionic@3.1.2" node-sass@4.5.3 \  
# && apk del .build-deps \  
# && rm -Rf /cache/yarn; rm -Rf /cache/.npm \  
# && mkdir -p /cache/yarn && mkdir -p /cache/.npm  

