FROM phpmyadmin/phpmyadmin:latest  
  
COPY ./config.user.inc.php /etc/phpmyadmin/config.user.inc.php  
COPY ./theme /www/themes/pmahomme-tgtg  
  
# Copied from https://github.com/phpmyadmin/docker/blob/master/Dockerfile  
RUN set -ex; \  
chown -R root:nobody /www/themes/pmahomme-tgtg; \  
find /www/themes/pmahomme-tgtg -type d -exec chmod 750 {} \; ; \  
find /www/themes/pmahomme-tgtg -type f -exec chmod 640 {} \; ;  

