FROM pataquets/ubuntu:bionic  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y upgrade && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
apache2 \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/  
  
# @todo: Add docker-init script and use 50-apache2-unset-home to:  
# @todo: unset HOME as done in /etc/apache2/envvars  
# Apache 'SetEnv HOME' directive seems to work (tested under PHP5.5)  
# https://httpd.apache.org/docs/2.4/mod/mod_env.html#unsetenv  
# PHP's getenv('HOME') returns an empty string if SetEnv as opposed  
# to FALSE if it is effectively unset from BASH before starting.  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_RUN_DIR /var/run  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
# https://bugs.launchpad.net/ubuntu/+source/apache2/+bug/603211  
RUN \  
mkdir -vp /var/run/apache2 && \  
mkdir -vp ${APACHE_LOG_DIR} && \  
mkdir -vp ${APACHE_LOCK_DIR} && \  
rm -v ${APACHE_LOG_DIR}/access.log && \  
ln -vs /dev/stdout ${APACHE_LOG_DIR}/access.log  
RUN \  
sed -i 's/Require local/Order Deny,Allow\n\t\tAllow from All\n\t\t#Require
local/' /etc/apache2/mods-available/status.conf  
  
EXPOSE 80 443  
  
WORKDIR /var/www/html  
  
CMD [ "apache2", "-D", "FOREGROUND", "-c", "ErrorLog /dev/stderr" ]  

