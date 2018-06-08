FROM centos:7  
  
EXPOSE 80  
  
RUN yum -y update && yum -y install centos-release-scl && yum makecache fast
&& \  
yum -y update && yum -y install \  
git \  
httpd \  
php55 \  
php55-php \  
php55-php-mbstring \  
php55-php-gd \  
php55-php-pdo \  
php55-php-bcmath \  
php55-php-ldap \  
php55-php-snmp \  
php55-php-mysqlnd \  
php55-php-fpm && \  
git clone https://github.com/RackTables/racktables.git && \  
rm -f /etc/httpd/conf.d/welcome.conf && \  
cp /opt/rh/httpd24/root/etc/httpd/conf.d/php55-php.conf /etc/httpd/conf.d/ &&
\  
cp /opt/rh/httpd24/root/etc/httpd/conf.modules.d/10-php55-php.conf
/etc/httpd/conf.modules.d/ && \  
cp /opt/rh/httpd24/root/etc/httpd/modules/libphp55-php5.so /etc/httpd/modules/
&& \  
cp /opt/rh/php55/root/etc/php.ini /etc/php.ini && \  
rm -rf /var/cache/yum  
  
ADD httpd.conf /etc/httpd/conf/httpd.conf  
  
VOLUME /var/log/httpd  
  
CMD ["/usr/sbin/httpd", "-DFOREGROUND"]  
  

