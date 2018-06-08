FROM miko2u/alpine  
RUN cd /tmp \  
&& apk add shadow redis \  
\--update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/
--allow-untrusted \  
&& find / -xdev -group redis -exec chgrp 496 {} \; && groupmod -g 496 redis \  
&& find / -xdev -user redis -exec chown 496 {} \; && usermod -u 496 redis \  
&& apk del shadow \  
&& rm -rf /var/cache/apk/* \  
&& sed -e 's/^bind 127.0.0.1/bind 0.0.0.0/g' \  
-e 's/^daemonize .*$/daemonize no/g' \  
-i.dist /etc/redis.conf \  
&& printf '#!/bin/sh\n\  
/usr/bin/redis-cli info replication\n\  
' > /usr/bin/redis-check \  
&& printf '#!/bin/sh\n\  
/usr/bin/redis-cli -p 26379 info sentinel\n\  
' > /usr/bin/sentinel-check \  
&& chmod 755 /usr/bin/sentinel-check  
  
# entry  
COPY redis-sentinel.conf /etc/  
COPY init prepare /boot/  
  
# expose  
VOLUME /var/lib/redis  
EXPOSE 26379  

