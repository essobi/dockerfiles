FROM php:cli  
  
# Download packages  
RUN apt-get update && apt-get install -y \  
mysql-client \  
libmysqlclient-dev \  
libmcrypt-dev \  
libpng12-dev \  
zlib1g-dev \  
ssmtp \  
cron \  
vim \  
tzdata \  
&& docker-php-ext-install -j$(nproc) mcrypt \  
&& docker-php-ext-install mysqli \  
&& docker-php-ext-install zip \  
&& docker-php-ext-install -j$(nproc) gd  
  
  
  
# Set LOG Directories  
#RUN mkdir /mnt/drupal && mkdir /mnt/drupal/var && mkdir /mnt/drupal/var/log
&& mkdir /mnt/drupal/var/log/export && chgrp adm /mnt/drupal/var/log/export &&
touch /mnt/drupal/var/log/export/cron.log && ln -s
/mnt/drupal/var/log/export/cron.log /var/log/export/cron.log  
  
RUN mkdir /mnt/drupal && mkdir /mnt/drupal/var && mkdir /mnt/drupal/var/www &&
mkdir /mnt/drupal/var/www/html && chgrp adm /mnt/drupal/var/www/html && mkdir
/var/www && ln -s /mnt/drupal/var/www/html/ /var/www/  
  
RUN mkdir /mnt/drupal/etc && mkdir /mnt/drupal/etc/ssmtp && chgrp adm
/mnt/drupal/etc/ssmtp && rm /etc/ssmtp/ssmtp.conf && ln -s
/mnt/drupal/etc/ssmtp/ssmtp.conf /etc/ssmtp/ssmtp.conf  
  
RUN mkdir /mnt/drupal/var/drupal_tmp && chgrp adm /mnt/drupal/var/drupal_tmp
&& ln -s /mnt/drupal/var/drupal_tmp/ /var/  
  
RUN mkdir /mnt/drupal/var/drupal_edocs && chgrp adm
/mnt/drupal/var/drupal_edocs && ln -s /mnt/drupal/var/drupal_edocs/ /var/  
  
RUN mkdir /mnt/drupal/usr && mkdir /mnt/drupal/usr/local && mkdir
/mnt/drupal/usr/local/etc && mkdir /mnt/drupal/usr/local/etc/php && mkdir
/mnt/drupal/usr/local/etc/php/conf.d && chgrp adm
/mnt/drupal/usr/local/etc/php/conf.d && touch
/mnt/drupal/usr/local/etc/php/conf.d/drupal.ini && ln -s
/mnt/drupal/usr/local/etc/php/conf.d/drupal.ini
/usr/local/etc/php/conf.d/drupal.ini  
  
  
# Add Crontab  
#RUN crontab -l | { cat; echo "* * * * * root .
/root/.profile;/usr/local/bin/php /var/www/html/cron.php >>
/var/log/export/cron.log 2>&1"; } | crontab -  
RUN crontab -l | { cat; echo "* * * * * /usr/local/bin/php
/var/www/html/cron.php >> /mnt/redcap/var/log/export/cron.log 2>&1"; } |
crontab -  
  
CMD cron && tail -f /mnt/drupal/var/log/export/cron.log

