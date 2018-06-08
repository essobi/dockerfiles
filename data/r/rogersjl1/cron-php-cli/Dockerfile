FROM php:7.1.8-cli  
RUN apt-get update && apt-get install -y --no-install-recommends cron \  
&& mkdir /var/php-code  
VOLUME ["/var/php-code", "/etc/cron.d"]  
CMD ["cron", "-f"]  

