FROM webhippie/alpine:latest  
MAINTAINER Thomas Boerger <thomas@webhippie.de>  
  
RUN apk update && \  
apk add \  
haproxy \  
curl && \  
rm -rf /var/cache/apk/*  
  
ADD rootfs /  
EXPOSE 80 443 9000  
WORKDIR /root  
CMD ["/bin/s6-svscan", "/etc/s6"]  

