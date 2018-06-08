FROM ubuntu:latest  
  
ENV POWERADMIN_VERSION 2.1.7  
ENV DB_HOST localhost  
ENV DB_PORT 3306  
ENV DB_NAME pdns  
ENV DB_USER pdns  
ENV DB_PASS pdns  
ENV DB_TYPE mysql  
ENV DNS_NS1 8.8.8.8  
ENV DNS_NS2 8.8.4.4  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -q update && apt-get -q install curl apache2 libapache2-mod-php5
php5 php5-common php5-mcrypt php5-curl php5-dev php5-gd php-pear php5-imap
php5-mcrypt php5-ming php5-mysql php5-xmlrpc gettext php-db php-mdb2 php-
mdb2-driver-mysql -y && \  
php5enmod mcrypt && \  
curl -sLo poweradmin-${POWERADMIN_VERSION}.tgz
http://freefr.dl.sourceforge.net/project/poweradmin/poweradmin-${POWERADMIN_VERSION}.tgz
&& \  
tar xf poweradmin-${POWERADMIN_VERSION}.tgz -C /tmp && \  
rm -f /var/www/html/* && \  
mv /tmp/poweradmin-${POWERADMIN_VERSION}/* /var/www/html/ && \  
cp /var/www/html/inc/config-me.inc.php /var/www/html/config.inc.php && \  
rm -rf /var/www/html/install && \  
chown -R www-data:www-data /var/www  
  
ADD entrypoint.sh /entrypoint.sh  
  
CMD ["tailf", "/var/log/apache2/error.log"]  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 80  

