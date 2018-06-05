FROM alpine:latest  
MAINTAINER Matt Bentley <mbentley@mbentley.net>  
  
RUN apk --no-cache add bind &&\  
rm /var/bind/pri/127.zone /var/bind/pri/localhost.zone &&\  
deluser named &&\  
addgroup -g 505 named &&\  
adduser -h /etc/bind -D -u 505 -g named -G named -s /sbin/nologin named &&\  
chgrp named /etc/bind /var/bind /var/run/named /var/bind/dyn /var/bind/pri
/var/bind/sec  
  
COPY *.zone /var/bind/pri/  
  
RUN ln -s /etc/bind/named.conf.recursive /etc/bind/named.conf &&\  
sed -i '/listen-on { 127.0.0.1; };/s/^/\/\//g' /etc/bind/named.conf.recursive
&&\  
sed -i '/127.0.0.1\/32/s//0.0.0.0\/0/g' /etc/bind/named.conf.recursive &&\  
sed -i '/^options.*/a prefetch 2 9;' /etc/bind/named.conf.recursive &&\  
named-checkconf /etc/bind/named.conf  
  
COPY entrypoint.sh /entrypoint.sh  
  
EXPOSE 53 53/udp  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/sbin/named","-c","/etc/bind/named.conf","-f","-u","named","-g"]  

