FROM alpine:latest  
  
RUN apk update && apk upgrade  
  
RUN apk add --no-cache samba-dc krb5 && rm -rf /var/cache/apk/*  
  
VOLUME /etc/samba  
VOLUME /var/lib/samba  
  
EXPOSE 53 88 135 139 389 445 464 636 1024-5000  
EXPOSE 53/udp 88/udp 137/udp 138/udp 389/udp 464/udp  
  
CMD /usr/sbin/samba -i  

