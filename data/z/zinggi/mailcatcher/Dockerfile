FROM alpine:3.4  
MAINTAINER Christian Zingg <mich-web@zinggi.ch>  
  
# Install Mailcatcher  
RUN apk add --no-cache ca-certificates openssl  
RUN apk add --no-cache ruby ruby-bigdecimal ruby-json sqlite-libs libstdc++  
RUN apk add --no-cache --virtual .build-deps ruby-dev make g++ sqlite-dev && \  
gem install mailcatcher --no-ri --no-rdoc && \  
apk del .build-deps  
  
# SMTP Port  
EXPOSE 1025  
# Webserver Port  
EXPOSE 1080  
CMD ["mailcatcher", "-f", "--ip=0.0.0.0"]

