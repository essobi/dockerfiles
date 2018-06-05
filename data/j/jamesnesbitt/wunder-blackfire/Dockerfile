FROM jamesnesbitt/wunder-base  
MAINTAINER james.nesbitt@wunderkraut.com  
  
### Blackfire ----------------------------------------------------------------  
# Install the REMI repo : HOW NICE WOULD IT BE TO HAVE AN HTTPS ?!?  
RUN /usr/bin/yum install --assumeyes --verbose
http://rpms.remirepo.net/enterprise/remi-release-7.rpm  
RUN yum-config-manager --enable remi-php70  
  
# Install php-fpm  
RUN /usr/bin/yum install --assumeyes --verbose \  
php-cli php-opcache php-pdo php-mysql php-pgsql \  
php-ldap php-gd php-mbstring php-mcrypt php-xml \  
php-pecl-apcu php-pecl-yaml php-pecl-uploadprogress php-pecl-zip  
  
# Install blackfire  
RUN curl "http://packages.blackfire.io/fedora/blackfire.repo" | tee
/etc/yum.repos.d/blackfire.repo  
RUN /usr/bin/yum install --assumeyes --verbose pygpgme blackfire-php  
  
RUN /bin/mkdir -p /var/run/blackfire && \  
/bin/mkdir -p /var/log/blackfire  
  
ENTRYPOINT ["blackfire-agent"]  
CMD ["--socket", "tcp://0.0.0.0:8707", "--config", "/dev/null"]  
  
### /Blackfire ---------------------------------------------------------------  

