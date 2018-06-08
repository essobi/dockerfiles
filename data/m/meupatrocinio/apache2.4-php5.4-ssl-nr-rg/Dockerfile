FROM centos  
MAINTAINER Rafael Bernardo <rafael@faztodadiferenca.com.br>  
  
  
# Install New Relic Repo  
RUN rpm -Uvh https://yum.newrelic.com/pub/newrelic/el5/x86_64/newrelic-
repo-5-3.noarch.rpm  
  
# Railgun Repo  
RUN rpm -ivh http://pkg.cloudflare.com/cloudflare-release-latest.el7.rpm  
  
RUN yum -y update && yum install -y \  
httpd \  
cronie\  
gcc \  
php-pear \  
php-devel \  
make \  
openssl-devel \  
git \  
which \  
ca-certificates \  
httpd \  
postfix \  
php \  
php-common \  
php-dba \  
php-gd \  
php-intl \  
php-ldap \  
php-mbstring \  
php-mysqlnd \  
php-odbc \  
php-pdo \  
php-pecl-memcache \  
php-pgsql \  
php-pspell \  
php-recode \  
php-snmp \  
php-soap \  
php-xml \  
php-xmlrpc \  
mod_ssl \  
newrelic-php5 \  
newrelic-sysmond \  
railgun-stable \  
&& yum clean all  
  
#Railgun Script + mod http_cloudflare  
RUN rpm -ivh
https://www.cloudflare.com/static/misc/mod_cloudflare/centos/mod_cloudflare-
el7-x86_64.latest.rpm  
ADD railgun.sh /bin/  
RUN chmod +x /bin/railgun.sh  
  
RUN sh -c 'echo short_open_tag=On >> /etc/php.ini'  
  
ENV LOG_STDOUT **Boolean**  
ENV LOG_STDERR **Boolean**  
ENV LOG_LEVEL warn  
ENV ALLOW_OVERRIDE All  
ENV DATE_TIMEZONE UTC  
  
COPY run-lap.sh /usr/sbin/  
RUN chmod +x /usr/sbin/run-lap.sh  
  
# Setup environment variables for initializing New Relic  
ENV NR_INSTALL_SILENT 1  
ENV NR_INSTALL_KEY **ChangeMe**  
ENV NR_APP_NAME "Default App Name"  
# Setup SSL  
RUN mkdir -p /etc/httpd/sites-enabled/  
RUN echo "IncludeOptional sites-enabled/*.conf" >> /etc/httpd/conf/httpd.conf  
  
VOLUME /etc/httpd/sites-enabled/  
  
# Apache and Railgun on the same server, so:  
RUN echo "CloudFlareRemoteIPTrustedProxy 127.0.0.1" >>
/etc/httpd/conf/httpd.conf  
  
EXPOSE 80  
EXPOSE 443  
EXPOSE 2408  
CMD ["/usr/sbin/run-lap.sh"]  

