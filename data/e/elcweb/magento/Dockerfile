FROM php:5.5-apache  
MAINTAINER Etienne Lachance <el@elcweb.ca>  
  
RUN requirements="libpng12-dev libmcrypt-dev libmcrypt4 libcurl3-dev
libfreetype6 libjpeg62-turbo libpng12-dev libfreetype6-dev libjpeg62-turbo-dev
mysql-client zlib1g-dev" \  
&& apt-get update && apt-get install -y $requirements && rm -rf
/var/lib/apt/lists/* \  
&& docker-php-ext-install mysql \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install mcrypt \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install zip \  
&& requirementsToRemove="libpng12-dev libmcrypt-dev libcurl3-dev libpng12-dev
libfreetype6-dev libjpeg62-turbo-dev" \  
&& apt-get purge --auto-remove -y $requirementsToRemove  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update \  
&& apt-get install -y ca-certificates postfix libsasl2-modules \  
&& apt-get -q clean -y \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -f /var/cache/apt/*.bin  
  
RUN usermod -u 1000 www-data  
RUN a2enmod rewrite  
RUN sed -i -e 's/\/var\/www\/html/\/var\/www\/web/' /etc/apache2/apache2.conf  
  
WORKDIR /var/www/web  
  
RUN apt-get update && apt-get install -y mysql-client-5.5 libxml2-dev  
RUN docker-php-ext-install soap  
  
VOLUME /var/www  
RUN sed -i 's/DocumentRoot \/var\/www\/html/DocumentRoot \/var\/www\/web/'
/etc/apache2/sites-available/000-default.conf  
RUN sed -i 's/DocumentRoot \/var\/www\/html/DocumentRoot \/var\/www\/web/'
/etc/apache2/sites-available/default-ssl.conf  
  
# Postfix  
ENV SMTP_ENABLE 0  
ENV SMTP_MYHOSTNAME localhost  
ENV SMTP_HOST null  
ENV SMTP_USER null  
ENV SMTP_PASSWORD null  
RUN echo 'sendmail_path="/usr/sbin/sendmail -t -i"' >>
/usr/local/etc/php/php.ini  
  
ADD entrypoint.sh /entrypoint.sh  
#ENTRYPOINT ["/entrypoint.sh"]  

