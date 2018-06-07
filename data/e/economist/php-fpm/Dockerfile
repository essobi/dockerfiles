# Install from docker image CentOS 6  
FROM centos:centos6  
#The container is maintained from Cent OS  
MAINTAINER The CentOS Project <cloud-ops@centos.org>  
  
# Perform updates  
RUN yum -y update; yum clean all  
  
# Install EPEL for owncloud packages  
RUN yum -y install epel-release; yum clean all  
RUN rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm  
  
#Instaling PHP-FPM  
RUN yum -y install --enablerepo=remi,remi-php55 php-fpm php-mbstring php-mcryp
php-mysql php-gd php-xml; yum clean all  
  
# Configure and secure PHP  
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php.ini && \  
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php-fpm.conf && \  
sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php.ini && \  
sed -i "s/short_open_tag = Off/short_open_tag = On/" /etc/php.ini && \  
sed -i '/^listen = /clisten = 0.0.0.0:9000' /etc/php-fpm.d/www.conf && \  
sed -i '/^listen.allowed_clients/c;listen.allowed_clients =' /etc/php-
fpm.d/www.conf && \  
sed -i '/^;catch_workers_output/ccatch_workers_output = yes' /etc/php-
fpm.d/www.conf && \  
sed -i "s/php_admin_flag\\[log_errors\\] = .*/;php_admin_flag[log_errors] =/"
/etc/php-fpm.d/www.conf && \  
sed -i "s/php_admin_value\\[error_log\\] =.*/;php_admin_value[error_log] =/"
/etc/php-fpm.d/www.conf && \  
sed -i "s/php_admin_value\\[error_log\\] =.*/;php_admin_value[error_log] =/"
/etc/php-fpm.d/www.conf && \  
echo "php_admin_value[display_errors] = 'stderr'" >> /etc/php-fpm.d/www.conf  
  
# DATA VOLUMES  
RUN mkdir -p /var/www/html  
VOLUME ["/var/www/html"]  
  
#ADD index.php /var/www/html/  
# PORTS  
# Port 9000 is how Nginx will communicate with PHP-FPM.  
EXPOSE 9000  
# Run PHP-FPM on container start.  
CMD ["/usr/sbin/php-fpm", "-F"]  
  

