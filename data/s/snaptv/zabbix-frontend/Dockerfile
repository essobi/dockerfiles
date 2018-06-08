FROM php:5.6-apache  
  
RUN curl -Lo /tmp/zabbix.tar.gz
http://repo.zabbix.com/zabbix/2.4/debian/pool/main/z/zabbix/zabbix_2.4.6.orig.tar.gz  
RUN tar -C /tmp/ -xf /tmp/zabbix.tar.gz  
RUN cp -aP /tmp/zabbix-2.4.6/frontends/php/* /var/www/html/  
RUN rm -r /tmp/*  
  
RUN apt-get update  
RUN apt-get install -y libfreetype6-dev libjpeg-dev libpng12-dev libpq-dev  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include --with-jpeg-
dir=/usr/include  
RUN docker-php-ext-install bcmath gd gettext mbstring pgsql sockets  
RUN apt-get clean  
  
RUN curl -Lo /usr/bin/confd
https://github.com/kelseyhightower/confd/releases/download/v0.10.0/confd-0.10.0-linux-
amd64  
RUN chmod +x /usr/bin/confd  
RUN mkdir -p /etc/confd/templates/  
RUN mkdir -p /etc/confd/conf.d/  
  
COPY php.ini /usr/local/etc/php/  
COPY *.toml /etc/confd/conf.d/  
COPY *.tmpl /etc/confd/templates/  
COPY entrypoint.sh /usr/bin/  
RUN chmod +x /usr/bin/entrypoint.sh  
  
CMD ["/usr/bin/entrypoint.sh"]  

