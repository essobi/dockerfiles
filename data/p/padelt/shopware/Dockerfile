FROM ubuntu:14.04  
MAINTAINER Philipp Adelt <info@philipp.adelt.net>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get -y --no-install-recommends install git python mercurial vim less
apache2 libapache2-mod-python syslog-ng-core openssh-client unzip logrotate
cron mysql-server php5-xcache supervisor phpmyadmin apache2-utils php5-cli
pwgen php5-gd php-image-text curl php5-curl  
  
RUN rm -f /etc/cron.daily/standard  
  
RUN sed -i -E 's/^(\s*)system\\(\\);/\1unix-stream("\/dev\/log");/'
/etc/syslog-ng/syslog-ng.conf  
  
ADD files/bashrc /.bashrc  
ADD files/start.sh /start.sh  
ADD files/supervisord.conf /etc/supervisord.conf  
  
ADD files/apache-foreground.sh /etc/apache2/foreground.sh  
ADD files/apache-shopware.conf /etc/apache2/sites-available/shopware.conf  
RUN a2ensite shopware  
RUN a2dissite 000-default  
RUN a2enmod rewrite  
RUN sed --in-place "s!^Alias /phpmyadmin!#Alias /phpmyadmin!"
/etc/phpmyadmin/apache.conf  
RUN ln -s /etc/phpmyadmin/apache.conf /etc/apache2/conf-
enabled/phpmyadmin.conf  
RUN chmod +x /start.sh /etc/apache2/foreground.sh  
  
ADD
http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
/tmp/  
RUN mkdir -p /usr/local/ioncube  
WORKDIR /usr/local/  
RUN tar xvf /tmp/ioncube_loaders_lin_x86-64.tar.gz  
RUN cp ioncube/ioncube_loader_lin_5.5.so /usr/lib/php5/20121212/ioncube.so  
RUN bash -c "echo zend_extension = /usr/lib/php5/20121212/ioncube.so >
/etc/php5/apache2/conf.d/00-ioncube.ini"  
RUN bash -c "echo zend_extension = /usr/lib/php5/20121212/ioncube.so >
/etc/php5/cli/conf.d/00-ioncube.ini"  
RUN sed --in-place "s/^upload_max_filesize.*$/upload_max_filesize = 10M/"
/etc/php5/apache2/php.ini  
  
ADD
http://releases.s3.shopware.com/install_4.3.0_3194284222dda5693ef5ec2c65b5dce378213fb0.zip
/tmp/shopware_4.3.0.zip  
  
EXPOSE 80  
CMD ["/bin/bash", "/start.sh"]  

