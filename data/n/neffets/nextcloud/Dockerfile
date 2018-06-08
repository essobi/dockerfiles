FROM nextcloud:13.0.2-apache  
  
RUN apt -y update; apt -y -f install; \  
apt -y install sudo vim libc-client-dev libkrb5-dev && \  
docker-php-ext-configure imap --with-kerberos --with-imap-ssl && \  
docker-php-ext-install imap; \  
echo '#!/bin/bash' >/usr/local/bin/occ && echo 'sudo -u www-data php
/var/www/html/occ $@' >>/usr/local/bin/occ && chmod 0755 /usr/local/bin/occ  
  

