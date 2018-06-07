FROM gliderlabs/alpine:3.4  
MAINTAINER Kyle Ondy <kyle@ondy.me>  
  
RUN apk add --no-cache \  
# build base for the znc-push module  
build-base \  
curl \  
openssl-dev \  
znc \  
znc-dev  
  
ADD docker-entrypoint.sh /entrypoint.sh  
ADD znc.conf.default /znc.conf.default  
RUN chmod 644 /znc.conf.default  
  
EXPOSE 6667  
ENTRYPOINT ["/entrypoint.sh"]  

