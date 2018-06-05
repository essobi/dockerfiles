FROM alpine:latest  
MAINTAINER Felix Seidel <felix@seidel.me>  
  
VOLUME /agent  
  
RUN apk add --update openssh sudo && \  
rm -rf /var/cache/apk/* && \  
adduser -u 1000 -g 1000 -D -H agent  
  
ADD docker-entrypoint.sh /  
ADD add.sh /usr/local/bin/  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

