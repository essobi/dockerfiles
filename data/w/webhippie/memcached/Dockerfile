FROM webhippie/alpine:latest  
MAINTAINER Thomas Boerger <thomas@webhippie.de>  
  
RUN apk update && \  
apk add \  
memcached \  
libmemcached && \  
rm -rf /var/cache/apk/*  
  
VOLUME ["/var/lib/memcached"]  
  
ADD rootfs /  
EXPOSE 11211  
WORKDIR /root  
CMD ["/bin/s6-svscan", "/etc/s6"]  

