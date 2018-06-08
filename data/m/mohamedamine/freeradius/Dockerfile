FROM alpine  
RUN echo 'radius:x:1100:1100:radius:/var/log/radius:/sbin/nologin' >>
/etc/passwd && \  
echo 'radius:x:1100:radius' >> /etc/group  
RUN apk update && \  
apk upgrade && \  
apk add --update freeradius freeradius-ldap && \  
chgrp radius /var/run/radiusd && \  
chmod g+rwx /var/run/radiusd && \  
rm /var/cache/apk/* && \  
rm -rf /etc/raddb  
EXPOSE 1812/udp 1813/udp  
ENTRYPOINT ["radiusd","-f"]  

