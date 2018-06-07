FROM docker:1.12.0  
MAINTAINER Rui Fernando Hayashi <rfhayashi@gmail.com>  
  
RUN apk add --update openjdk8=8.92.14-r1  
  
RUN apk add --update bash=4.3.42-r3  
  
# avoid "Failed to load native library 'libnative-platform.so' for Linux
amd64." error  
RUN apk add --update libstdc++=5.3.0-r0  
  
RUN rm -rf /var/cache/apk/*  
  
ENV LEIN_ROOT true  
  
RUN wget -q -O /usr/bin/lein \  
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein \  
&& chmod +x /usr/bin/lein  
  
RUN lein upgrade 2.6.1  
  
RUN mkdir /app  
WORKDIR /app

