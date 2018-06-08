FROM alpine:latest  
MAINTAINER Erlend Aakre <erlend@frostvoid.com>  
  
USER root  
COPY murmur.ini /etc/murmur.tpl  
COPY init.sh /usr/bin/init.sh  
  
RUN apk upgrade \--update-cache --available && \  
apk --no-cache add qt-mysql && \  
apk --no-cache add murmur  
  
RUN addgroup mumble && \  
adduser -h /home/mumble -s /sbin/nologin -D -G mumble mumble && \  
chown -R mumble /home/mumble && \  
chown -R mumble /etc/murmur.tpl && \  
chown -R mumble /usr/bin/init.sh && \  
mkdir -p /data && \  
chown -R mumble /data  
  
USER mumble  
  
VOLUME ["/data"]  
  
EXPOSE 64738 64738/udp  
  
CMD ["/usr/bin/init.sh"]  
  

