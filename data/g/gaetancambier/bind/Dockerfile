FROM alpine:latest  
  
MAINTAINER Gaetan Cambier "Gaetan@Cambier.org"  
EXPOSE 53/tcp 53/udp  
  
ENV BIND_USER=bind \  
DATA_DIR=/data  
  
RUN apk add --update --no-cache bind && \  
mkdir -m 0755 -p /var/run/named && \  
chown -R root:named /var/run/named  
  
VOLUME ["/data"]  
  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
  

