FROM ubuntu:xenial  
RUN export DEBIAN_FRONTEND=noninteractive  
RUN export RUNLEVEL=1  
RUN echo "#!/bin/sh \nexit 0" > /usr/sbin/policy-rc.d  
RUN apt-get update  
RUN apt-get install -y nginx php-fpm php-mysql php-gd php-zip php-json php-
curl php-mbstring php-intl php-mcrypt php-imagick php-xml php-redis php-
memcached php-apcu php-gmp php-smbclient php-sqlite3  
ADD nginx.conf /etc/nginx/sites-available/default  
RUN nginx -t  
ADD /entrypoint.sh .  
RUN chmod +x /entrypoint.sh  
CMD ["/entrypoint.sh"]  

