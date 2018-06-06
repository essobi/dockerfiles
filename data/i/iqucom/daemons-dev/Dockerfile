FROM iqucom/php-daemon-container  
  
MAINTAINER mauricio.van.der.maesen@iqu.com  
  
ARG HOST_IP  
ENV HOST_IP ${HOST_IP}  
  
# Dependencies  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get autoremove -y \  
&& pecl install xdebug  
  
RUN echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name
xdebug.so)\n" >> /usr/local/etc/php/php.ini  
RUN echo "xdebug.remote_enable=1" >> /usr/local/etc/php/php.ini  
RUN echo "xdebug.remote_autostart=1" >> /usr/local/etc/php/php.ini  
RUN echo "xdebug.remote_connect_back=1" >> /usr/local/etc/php/php.ini  
RUN echo "xdebug.remote_port=9000" >> /usr/local/etc/php/php.ini  
RUN echo "xdebug.remote_handler=dbgp" >> /usr/local/etc/php/php.ini  
RUN echo "xdebug.remote_mode=req" >> /usr/local/etc/php/php.ini  
RUN echo "xdebug.idekey=PHPSTORM" >> /usr/local/etc/php/php.ini  
RUN echo "xdebug.remote_host=$HOST_IP" >> /usr/local/etc/php/php.ini  
  
## run: sed -i -- "s/{{HOST_IP}}/`ipconfig getifaddr en0`/g" docker-
environment/docker/php/*.ini  
# open port  
EXPOSE 9000

