FROM ubuntu:16.04  
MAINTAINER Sebastian Wasser <sebastian.wasser@gmail.com>  
  
ENV SCRIPT_PATH ${SCRIPT_PATH:-/opt/srdb}  
ENV CONFIG_PATH ${CONFIG_PATH:-/tmp/wp-config.php}  
  
RUN set -ex; \  
apt-get update; \  
apt-get install -y git php-cli php-mysql php-mbstring; \  
git clone https://github.com/interconnectit/Search-Replace-DB ${SCRIPT_PATH};
\  
apt-get remove -y git; \  
apt-get autoremove -y && apt-get clean; \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*;  
  
COPY entrypoint.sh /docker-entrypoint.sh  
COPY srdb.sh /usr/bin/srdb  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["/usr/bin/supervisord"]  

