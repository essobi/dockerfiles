FROM former03/dev03-debian-squeeze  
MAINTAINER Christian Simon <simon@swine.de>  
# Install FORMER 03 Apt  
ADD ./former03.list /etc/apt/sources.list.d/former03.list  
ADD ./former03.gpg /tmp/former03.gpg  
RUN apt-key add /tmp/former03.gpg  
RUN apt-get update  
# Install apache fastcgi php base  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install imagemagick
graphicsmagick mysql-server phpmyadmin apache2 libapache2-mod-fcgid
libapache2-mod-php5 php5-cgi makedev supervisor  
# Run apache as devel user  
RUN sed -i 's/www-data/devel/g' /etc/apache2/envvars  
RUN chown -R -c --from www-data:www-data devel:devel /var/lib/apache2/fcgid  
# Config Apache vHost  
ADD ./apache.default.conf /etc/apache2/sites-available/default  
# Don't use mod-php as default  
RUN echo "" > /etc/apache2/mods-available/php5.conf  
# Enable some modules  
RUN a2enmod rewrite; a2enmod headers; a2enmod fcgid  
# Install php fcgid starter  
ADD ./apache_php_fcgid.sh /etc/apache2/apache_php_fcgid.sh  
RUN chmod 755 /etc/apache2/apache_php_fcgid.sh  
# Enable phpmyadmin  
RUN ln -s ../../phpmyadmin/apache.conf /etc/apache2/conf.d/phpmyadmin  
# Config phpmyadmin  
ADD ./phpmyadmin.config.inc.php /usr/share/phpmyadmin/config.inc.php  
# Init phpmyadmin tables  
RUN /etc/init.d/mysql start && mysqladmin create phpmyadmin && zcat
/usr/share/doc/phpmyadmin/examples/create_tables.sql.gz | mysql phpmyadmin  
# Set mysql server password  
RUN /etc/init.d/mysql start; mysqladmin -u root password dev03  
# Setup default page  
RUN mkdir -p /devel/workspace && echo "<?php phpinfo() ?>" >
/devel/workspace/index.php  
# Link /var/www to /devel/workspace  
RUN rm -r /var/www && ln -s ../devel/workspace /var/www  
# Copy run.sh and supervisor config  
ADD ./run.sh /run.sh  
ADD ./apache.foreground.sh /etc/apache2/foreground.sh  
ADD ./supervisord.apache.conf /etc/supervisor/conf.d/apache.conf  
ADD ./supervisord.mysql.conf /etc/supervisor/conf.d/mysql.conf  
# CMD TO RUN  
CMD /run.sh  
# PORT TO EXPOSE  
EXPOSE 80  

