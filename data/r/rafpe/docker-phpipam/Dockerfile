FROM debian:wheezy  
  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update \  
&& apt-get -y install apache2 libapache2-mod-php5 php5-mysql vim curl php5-gmp
php5-ldap php-pear \  
&& apt-get clean \  
&& mkdir /var/www/html/  
  
ADD https://github.com/phpipam/phpipam/archive/1.2.tar.gz /tmp  
RUN tar -xzf /tmp/1.2.tar.gz -C /var/www/html --strip-components=1  
  
COPY 000-default.conf /etc/apache2/sites-available/default  
COPY config.php /var/www/html  
  
VOLUME ["/ssl"]  
  
RUN a2enmod rewrite  
  
# apache env vars  
ENV APACHE_LOCK_DIR /var/lock  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2/  
ENV APACHE_PID_FILE /var/apache.pid  
  
# Defaults  
ENV SSL_ENABLED false  
ENV PROXY_ENABLED false  
  
LABEL org.label-schema.build-date="2016-06-20T10:05:01Z" \  
org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.license="MIT" \  
org.label-schema.name="PHPIpam" \  
org.label-schema.url="https://rafpe.ninja" \  
org.label-schema.vcs-ref="d7ef28d" \  
org.label-schema.vcs-type="Git" \  
org.label-schema.vcs-url="https://github.com/RafPe/docker-phpipam.git"  
  
EXPOSE 80 443  
CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]  

