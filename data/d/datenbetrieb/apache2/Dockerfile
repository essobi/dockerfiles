# DOCKER-VERSION 1.0.0  
FROM datenbetrieb/ubuntu:trusty  
MAINTAINER Peter Niederlag "peter.niederlag@datenbetrieb.de"  
# add apt packages for apache2 and php5  
RUN apt-get update && \  
apt-get install -y --no-install-recommends apache2 apache2-mpm-prefork && \  
apt-get install -y --no-install-recommends libapache2-mod-php5 && \  
apt-get install -y --no-install-recommends php5-cli php5-gd php5-json
php5-ldap php5-mcrypt php5-sqlite php5-xdebug php5-curl php5-xsl php5-mysql &&
\  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
## Remove default VirtualHost  
RUN rm -f /etc/apache2/sites-available/*  
  
# Enable rewrite module  
RUN a2enmod rewrite expires  
  
# add composer  
RUN curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer  
  
# forward request and error logs to docker log collector  
#RUN ln -sf /dev/stdout /var/log/apache2/access.log  
#RUN ln -sf /dev/stderr /var/log/apache2/error.log  
# Configure Apache2  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
env APACHE_PID_FILE /var/run/apache2.pid  
env APACHE_RUN_DIR /var/run/apache2  
env APACHE_LOCK_DIR /var/lock/apache2  
  
# make www-data use the uid 1000, makes interop with perms more easy  
RUN usermod -u 1000 www-data  
  
# PORTS  
EXPOSE 80  
EXPOSE 443  
ENTRYPOINT ["/usr/sbin/apache2", "-DFOREGROUND" ]  

