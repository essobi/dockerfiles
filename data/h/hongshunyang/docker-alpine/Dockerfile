FROM alpine:3.6  
MAINTAINER Hongshun Yang <yanghongshun@outlook.com>  
  
# updated  
## add openssl bash  
RUN apk add -U ca-certificates openssl bash zlib file  
  
## add dockerize  
ENV DOCKERIZE_VERSION v0.5.0  
ENV DOCKERIZE_DOWNLOAD_URL
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
RUN wget -qO- $DOCKERIZE_DOWNLOAD_URL | tar xvz -C /usr/local/bin  
  
## add dig  
ENV BIND_DIG_VERSION 9.11.1rc3  
ENV BIND_DIG_DOWNLOAD_URL
ftp://ftp.isc.org/isc/bind9/$BIND_DIG_VERSION/bind-$BIND_DIG_VERSION.tar.gz  
  
RUN apk add -U --virtual build-deps linux-headers alpine-sdk curl zlib-dev \  
&& cd /tmp \  
&& curl $BIND_DIG_DOWNLOAD_URL | tar -xzv \  
&& cd bind-$BIND_DIG_VERSION \  
&& CFLAGS="-static" ./configure --without-openssl --disable-symtable \  
&& make \  
&& cp ./bin/dig/dig /usr/bin/ \  
&& apk del build-deps \  
&& rm -rf /tmp/* \  
&& rm -rf /va/cache/apk/*  
  
## add local repo for building custom package  
## https://bitbucket.org/hongshunyang/alpine-abuild  
RUN mkdir /alpine-abuild \  
&& echo '@alpine-abuild /alpine-abuild' >> /etc/apk/repositories  
COPY keys/yanghongshun@outlook.com-2017-01-03-22-48-50.rsa.pub
/etc/apk/keys/alpine-abuild.rsa.pub  
VOLUME ["/alpine-abuild"]  
## docker run -it -v $(pwd)/build/packages/main:/alpine-abuild
hongshunyang/docker-alpine /bin/bash  

