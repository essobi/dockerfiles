FROM php:5.6.16-apache  
# Install modules  
RUN apt-get update && apt-get install -y \  
php5-mysql \  
libmcrypt-dev \  
&& docker-php-ext-configure mbstring --enable-mbstring \  
&& docker-php-ext-install pdo_mysql mcrypt mbstring  
RUN a2enmod rewrite  
#RUN a2enmod ssl  
COPY sites-available/ /etc/apache2/sites-available/  
  
RUN a2ensite manage.unblockr.net  
#RUN a2ensite manage.unblockr.net-ssl  
#RUN apt-get install -y git  
#RUN git clone https://seaspray:B1u3b0tt13@bitbucket.org/unblockr/amember.git
/var/www/amember  
EXPOSE 80 443  

