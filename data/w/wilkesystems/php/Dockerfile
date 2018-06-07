FROM debian:jessie-slim  
  
MAINTAINER wilkesystems <maintainer@wilke.systems>  
  
RUN apt-get update; \  
echo "exim4-config exim4/mailname string $(hostname --fqdn)" | debconf-set-
selections; \  
echo "exim4-config exim4/dc_postmaster string postmaster@$(hostname --fqdn)" |
debconf-set-selections; \  
apt-get install -y ca-certificates cron curl exim4-daemon-light graphicsmagick
imagemagick \  
locales locales-all mysql-client openssl php5-apcu php5-cgi php5-cli \  
php5-curl php5-enchant php5-fpm php5-gd php5-gmp php5-imagick php5-imap \  
php5-interbase php5-intl php5-json php5-ldap php5-mcrypt php5-mysql \  
php5-pgsql php5-pspell php5-readline php5-recode php5-snmp php5-sqlite \  
php5-sybase php5-tidy php5-xmlrpc php5-xsl rrdtool snmp ssl-cert supervisor; \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /var/www  
  
EXPOSE 9000  
COPY ["docker-entrypoint.sh", "/usr/bin/docker-entrypoint.sh"]  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

