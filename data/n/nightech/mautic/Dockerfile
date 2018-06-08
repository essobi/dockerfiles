FROM nightech/php-fpm:7.0  
ENV EXT_IMAP "on"  
ENV EXT_INTL "on"  
ENV EXT_MCRYPT "on"  
ENV EXT_MYSQL "on"  
ENV EXT_REDIS "on"  
ENV EXT_SOCKETS "on"  
ENV EXT_ZIP "on"  
ENV PHP_EXT_OPCACHE_VALIDATE_TIMESTAMPS "0"  
COPY ./overlay/ /  
  
RUN apt-get update -y && \  
apt-get install -y --no-install-recommends gawk && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
useradd fcron && \  
chmod 644 /usr/local/etc/fcron.conf && \  
mkdir -p /usr/local/var/spool/fcron && \  
chown root.fcron /usr/local/etc/fcron.conf /usr/local/var/spool/fcron  
  
HEALTHCHECK \--interval=60s --retries=3 --timeout=5s CMD \  
fcrondyn -x ls | grep root || exit 1  
  
VOLUME /var/www/mautic  
WORKDIR /var/www/mautic  
  
ENTRYPOINT ["docker-fcron-entrypoint.sh"]  
CMD fcron -f --nosyslog  

