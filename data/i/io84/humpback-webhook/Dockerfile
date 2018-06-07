FROM io84/php:7.1-apache-alpine  
MAINTAINER Rushairer <rushairer@163.com>  
  
# install composer  
COPY ./resources/composer-installer composer-setup.php  
#RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
RUN php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" \  
&& php composer-setup.php --install-dir=/usr/bin --filename=composer\  
&& php -r "unlink('composer-setup.php');"  
  
ENV WEBAPP_WWW_DIR /var/www  
  
COPY ./resources/webapp $WEBAPP_WWW_DIR/webapp  
  
VOLUME $WEBAPP_WWW_DIR  
  
WORKDIR $WEBAPP_WWW_DIR  
  
# change apache2 conf  
COPY ./resources/vhosts.conf /etc/apache2/conf/vhosts.conf  
RUN echo 'Include /etc/apache2/conf/vhosts.conf' >>
/etc/apache2/conf/httpd.conf  
  
COPY ./resources/docker-humpbackwebhook-entrypoint /usr/local/bin/  
  
EXPOSE 80  
CMD ["docker-humpbackwebhook-entrypoint"]  
  

