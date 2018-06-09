FROM mysql:5.6  
RUN apt-get update && apt-get -y install apache2 php5 libapache2-mod-php5
php5-memcached php5-curl php5-mysql memcached curl && apt-get clean && rm -rf
/var/lib/apt/lists/*  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
RUN /usr/sbin/a2ensite default-ssl  
RUN /usr/sbin/a2enmod actions  
RUN /usr/sbin/a2enmod ssl  
RUN /usr/sbin/a2enmod rewrite  
RUN /usr/sbin/a2enmod rewrite  
RUN /usr/sbin/a2dismod 'mpm_*' && /usr/sbin/a2enmod mpm_prefork  
  
EXPOSE 80  
EXPOSE 443  
EXPOSE 11211  
#COPY start.sh /usr/local/bin/  
#CMD ["start.sh"]

