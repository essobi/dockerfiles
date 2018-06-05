######################################################  
#  
# Agave Apache PHP Base Image  
# Tag: agaveapi/api-base-images  
#  
# This is the base image for Agave's PHP APIs. It  
# builds a minimal image with apache2 + php 5.5 + composer  
#  
# with support for auto-wiring database connections,  
# CORS support, and unified logging to standard out.  
#  
# https://bitbucket.org/agaveapi/php-api-base  
# http://agaveapi.co  
#  
######################################################  
FROM agaveapi/httpd:2.4  
MAINTAINER Rion Dooley <dooley@tacc.utexas.edu  
  
ADD tcp/limits.conf /etc/security/limits.conf  
ADD tcp/sysctl.conf /etc/sysctl.conf  
  
# RUN /usr/sbin/deluser apache && \  
# addgroup -g 50 -S apache && \  
# adduser -u 1000 -g apache -G apache -S apache && \  
RUN \  
echo "Installing php and dependencies..." && \  
apk --update add apache2-ssl apache2-proxy php-apache2 curl php-cli php-json
php-phar php-openssl php-mysql php-pdo php-zip php-curl php-mysqli php-gd php-
iconv php-zlib php-ctype php-xml php-dom php-opcache php-mcrypt php-pdo_mysql
vim curl gzip ssmtp && \  
rm -f /var/cache/apk/* && \  
#  
# # Set up system timezone and ntpd  
# echo "Setting system timezone to America/Chicago..." && \  
# ln -snf /usr/share/zoneinfo/America/Chicago /etc/localtime && \  
# echo "Setting up ntpd..." && \  
# echo $(setup-ntp -c busybox 2>&1) && \  
# ntpd -d -p pool.ntp.org && \  
  
echo "Installing and configuring ssmtp..." && \  
# Parameterize SSMTP mail so php mail will work out of the box using the
environment variables provided at runtiem  
sed -ri -e 's/^(mailhub=).*/\1%%SMTP_HUB%%/' -e 's/^#(FromLineOverride)/\1/'
/etc/ssmtp/ssmtp.conf && \  
{ \  
echo "AuthUser=%%SMTP_USER%%"; \  
echo "AuthPass=%%SMTP_PASSWORD%%"; \  
echo "UseSTARTTLS=YES"; \  
} >> /etc/ssmtp/ssmtp.conf && \  
  
echo "Installing and configuring opcache..." && \  
# Configure PHP opcache  
{ \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=60'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /etc/php/conf.d/opcache-recommended.ini && \  
  
# Install PHP Composer  
echo "Installing composer..." && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
  
# Updating apache defaults for php  
sed -i 's#DirectoryIndex index.html#DirectoryIndex index.php index.html#'
/etc/apache2/httpd.conf && \  
echo "<?php phpinfo(); ?>" > /var/www/html/index.php && \  
  
# Add custom log format with unique id passed in all agave sessions  
sed -i 's#LogFormat "%h#LogFormat "[%{UNIQUE_ID}i] %{CONTAINER_STACK}e %h#g'
/etc/apache2/httpd.conf  
  
  
# Uncomment for bind util with host, dig, etc ~140MB  
#RUN apk add -U alpine-sdk linux-headers \  
# && curl ftp://ftp.isc.org/isc/bind9/9.10.2/bind-9.10.2.tar.gz|tar -xzv \  
# && cd bind-9.10.2 \  
# && CFLAGS="-static" ./configure --without-openssl --disable-symtable \  
# && make \  
# && cp ./bin/dig/dig /usr/bin/ \  
# && apk del build-base alpine-sdk linux-headers \  
# && rm -rf bind-9.10.2 \  
# && rm /var/cache/apk/*  
# Uncomment for newrelic support...should install logrotate as well or disable
logging.  
# RUN curl -sk -O
http://download.newrelic.com/php_agent/archive/5.1.0.129/newrelic-
php5-5.1.0.129-linux.tar.gz && \  
# gunzip -dc newrelic-php5-5.1.0.129-linux.tar.gz | tar xf - && \  
# cd newrelic-php5-5.1.0.129-linux && \  
# ls && \  
# chmod +x ./newrelic-install && \  
# sysctl -p && \  
# newrelic-install install  
ADD php/php.ini /etc/php/php.ini  
ADD docker_entrypoint.sh /docker_entrypoint.sh  
  
WORKDIR /var/www/html  
  
VOLUME [ "/var/www/html" ]  
  
EXPOSE 80 443  
ENTRYPOINT ["/docker_entrypoint.sh"]  
  
CMD ["httpd", "-DFOREGROUND"]  

