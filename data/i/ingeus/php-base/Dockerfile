FROM php:5.6-apache  
MAINTAINER Stephen Masters <steve@scattercode.co.uk>  
  
COPY policy-rc.d /usr/sbin/policy-rc.d  
  
RUN apt-get update  
RUN apt-get install -y supervisor php5-gd php5-ldap php5-imap libpng12-dev
libjpeg-dev zlib1g-dev unzip nano  
RUN rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd pdo pdo_mysql mbstring zip  
RUN apt-get clean  
  
RUN php5enmod imap  
RUN php5enmod ldap  
  
RUN a2enmod rewrite  
  
WORKDIR /var/www  
  
RUN a2ensite 000-default  
  
COPY run.sh /run.sh  
COPY start-apache2.sh /start-apache2.sh  
COPY supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf  
  
EXPOSE 80  
CMD ["/run.sh"]  

