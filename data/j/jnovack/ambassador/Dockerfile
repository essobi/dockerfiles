FROM alpine:3.5  
MAINTAINER Justin J. Novack <jnovack@gmail.com>  
  
ENTRYPOINT ["/usr/bin/entrypoint.sh"]  
  
RUN apk add --update --no-cache openssl socat supervisor && \  
rm -rf /var/cache/apk  
  
COPY entrypoint.sh /usr/bin/entrypoint.sh

