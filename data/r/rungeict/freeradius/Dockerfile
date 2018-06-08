FROM alpine  
  
RUN apk update && apk upgrade && \  
apk add --update ca-certificates freeradius freeradius-radclient freeradius-
eap freeradius-rest freeradius-ldap && \  
chgrp radius /var/run/radiusd && chmod g+rwx /var/run/radiusd && \  
rm /var/cache/apk/*  
  
RUN update-ca-certificates  
  
VOLUME /etc/raddb/  
  
EXPOSE 1812/udp 1813/udp 1812 1813  
# ENTRYPOINT radiusd  
CMD radiusd -f -l stdout  

