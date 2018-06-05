FROM debian:jessie  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
echo "export TERM=xterm" >> /root/.bashrc  
  
RUN apt-get update && apt-get -y install vim apache2 php5 zip mysql-client
php5-mcrypt php5-mhash php5-gd php5-xsl php5-curl php5-xmlrpc php-soap
php5-mysql php5-memcached php5-redis php5-intl  
  
ENV DEFAULT_PHP_MODS=  
ENV DEFAULT_LIB_DEPENDENCIES=  
ENV DEFAULT_APACHE_MODS=rewrite;ssl;headers  
  
COPY conf_default /var/conf_default  
COPY conf /var/conf_tmp  
  
ADD install_and_run.sh /tmp/install_and_run.sh  
RUN chmod +x /tmp/install_and_run.sh  
  
RUN rm -rf /var/conf && mkdir -p /var/conf  
  
ENV PHP_INI_SCAN_DIR=/etc/php5/apache2/conf.d:/var/conf  
  
WORKDIR /var/www/html  
  
VOLUME /var/www/html  
VOLUME /var/conf  
  
EXPOSE 80  
ENTRYPOINT ["/tmp/install_and_run.sh"]  
# CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

