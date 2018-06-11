FROM php:7.0.6-apache  
MAINTAINER Azure App Services Container Images <appsvc-images@microsoft.com>  
  
COPY apache2.conf /bin/  
COPY init_container.sh /bin/  
COPY hostingstart.html /home/site/wwwroot/hostingstart.html  
  
RUN a2enmod rewrite expires include  
  
# install the PHP extensions we need  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
openssh-server vim curl wget tcptraceroute \  
&& chmod 755 /bin/init_container.sh \  
&& echo "root:Docker!" | chpasswd  
  
RUN \  
rm -f /var/log/apache2/* \  
&& rmdir /var/lock/apache2 \  
&& rmdir /var/run/apache2 \  
&& rmdir /var/log/apache2 \  
&& chmod 777 /var/log \  
&& chmod 777 /var/run \  
&& chmod 777 /var/lock \  
&& chmod 777 /bin/init_container.sh \  
&& cp /bin/apache2.conf /etc/apache2/apache2.conf \  
&& rm -rf /var/www/html \  
&& rm -rf /var/log/apache2 \  
&& mkdir -p /home/LogFiles \  
&& ln -s /home/site/wwwroot /var/www/html \  
&& ln -s /home/LogFiles /var/log/apache2  
  
RUN { \  
echo 'error_log=/var/log/apache2/php-error.log'; \  
echo 'display_errors=Off'; \  
echo 'log_errors=On'; \  
echo 'display_startup_errors=Off'; \  
echo 'date.timezone=UTC'; \  
} > /usr/local/etc/php/conf.d/php.ini  
  
COPY sshd_config /etc/ssh/  
  
EXPOSE 2222 8080  
ENV APACHE_RUN_USER www-data  
ENV PHP_VERSION 7.0.6  
ENV PORT 8080  
ENV WEBSITE_ROLE_INSTANCE_ID localRoleInstance  
ENV WEBSITE_INSTANCE_ID localInstance  
ENV PATH ${PATH}:/home/site/wwwroot  
  
WORKDIR /var/www/html  
  
ENTRYPOINT ["/bin/init_container.sh"]  

