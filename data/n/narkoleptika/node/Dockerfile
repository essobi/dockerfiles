FROM node:alpine  
MAINTAINER Joey Marsh "joey@clever.ly"  
RUN apk --update --no-cache add \  
alpine-sdk \  
autoconf \  
automake \  
libtool \  
libpng-dev \  
nasm  
  
ENV NPM_CONFIG_LOGLEVEL warn  
EXPOSE 80  
EXPOSE 443  
EXPOSE 3000  
COPY entrypoint /usr/local/bin/entrypoint  
RUN mkdir -p /usr/src/app  
VOLUME /usr/src/app  
VOLUME /usr/src/app/node_modules  
WORKDIR /usr/src/app  
  
ENTRYPOINT ["entrypoint"]  

