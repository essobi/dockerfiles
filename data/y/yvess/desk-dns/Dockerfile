FROM yvess/desk-worker:0.1.2  
MAINTAINER Yves Serrano <y@yas.ch>  
  
RUN echo -e "http://dl-cdn.alpinelinux.org/alpine/edge/main\nhttp://dl-
cdn.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories && \  
apk add --no-cache \  
boost-serialization \  
boost-program_options \  
pdns \  
pdns-backend-sqlite3 && \  
ln -s /usr/lib/pdns/pdns/libgsqlite3backend.so
/usr/lib/pdns/libgsqlite3backend.so && \  
rm -rf /var/cache/apk/*  
# rm /etc/pdns.conf && \  
ADD ./etc/ /etc/  
ENV WORKER_TYPE worker  
ENV WORKER_SUBTYPE dns  
EXPOSE 53/udp 53/tcp  

