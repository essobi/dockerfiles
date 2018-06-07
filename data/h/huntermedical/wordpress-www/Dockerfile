FROM php:apache  
  
RUN apt-get update && apt-get install -y \  
mysql-client \  
libmysqlclient-dev \  
libmcrypt-dev \  
libpng12-dev \  
zlib1g-dev \  
ssmtp \  
cron \  
vim\  
&& docker-php-ext-install -j$(nproc) mcrypt \  
&& docker-php-ext-install mysqli \  
&& docker-php-ext-install zip \  
&& docker-php-ext-install -j$(nproc) gd  
  
RUN a2enmod substitute  
RUN a2enmod rewrite  
  
# Set LOG Directories  
RUN mkdir /var/log/export && chgrp adm /var/log/export  
  
RUN mkdir /mnt/wordpress && mkdir /mnt/wordpress/var && mkdir
/mnt/wordpress/var/www && mkdir /mnt/wordpress/var/www/html && chgrp adm
/mnt/wordpress/var/www/html && rmdir /var/www/html && ln -s
/mnt/wordpress/var/www/html/ /var/www/  
  
RUN mkdir /mnt/wordpress/etc && mkdir /mnt/wordpress/etc/ssmtp && chgrp adm
/mnt/wordpress/etc/ssmtp && rm /etc/ssmtp/ssmtp.conf && ln -s
/mnt/wordpress/etc/ssmtp/ssmtp.conf /etc/ssmtp/ssmtp.conf  
  
RUN mkdir /mnt/wordpress/var/wordpress_tmp && chgrp adm
/mnt/wordpress/var/wordpress_tmp && ln -s /mnt/wordpress/var/wordpress_tmp/
/var/  
  
RUN mkdir /mnt/wordpress/usr && mkdir /mnt/wordpress/usr/local && mkdir
/mnt/wordpress/usr/local/etc && mkdir /mnt/wordpress/usr/local/etc/php &&
mkdir /mnt/wordpress/usr/local/etc/php/conf.d && chgrp adm
/mnt/wordpress/usr/local/etc/php/conf.d && touch
/mnt/wordpress/usr/local/etc/php/conf.d/wordpress.ini && ln -s
/mnt/wordpress/usr/local/etc/php/conf.d/wordpress.ini
/usr/local/etc/php/conf.d/wordpress.ini  
  
# Add image configuration and scripts  
ADD start-apache2.sh /start-apache2.sh  
RUN chmod +x /*.sh  
  
EXPOSE 80  
#CMD ["/run.sh"]  

