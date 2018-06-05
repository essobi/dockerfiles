FROM ubuntu:14.10  
MAINTAINER Wizacha "arnaud@wizacha.com"  
# Depots, mises a jour et installs  
RUN (apt-get update && apt-get upgrade -y -q && apt-get dist-upgrade -y -q &&
apt-get -y -q autoclean && apt-get -y -q autoremove)  
RUN apt-get install -y -q nano  
RUN apt-get install -y -q mysql-server mysql-client  
RUN apt-get install -y -q wget  
RUN wget http://in1.php.net/distributions/php-5.3.29.tar.bz2 && tar -xvf
php-5.3.29.tar.bz2  
RUN apt-get install -y -q gcc libxml2-dev make  
RUN cd php-5.3.29 && ./configure && make && make install  
RUN apt-get update  
RUN apt-get install -y -q apache2 libapache2-mod-php5  
RUN apt-get install -y -q php5-cli  
RUN apt-get install -y -q php5-mysql  
RUN apt-get install -y -q php5-gd  
RUN apt-get install -y -q php5-intl  
RUN apt-get install -y -q php5-curl  
RUN apt-get install -y -q php5-xdebug  
RUN apt-get install -y -q php-pear  
RUN apt-get install -y -q git  
RUN apt-get install -y -q mercurial  
  
#Config Php  
RUN echo "xdebug.max_nesting_level = 256" >>
/etc/php5/apache2/conf.d/xdebug.ini  
RUN echo "xdebug.remote_enable = 1" >> /etc/php5/apache2/conf.d/xdebug.ini  
RUN echo "xdebug.remote_connect_back = 1" >>
/etc/php5/apache2/conf.d/xdebug.ini  
  
# Config de Apache  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
RUN a2enmod rewrite  
RUN a2enmod ssl  
RUN a2enmod headers  
RUN a2ensite default-ssl  
RUN sed -i "11s/AllowOverride None/AllowOverride All/" /etc/apache2/sites-
enabled/000-default.conf  
RUN sed -i "4 i\<Directory /var/www/html/>\nAllowOverride All\n</Directory>\n"
/etc/apache2/sites-enabled/default-ssl.conf  
  
# Config Mysql  
RUN sed -i "s/^max_allowed_packet.*/max_allowed_packet = 500M/"
/etc/mysql/my.cnf  
RUN sed -Ei 's/^(bind-address|log)/#&/' /etc/mysql/my.cnf  
  
# installation phing  
RUN pear channel-discover pear.phing.info  
RUN pear install phing/phing  
  
#config Locale  
RUN locale-gen fr_FR.UTF-8  
ENV LANG fr_FR.UTF-8  
ENV LANGUAGE fr_FR:en  
ENV LC_ALL fr_FR.UTF-8  
#Config DB  
RUN /etc/init.d/mysql start && mysql -e "GRANT ALL ON *.* TO root@'%'
IDENTIFIED BY 'dbpassword'; GRANT ALL ON *.* TO root@localhost IDENTIFIED BY
'dbpassword'; CREATE DATABASE db;"  
  
WORKDIR /var/www/html  
EXPOSE 80  
EXPOSE 443  
EXPOSE 9000  
EXPOSE 3306  
CMD /bin/bash -c "source /etc/apache2/envvars && exec /usr/sbin/apache2 " &&
/etc/init.d/mysql start && /bin/bash

