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
  
  
# Set LOG Directories  
RUN mkdir /var/log/export && chgrp adm /var/log/export  
  
RUN mkdir /mnt/redcap && mkdir /mnt/redcap/var && mkdir /mnt/redcap/var/www &&
mkdir /mnt/redcap/var/www/html && chgrp adm /mnt/redcap/var/www/html && rmdir
/var/www/html && ln -s /mnt/redcap/var/www/html/ /var/www/  
  
RUN mkdir /mnt/redcap/etc && mkdir /mnt/redcap/etc/ssmtp && chgrp adm
/mnt/redcap/etc/ssmtp && rm /etc/ssmtp/ssmtp.conf && ln -s
/mnt/redcap/etc/ssmtp/ssmtp.conf /etc/ssmtp/ssmtp.conf  
  
RUN mkdir /mnt/redcap/var/redcap_tmp && chgrp adm /mnt/redcap/var/redcap_tmp
&& ln -s /mnt/redcap/var/redcap_tmp/ /var/  
  
RUN mkdir /mnt/redcap/var/redcap_edocs && chgrp adm
/mnt/redcap/var/redcap_edocs && ln -s /mnt/redcap/var/redcap_edocs/ /var/  
  
RUN mkdir /mnt/redcap/usr && mkdir /mnt/redcap/usr/local && mkdir
/mnt/redcap/usr/local/etc && mkdir /mnt/redcap/usr/local/etc/php && mkdir
/mnt/redcap/usr/local/etc/php/conf.d && chgrp adm
/mnt/redcap/usr/local/etc/php/conf.d && touch
/mnt/redcap/usr/local/etc/php/conf.d/redcap.ini && ln -s
/mnt/redcap/usr/local/etc/php/conf.d/redcap.ini
/usr/local/etc/php/conf.d/redcap.ini  
  
# Add image configuration and scripts  
ADD start-apache2.sh /start-apache2.sh  
RUN chmod +x /*.sh  
  
EXPOSE 80  
#CMD ["/run.sh"]  

