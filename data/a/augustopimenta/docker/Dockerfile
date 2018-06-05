FROM ubuntu:14.04  
RUN apt-get update \  
&& apt-get install -y apache2 git curl php5 php5-mcrypt php5-mysql php5-curl
php5-sybase tdsodbc php5-odbc php5-gd \  
&& apt-get autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& /usr/sbin/a2dismod 'mpm_*' && /usr/sbin/a2enmod mpm_prefork \  
&& /usr/sbin/a2enmod rewrite \  
&& /usr/sbin/a2dissite '*'  
  
COPY ports.conf /etc/apache2/ports.conf  
COPY alias.conf /etc/apache2/mods-enabled/alias.conf  
  
ADD laravel.conf /etc/apache2/sites-available/  
COPY freetds.conf /etc/freetds/freetds.conf  
  
RUN /usr/sbin/a2ensite laravel.conf \  
&& /usr/bin/curl -sS https://getcomposer.org/installer | /usr/bin/php \  
&& /bin/mv composer.phar /usr/local/bin/composer \  
&& /usr/sbin/php5enmod mcrypt  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
EXPOSE 80  
VOLUME ['/var/www']  
  
CMD /usr/sbin/apache2ctl -D FOREGROUND

