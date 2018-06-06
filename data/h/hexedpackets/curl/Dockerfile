FROM alpine:latest  
MAINTAINER William Huba <hexedpackets@gmail.com>  
  
RUN apk add \--no-cache --update openssl curl jq && \  
addgroup -S curly && \  
adduser -S -g curly curly  
  
USER curly  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["entrypoint.sh"]  

