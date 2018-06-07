FROM alpine:3.4  
  
MAINTAINER engineering@reviewtrackers.com  
  
RUN echo '@edge http://nl.alpinelinux.org/alpine/edge/main' >>
/etc/apk/repositories && \  
echo '@community http://nl.alpinelinux.org/alpine/edge/community' >>
/etc/apk/repositories && \  
echo '@testing http://nl.alpinelinux.org/alpine/edge/testing' >>
/etc/apk/repositories && \  
apk update && \  
apk upgrade && \  
apk add --update \  
bash \  
build-base \  
ca-certificates \  
curl \  
git \  
openssl \  
tar \  
unzip \  
wget \  
xz && \  
wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub && \  
apk --no-cache -X http://apkproxy.heroku.com/andyshinn/alpine-pkg-glibc add
glibc glibc-bin && \  
rm -rf /var/cache/apk/*  
  
CMD /bin/bash  

