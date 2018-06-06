FROM docker:1.12.1  
  
MAINTAINER Kris Siepert <kris@keksbox.com>  
  
ARG compose_version=1.8.0  
  
RUN apk update && apk add --no-cache \  
curl openssl ca-certificates bash git \  
&& curl -L
https://github.com/docker/compose/releases/download/${compose_version}/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose \  
&& wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub \  
&& wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.23-r3/glibc-2.23-r3.apk \  
&& apk add --no-cache glibc-2.23-r3.apk && rm glibc-2.23-r3.apk \  
&& ln -s /lib/libz.so.1 /usr/glibc-compat/lib/ \  
&& ln -s /lib/libc.musl-x86_64.so.1 /usr/glibc-compat/lib  

