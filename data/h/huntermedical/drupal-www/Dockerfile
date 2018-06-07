FROM php:apache  
  
RUN apt-get update && apt-get install -y \  
mysql-client \  
libmysqlclient-dev \  
libmcrypt-dev \  
libpng12-dev \  
zlib1g-dev \  
ssmtp \  
cron \  
vim \  
# && docker-php-ext-install mysql pdo pdo_mysql \  
&& docker-php-ext-install -j$(nproc) mcrypt \  
&& docker-php-ext-install mysqli \  
&& docker-php-ext-install zip \  
&& docker-php-ext-install -j$(nproc) gd  
  
# Install pdo_mysql  
RUN apt-get update \  
&& echo 'deb http://packages.dotdeb.org jessie all' >> /etc/apt/sources.list \  
&& echo 'deb-src http://packages.dotdeb.org jessie all' >>
/etc/apt/sources.list \  
&& apt-get install -y wget \  
&& wget https://www.dotdeb.org/dotdeb.gpg \  
&& apt-key add dotdeb.gpg \  
&& apt-get update \  
&& apt-get install -y php7.0-mysql \  
&& docker-php-ext-install pdo_mysql  
  
  
# Set LOG Directories  
RUN mkdir /var/log/export && chgrp adm /var/log/export  
  
RUN mkdir /mnt/drupal && mkdir /mnt/drupal/var && mkdir /mnt/drupal/var/www &&
mkdir /mnt/drupal/var/www/html && chgrp adm /mnt/drupal/var/www/html && rm -rf
/var/www/html && ln -s /mnt/drupal/var/www/html/ /var/www/  
  
RUN mkdir /mnt/drupal/etc && mkdir /mnt/drupal/etc/ssmtp && chgrp adm
/mnt/drupal/etc/ssmtp && rm /etc/ssmtp/ssmtp.conf && ln -s
/mnt/drupal/etc/ssmtp/ssmtp.conf /etc/ssmtp/ssmtp.conf  
  
#RUN mkdir /mnt/drupal/var/drupal_tmp && chgrp adm /mnt/drupal/var/drupal_tmp
&& ln -s /mnt/drupal/var/drupal_tmp/ /var/  
  
#RUN mkdir /mnt/drupal/var/drupal_edocs && chgrp adm
/mnt/drupal/var/drupal_edocs && ln -s /mnt/drupal/var/drupal_edocs/ /var/  
  
RUN mkdir /mnt/drupal/usr && mkdir /mnt/drupal/usr/local && mkdir
/mnt/drupal/usr/local/etc && mkdir /mnt/drupal/usr/local/etc/php && mkdir
/mnt/drupal/usr/local/etc/php/conf.d && chgrp adm
/mnt/drupal/usr/local/etc/php/conf.d && touch
/mnt/drupal/usr/local/etc/php/conf.d/drupal.ini && ln -s
/mnt/drupal/usr/local/etc/php/conf.d/drupal.ini
/usr/local/etc/php/conf.d/drupal.ini  
  
  
# Add image configuration and scripts  
ADD start-apache2.sh /start-apache2.sh  
RUN chmod +x /*.sh  
  
EXPOSE 80  
#CMD ["/run.sh"]  

