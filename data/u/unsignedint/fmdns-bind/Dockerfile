FROM php:5-apache  
  
WORKDIR /src  
  
RUN apt-get update \  
&& apt-get -qqy install wget bind9 dnsutils sudo \  
&& wget http://www.facilemanager.com/download/facilemanager-
complete-2.3.3.tar.gz \  
&& tar -xvf facilemanager-complete-2.3.3.tar.gz \  
&& mv facileManager/client/facileManager /usr/local \  
&& ln -s /usr/local/facileManager/www /var/www/html/fM  
  
COPY bind9/config.inc.php /usr/local/facileManager/  
COPY bind9/entrypoint.sh /  
COPY php.ini /usr/local/etc/php/  
  
ENV FACILE_MANAGER_HOST=localhost/  
ENV FACILE_MANAGER_AUTHKEY=default  
ENV FACILE_CLIENT_SERIAL_NUMBER=  
  
CMD ["apache2-foreground"]  
ENTRYPOINT ["/entrypoint.sh"]

