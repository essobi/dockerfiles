FROM ubuntu  
# choose uid 80 for www-data  
RUN userdel www-data || true  
RUN groupdel www-data || true  
RUN groupadd www-data -g 80 || true  
RUN useradd www-data -u 80 -g 80 -M -d /nonexists -s /usr/sbin/nologin || true  
  
# install apache and php  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install apache2 libapache2-mod-
php5 php5 php5-oauth \  
php5-xmlrpc php5-gnupg php5-sqlite php5-ps php5-fpm php5-mongo php5-geoip
php5-adodb php5-apcu \  
php5-redis php5-remctl php5-ldap php5-common php5-curl php5-pinba php5-mcrypt
php5-sasl php5-tidy \  
php5-msgpack php5-readline php5-radius php5-memcache php5-librdf
php5-exactimage php5-enchant \  
php5-stomp php5-mapscript php5-cgi php5-mysqlnd-ms php5-xdebug php5-xsl
php5-cli php5-svn \  
php5-recode php5-xhprof php5-mysqlnd php5-memcached php5-interbase php5-json
php5-imap php5-rrd \  
php5-pgsql php5-pspell php5-gdcm php5-odbc php5-lasso php5-gmp php5-gd
php5-imagick php5-intl  
  
RUN apachectl start  
RUN mv /etc/php5/apache2/php.ini /etc/apache2/ && ln -s /etc/apache2/php.ini
/etc/php5/apache2/php.ini  
ADD crontab /etc/crontab  
ADD . /opt/nicedocker  
  
EXPOSE 80  
CMD ["/opt/nicedocker/run.sh"]  

