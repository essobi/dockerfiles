FROM alpine:latest  
MAINTAINER raffaele messuti <raffaele@atomotic.com>  
  
RUN apk add \--update alpine-sdk python3 python3-dev py3-cffi py3-crypto
py3-openssl py3-gevent tor \  
&& pip3 install pysocks pywb \  
&& pip3 install chaperone && mkdir /etc/chaperone.d \  
&& apk del alpine-sdk  
  
COPY chaperone.conf /etc/chaperone.d/chaperone.conf  
  
EXPOSE 8080  
ENTRYPOINT ["/usr/bin/chaperone"]

