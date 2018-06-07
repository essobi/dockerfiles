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
#RUN mkdir /mnt/redcap && mkdir /mnt/redcap/var && mkdir /mnt/redcap/var/log
&& mkdir /mnt/redcap/var/log/export && chgrp adm /mnt/redcap/var/log/export &&
touch /mnt/redcap/var/log/export/cron.log && ln -s
/mnt/redcap/var/log/export/cron.log /var/log/export/cron.log  
  
RUN mkdir /mnt/redcap && mkdir /mnt/redcap/var && mkdir /mnt/redcap/var/www &&
mkdir /mnt/redcap/var/www/html && chgrp adm /mnt/redcap/var/www/html && mkdir
/var/www && ln -s /mnt/redcap/var/www/html/ /var/www/  
  
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
  
  
# Add mappable volumes  
#VOLUME ["/var/log/export" ]  
  
# Create the log file to be able to run tail  
#RUN touch /var/log/export/cron.log  
  
# Add Crontab  
RUN crontab -l | { cat; echo "* * * * * /usr/local/bin/php
/var/www/html/cron.php >> /mnt/redcap/var/log/export/cron.log 2>&1"; } |
crontab -  
  
CMD cron && tail -f /mnt/redcap/var/log/export/cron.log

