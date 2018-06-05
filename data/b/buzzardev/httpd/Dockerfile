FROM httpd:2.4  
MAINTAINER Bart Reunes "@MetalArend"  
# Possible LOG_LEVEL values include: trace8..1, debug, info, notice, warn,
error, crit, alert, emerg  
ENV PHP_HOST="php-fpm" \  
PHP_PORT="9000" \  
APACHE_HOST="*" \  
APACHE_PORT="80" \  
SERVER_NAME="www.example.com:80" \  
SERVER_ADMIN="you@example.com" \  
LOG_LEVEL="warn" \  
ERROR_LOG="/proc/self/fd/2" \  
CUSTOM_LOG="/proc/self/fd/2" \  
DOCUMENT_ROOT="/usr/local/apache2/htdocs"  
# To customize the configuration of the httpd server, just COPY your custom
configuration in as /usr/local/apache2/conf/httpd.conf  
ADD ./httpd.conf /usr/local/apache2/conf/httpd.conf  
  
EXPOSE 80  
  
# If you want to run your web traffic over SSL, the simplest setup is to COPY
or mount (-v) your server.crt and server.key into /usr/local/apache2/conf/ and
then customize the /usr/local/apache2/conf/httpd.conf by removing the comment
from the line with #Include conf/extra/httpd-ssl.conf.  
# http://www.akadia.com/services/ssh_test_certificate.html  
# EXPOSE 443  

