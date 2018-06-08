# Docker-Moodle  
FROM ubuntu:latest  
LABEL maintainer="eluminare@eluhome.de"  
ADD VERSION .  
EXPOSE 80 443  
COPY moodle-config.php /var/www/html/config.php  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV MOODLE_URL http://127.0.0.1  
ADD ./foreground.sh /etc/apache2/foreground.sh  
  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get -y install mysql-client pwgen python-setuptools curl git unzip
apache2 php  
RUN apt-get -y install php-gd libapache2-mod-php postfix wget supervisor php-
pgsql libcurl3 ldap-utils iputils-ping  
RUN apt-get -y install curl  
RUN apt-get -y install libcurl3-dev php-curl php-xmlrpc php-intl php-mysql
git-core php-xml php-mbstring php-ldap php-zip php-soap cron sudo ghostscript  
RUN cd /tmp && \  
#git clone -b MOODLE_34_STABLE git://git.moodle.org/moodle.git --depth=1 && \  
#git clone -b v3.4.2 git://git.moodle.org/moodle.git && \  
git clone -b MOODLE_35_STABLE git://git.moodle.org/moodle.git && \  
mv /tmp/moodle/* /var/www/html/ && \  
rm /var/www/html/index.html && \  
git clone -b master git://github.com/fernandooliveira/moodle-
block_marking_manager.git && \  
git clone -b master https://github.com/Twoscope/moodle-
report_completionoverview.git && \  
git clone -b master https://github.com/jgramp/moodle-report_myfeedback.git  
RUN mv /tmp/moodle-block_marking_manager /var/www/html/blocks/fn_marking && \  
mv /tmp/moodle-report_completionoverview
/var/www/html/report/completionoverview && \  
mv /tmp/moodle-report_myfeedback /var/www/html/report/myfeedback  
RUN chown -R www-data:www-data /var/www/html && chmod +x
/etc/apache2/foreground.sh  
  
#cron  
#COPY moodlecron /etc/cron.d/moodlecron  
COPY moodlecron /var/spool/cron/www-data  
COPY moodlecron /var/spool/cron/root  
#RUN chmod 0644 /etc/cron.d/moodlecron  
#NEW_LINE  
RUN chown www-data.www-data /var/spool/cron/www-data  
RUN chmod 0600 /var/spool/cron/www-data  
  
# Enable SSL, moodle requires it  
RUN a2enmod ssl && a2ensite default-ssl #if using proxy dont need actually
secure connection  
  
#Change Body Max Size in php.ini  
#RUN find /etc/ -name php.ini -exec sed -i "s/post_max_size.*/post_max_size\
=\ 100M/g" {} \; -exec sed -i "s/upload_max_filesize.*/upload_max_filesize\ =\
100M/g" {} \  
RUN find /etc/ -name php.ini -exec sed -i "s/post_max_size.*/post_max_size\ =\
100M/g" {} \;  
RUN find /etc/ -name php.ini -exec sed -i
"s/upload_max_filesize.*/upload_max_filesize\ =\ 100M/g" {} \;  
  
# Cleanup, this is ran to reduce the resulting size of the image.  
#RUN apt-get clean autoclean && apt-get autoremove -y && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/* /var/lib/dpkg/* /var/lib/cache/*
/var/lib/log/*  
RUN apt-get clean autoclean && apt-get autoremove -y  
  
CMD ["/etc/apache2/foreground.sh"]  

