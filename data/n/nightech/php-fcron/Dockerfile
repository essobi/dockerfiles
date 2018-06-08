FROM nightech/php-fpm:7.1  
COPY ./overlay/ /  
  
RUN apt-get update -y && \  
apt-get install -y --no-install-recommends gawk vim && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
useradd fcron && \  
chmod 644 /usr/local/etc/fcron.conf && \  
mkdir -p /usr/local/var/spool/fcron && \  
chown root.fcron /usr/local/etc/fcron.conf /usr/local/var/spool/fcron  
  
HEALTHCHECK \--interval=60s --retries=3 --timeout=5s CMD \  
fcrondyn -x ls | grep root || exit 1  
  
ENTRYPOINT ["docker-fcron-entrypoint.sh"]  
CMD fcron -f --nosyslog  

