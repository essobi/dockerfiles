FROM clastic/php:5.6  
  
MAINTAINER Dries De Peuter <dries@nousefreak.be>  
  
##  
# Debug  
##  
  
RUN pecl install xdebug \  
&& echo "zend_extension=/usr/local/lib/php/extensions/no-debug-non-
zts-20131226/xdebug.so" >> /usr/local/etc/php/conf.d/xdebug.ini \ \  
&& echo " \  
xdebug.remote_enable = On\n \  
xdebug.remote_connect_back = On\n \  
xdebug.auto_trace = On\n \  
xdebug.idekey = docker\n \  
html_errors = On\n \  
error_reporting = E_ALL\n \  
display_errors = On\n" \  
>> /usr/local/etc/php/conf.d/debug.ini  
  
ENV PHP_IDE_CONFIG="serverName=docker"  
RUN echo "alias xdebug=\"XDEBUG_CONFIG=\\\"idekey=phpstorm
remote_host=192.168.99.1 remote_port=9000\\\"\"" >> /root/.bash_profile  

