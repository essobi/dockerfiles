FROM alpine:3.1  
MAINTAINER Jeremy Klein <jeremydk@gmail.com>  
  
WORKDIR /etc/raddb  
  
RUN apk update && apk upgrade && \  
apk add --update freeradius3 freeradius3-sqlite freeradius3-radclient sqlite
openssl-dev && \  
chgrp radius /usr/sbin/radiusd && chmod g+rwx /usr/sbin/radiusd && \  
rm /var/cache/apk/* && chgrp radius /etc/raddb/mods-available  
  
VOLUME \  
/opt/db/  
  
EXPOSE \  
1812/udp \  
1813 \  
18120  
CMD ["radiusd","-xx","-f"]  

