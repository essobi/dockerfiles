FROM alpine:3.7  
MAINTAINER Tom Price <tom@codedinternet.com>  
  
RUN apk add \--no-cache freeradius freeradius-eap freeradius-sqlite
freeradius-radclient sqlite openssl-dev  
RUN chgrp radius  /usr/sbin/radiusd && chmod g+rwx /usr/sbin/radiusd  
  
VOLUME \  
/opt/certs \  
/opt/db/ \  
/etc/raddb  
  
EXPOSE \  
1812/udp \  
1813/udp \  
18120  
  
CMD ["radiusd", "-xx", "-f"]  

