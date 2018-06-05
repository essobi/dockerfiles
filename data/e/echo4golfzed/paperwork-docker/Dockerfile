# Use phusion/baseimage as base image. To make your builds reproducible, make  
# sure you lock down to a specific version, not to `latest`!  
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for  
# a list of version numbers.  
#Based on Zhukov's Paperwork Project  
#Using Phusion's Ubuntu 14.04 base image. Updated to 0.9.18.  
FROM phusion/baseimage:0.9.18  
#FROM phusion/baseimage:latest  
MAINTAINER GDGgeorge <jerry@echo4golf.com>  
  
# Set correct environment variables.  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Configure user 'nobody' to match unRAID's settings  
RUN usermod -u 99 nobody  
RUN usermod -g 100 nobody  
RUN usermod -d /home nobody  
RUN chown -R nobody:users /home  
  
# Error handler for "invoke-rc.d: policy-rc.d denied execution of start."  
RUN sed -i "s/^exit 101$/exit 0/" /usr/sbin/policy-rc.d  
  
# SSH access to the container disabled by default. Comment this to enable or
just use 'docker exec -it [paperwork container] /bin/bash' to access the
container as root if necessary.  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Install locales. Uncomment to enable others.  
# RUN locale-gen cs_CZ.UTF-8  
# RUN locale-gen de_DE.UTF-8  
RUN locale-gen en_US.UTF-8  
# RUN locale-gen es_ES.UTF-8  
# RUN locale-gen fr_FR.UTF-8  
# RUN locale-gen it_IT.UTF-8  
# RUN locale-gen pl_PL.UTF-8  
# RUN locale-gen pt_BR.UTF-8  
# RUN locale-gen ru_RU.UTF-8  
# RUN locale-gen sl_SI.UTF-8  
# RUN locale-gen uk_UA.UTF-8  
# Install and configure Paperwork dependancies  
# Add MariaDB and NodeJS repositories.  
RUN add-apt-repository 'deb http://mirror.jmu.edu/pub/mariadb/repo/5.5/ubuntu
trusty main'  
WORKDIR /tmp  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -  
  
# Install and configure packages except node-js.  
RUN apt-get install -y --allow-unauthenticated \  
libssl-dev \  
nginx \  
unzip \  
pwgen \  
git \  
wget \  
php5-cli \  
php5-common \  
php5-curl \  
php5-fpm \  
php5-tidy \  
php5-mysql \  
php5-gd \  
php5-mcrypt\  
mariadb-server  
  
#Fix MariaDB root access issue  
# RUN service mysql stop  
# RUN service mysql start ---skip-grant-tables &  
# RUN mysql -uroot -e USE mysql;  
# RUN mysql -uroot -e -i UPDATE USER SET password=PASSWORD("echo4golf") WHERE
User='root';  
# RUN service mysql restart  
# Configure php-fpm  
RUN echo "cgi.fix_pathinfo = 0" >> /etc/php5/fpm/php.ini  
RUN echo "extension=mcrypt.so" >> /etc/php5/fpm/php.ini  
RUN echo "extension=mcrypt.so" >> /etc/php5/cli/php.ini  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# Tweak my.cnf settings to set up database correctly.  
RUN sed -i -e 's#\\(bind-address.*=\\).*#\1 0.0.0.0#g' /etc/mysql/my.cnf  
RUN sed -i -e 's#\\(log_error.*=\\).*#\1 /config/databases/mysql_safe.log#g'
/etc/mysql/my.cnf  
RUN sed -i -e 's/\\(user.*=\\).*/\1 nobody/g' /etc/mysql/my.cnf  
RUN echo '[mysqld]' > /etc/mysql/conf.d/innodb_file_per_table.cnf  
RUN echo 'innodb_file_per_table' >>
/etc/mysql/conf.d/innodb_file_per_table.cnf  
  
# Now go ahead and install node-js without database access issues.  
RUN apt-get install -y --allow-unauthenticated nodejs  
  
# Setup container php and web services  
COPY www.conf /etc/php5/fpm/pool.d/www.conf  
RUN mkdir /etc/service/php5-fpm  
COPY php5-fpm.sh /etc/service/php5-fpm/run  
RUN mkdir /etc/service/nginx  
COPY nginx.sh /etc/service/nginx/run  
RUN chmod +x /etc/service/php5-fpm/run  
RUN chmod +x /etc/service/nginx/run  
  
# Install composer and setup Paperwork  
RUN curl -s https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
RUN mkdir -p /var/www/paperwork /config/databases /etc/firstrun /nginx/sites-
available/ /etc/service/mariadb /var/www/html/paperwork/frontend/app/config/  
WORKDIR /var/www  
RUN git clone https://github.com/twostairs/paperwork.git  
WORKDIR /var/www/paperwork/frontend  
RUN composer install  
RUN wget https://www.npmjs.org/install.sh  
RUN bash ./install.sh  
RUN npm install -g gulp  
RUN npm install  
RUN gulp  
COPY mariadb.sh /etc/service/mariadb/run  
COPY database.php /etc/firstrun/database.php  
COPY my.cnf /firstrun/my.cnf  
COPY firstrun.sh /etc/my_init.d/firstrun.sh  
COPY setup /var/www/html/paperwork/frontend/app/config  
RUN chown -R nobody:users /var/www/paperwork  
RUN chown -R nobody:users /config  
RUN chown -R nobody:users /var/lib/mysql  
RUN chown -R nobody:users /etc/mysql  
RUN chown -R nobody:users /var/run/mysqld  
RUN chown -R nobody:users /var/www/html/paperwork/frontend/app/  
RUN chmod +x /etc/service/mariadb/run  
RUN chmod +x /etc/my_init.d/firstrun.sh  
RUN chmod 755 -R /var/www/paperwork  
RUN chmod 755 -R /config  
RUN rm /var/www/paperwork/frontend/app/config/database.php  
  
# Configure nginx to serve Paperwork app  
COPY nginx-paperwork /etc/nginx/sites-available/default  
EXPOSE 80/tcp 3306  
VOLUME ["/config"]  
  
# # Clean up APT when done.  
# RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# sudo docker run -d -v /home/jerry/repos/data:/config -v
home/jerry/repos/data:/var/log/mysql -p 8888:80 --namepaperwork:latest  
#-->Figure out with the setup file (contains "8") goes and when.
=/var/www/html/paperwork/frontend/app/config/ =echo "8" > setup  
# PDOException: SQLSTATE[HY000] [2002] Can't connect to local MySQL server
through socket '/var/run/mysqld/mysqld.sock' (111 "Connection refused")  
# Please configure your database connection correctly, or use the sqlite
memory driver (-M). Skipping \Illuminate\Support\Facades\Password.  
# PDOException: SQLSTATE[HY000] [2002] Can't connect to local MySQL server
through socket '/var/run/mysqld/mysqld.sock' (111 "Connection refused")  
# Please configure your database connection correctly, or use the sqlite
memory driver (-M). Skipping \Illuminate\Support\Facades\Schema.  
# A new helper file was written to _ide_helper.php  
# > php artisan optimize  

