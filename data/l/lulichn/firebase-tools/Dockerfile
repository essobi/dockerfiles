# use latest Node LTS (Carbon)  
FROM node:carbon-alpine  
  
ENV PACKAGE firebase-tools  
ENV VERSION 3.17.4  
  
RUN apk add \--no-cache --virtual .gyp python make g++ \  
&& apk --no-cache add avahi-dev \  
&& npm install mdns \  
&& apk del .gyp  
  
# set user to avoid permission issues  
# (see https://github.com/nodejs/node-gyp/issues/1236)  
USER node  
RUN mkdir /home/node/.npm-global  
ENV PATH=/home/node/.npm-global/bin:$PATH  
ENV NPM_CONFIG_PREFIX=/home/node/.npm-global  
  
# install Firebase CLI  
RUN npm install -g $PACKAGE@$VERSION  
# reset user back to root  
USER root  
  
RUN mkdir /data  
WORKDIR /data  
  
ENTRYPOINT ["firebase"]  
  

