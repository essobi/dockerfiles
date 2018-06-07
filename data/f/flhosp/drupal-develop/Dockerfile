FROM flhosp/apache-php:5.3.3  
MAINTAINER Kevin Finley <kevishie@gmail.com>  
  
RUN \  
yum --setopt=tsflags=nodocs -y install php-pdo php-mysql php-ldap php-soap \  
&& yum --setopt=tsflags=nodocs -y install php-xml php-xmlrpc php-intl php-tidy
\  
&& yum --setopt=tsflags=nodocs -y install ImageMagick \  
&& yum clean all  
  
## Configure php.ini for development  
RUN { \  
echo 'memory_limit = 1G'; \  
echo 'max_execution_time = 90'; \  
echo 'error_reporting = E_ALL | E_STRICT'; \  
echo 'display_errors = On'; \  
echo 'display_startup_errors = On'; \  
} >> /etc/php.ini  
  
## Need to allow Options and Override for clean urls.  
RUN { \  
echo '<Directory "/var/www/html">'; \  
echo 'Options All'; \  
echo 'AllowOverride All'; \  
echo 'Order allow,deny'; \  
echo 'Allow from all'; \  
echo '</Directory>'; \  
} >> /etc/httpd/conf/httpd.conf  
  
WORKDIR /var/www/html  

