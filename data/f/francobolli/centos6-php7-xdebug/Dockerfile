# Switched back to Centos 6, as there is an error in the hub repo for Centos 7
concerning httpd  
# See: https://github.com/docker/hub-feedback/issues/461  
FROM centos:6  
MAINTAINER Francesco de Guytenaere <guytenaere.fe@gmail.com>  
  
RUN yum update -y && yum -y install epel-release && yum clean all  
  
#RUN rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm  
RUN rpm -Uvh https://mirror.webtatic.com/yum/el6/latest.rpm  
RUN yum update -y \  
&& yum install -y supervisor git wget vim iproute httpd \  
&& yum -y install \  
php70w \  
php70w-bcmath \  
php70w-cli \  
php70w-fpm \  
php70w-common \  
php70w-mbstring \  
php70w-mcrypt \  
php70w-mysqlnd \  
php70w-pdo \  
php70w-pecl-imagick \  
php70w-pecl-xdebug \  
php70w-opcache \  
php70w-xml \  
&& yum clean all  
  
# Composer  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer  
  
# Copy settings  
COPY php.d/ /etc/php.d/  
COPY conf.d/ /etc/httpd/conf.d/  
RUN IP=$(/sbin/ip route|awk '/default/ { print $3 }'); printf
"xdebug.remote_connect_back=Off\nxdebug.remote_host="${IP}"" >>
/etc/php.d/xdebug.ini  
RUN printf "Include vhost.d/*.conf" >> /etc/httpd/conf/httpd.conf  
  
# Adding the configuration file of the Supervisor  
ADD supervisord.conf /etc/  
  
#Ports  
EXPOSE 80 9000  
# Executing supervisord  
# -n / --nodaemon : runs in foreground ( required for docker )  
# -c <configfile> : specifies the config file  
CMD ["supervisord", "-n", "-c", "/etc/supervisord.conf"]  

