FROM mhart/alpine-node:6.11.2  
MAINTAINER Kayvan Sylvan <kayvansylvan@gmail.com>  
  
RUN apk update && apk upgrade  
  
RUN apk add --no-cache g++ gcc make postgresql-dev python git  
RUN rm -rf /usr/share/man /tmp/* /var/cache/apk/* /root/.npm \  
/root/.node-gyp /root/.gnupg /usr/lib/node_modules/npm/man \  
/usr/lib/node_modules/npm/doc /usr/lib/node_modules/npm/html  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ONBUILD COPY package.json /usr/src/app/  
ONBUILD RUN npm install  
ONBUILD RUN rm -rf /tmp/npm*  
ONBUILD COPY . /usr/src/app  
  
CMD [ "npm", "start" ]  

