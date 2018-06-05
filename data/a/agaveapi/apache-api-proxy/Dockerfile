######################################################  
#  
# Agave API Proxy  
# Tag: agaveapi/apache-api-proxy  
#  
# This is the HTTP proxy used to access the Agave core  
# science APIs. It contains a minimal Apache2 server  
# with SSL support on top of an Alpine 3.2 base image.  
# The Apache configuration has the necessary rewrite  
# and proxy rules to expose the core science APIs by  
# default. CORS support is built in. Logging goes to  
# /var/log/apache2, which is an exposed volume.  
#  
# https://bitbucket.org/agaveapi/apache-api-proxy  
# http://agaveapi.co  
#  
######################################################  
  
FROM alpine:3.2  
MAINTAINER Rion Dooley <dooley@tacc.utexas.edu  
  
ADD tcp/limits.conf /etc/security/limits.conf  
ADD tcp/sysctl.conf /etc/sysctl.conf  
  
RUN /usr/sbin/deluser apache && \  
addgroup -g 50 -S apache && \  
adduser -u 1000 -g apache -G apache -S apache && \  
apk --update add apache2-ssl apache2-proxy vim gzip tzdata bash && \  
rm -f /var/cache/apk/* && \  
echo "Setting system timezone to America/Chicago..." && \  
ln -snf /usr/share/zoneinfo/America/Chicago /etc/localtime && \  
echo "Setting up ntpd..." && \  
echo $(setup-ntp -c busybox 2>&1) && \  
ntpd -d -p pool.ntp.org && \  
echo "Installing composer..." && \  
mkdir /var/www/html && \  
chown -R apache:apache /var/www/html  
  
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
  
ADD apache/httpd.conf /etc/apache2/httpd.conf  
ADD apache/ssl.conf /etc/apache2/conf.d/ssl.conf  
ADD docker_entrypoint.sh /docker_entrypoint.sh  
  
WORKDIR /var/www/html  
  
VOLUME [ "/var/www/html" ]  
VOLUME [ "/var/log/newrelic" ]  
  
EXPOSE 80 443  
  
ENTRYPOINT ["/docker_entrypoint.sh"]  
  
CMD ["/usr/sbin/apachectl", "-DFOREGROUND"]  

