FROM library/debian:stable  
MAINTAINER Jared Scott <jtscott@gmail.com>  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
RUN apt-get update && apt-get install -y \  
curl \  
unzip \  
apache2 \  
php \  
php-mysql \  
php-curl \  
php-gd \  
php-fdomdocument \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN /usr/sbin/a2enmod mpm_prefork \  
&& /usr/sbin/a2enmod ssl \  
&& /usr/sbin/a2enmod rewrite \  
&& /usr/sbin/a2ensite default-ssl \  
&& chown -R www-data:www-data /var/www/html  
  
COPY download-pancake.sh /opt/  
RUN chmod 755 /opt/download-pancake.sh  
  
EXPOSE 80  
EXPOSE 443  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

