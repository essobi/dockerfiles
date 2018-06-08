FROM ivixq/alpine-s6  
MAINTAINER ivixq  
  
RUN echo '@main http://nl.alpinelinux.org/alpine/edge/main' >>
/etc/apk/repositories && \  
apk update && apk upgrade && \  
apk add --update freeradius@main \  
freeradius-sqlite@main \  
freeradius-lib@main \  
freeradius-radclient@main \  
freeradius-mysql@main \  
pwgen \  
mutt \  
msmtp \  
mariadb-client@main && \  
rm -rf /var/cache/apk/*  
  
COPY rootfs /  
  
RUN ln -snf /etc/raddb/mods-available/sql /etc/raddb/mods-enabled/ && \  
chgrp radius /usr/sbin/radiusd && chmod g+rwx /usr/sbin/radiusd && \  
chgrp radius /etc/raddb/mods-available/sql  
  
VOLUME [ "/userpass/" ] \  
[ "/scripts/" ]  
  
EXPOSE 1812/udp \  
1813/udp \  
18120/udp  
  
ENTRYPOINT [ "/init" ]  
  
CMD []  
  

