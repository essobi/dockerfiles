FROM ubuntu:14.04  
### Repositories & Keys  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10  
RUN for i in "" -updates -backports -security; do echo "deb
mirror://mirrors.ubuntu.com/mirrors.txt trusty${i} main restricted universe
multiverse"; done > /etc/apt/sources.list  
RUN apt-get update --fix-missing  
RUN apt-get -y upgrade  
  
### General system configuration  
RUN locale-gen en_US.UTF-8  
  
### SSH  
RUN apt-get install -y openssh-server  
  
RUN mkdir -p /var/run/sshd  
RUN echo 'root:schibstedpl' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
### Install nodejs and npm  
RUN apt-get install -y nodejs-legacy npm git git-core  
  
### libfontconfig1 (for PhantomJs)  
RUN apt-get install -y libfontconfig1  
  
### Imagemagick  
RUN apt-get install -y imagemagick  
  
### PhantomJS  
RUN npm install -g phantomjs  
  
### Supervisor  
RUN apt-get install -y supervisor  
  
RUN mkdir -p /var/log/supervisor  
  
ADD docker/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
### MySQL  
RUN apt-get install -y mysql-server mysql-client  
RUN mkdir -p /var/lib/mysql  
  
### PHP & Apache2  
RUN apt-get install -y apache2 zip curl git acl php5-curl php5-cli php5-json
php5-intl php5 php5-gd libapache2-mod-php5 php5-mysql libapache2-mod-fastcgi
php5-fpm  
ADD docker/apache/vhost.conf /etc/apache2/sites-enabled/000-default.conf  
ADD docker/apache/ports.conf /etc/apache2/ports.conf  
ADD docker/php-fpm/fastcgi.conf /etc/apache2/mods-enabled/fastcgi.conf  
ADD docker/php-fpm/www.conf /etc/php5/fpm/pool.d/www.conf  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
RUN a2enmod rewrite  
RUN a2enmod headers  
RUN a2enmod actions  
RUN a2enmod proxy_fcgi  
  
RUN sed -i "s/;date.timezone =/date.timezone = Europe\/Warsaw/"
/etc/php5/fpm/php.ini  
RUN sed -i "s/upload_max_filesize = .*/upload_max_filesize = 40M/"
/etc/php5/fpm/php.ini  
RUN sed -i "s/post_max_size = .*/post_max_size = 42M/" /etc/php5/fpm/php.ini  
  
### Composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/bin/composer  
  
### WP-Cli  
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar  
RUN chmod +x wp-cli.phar  
RUN mv wp-cli.phar /usr/local/bin/wp  
  
### Varnish  
RUN apt-get install -y apt-transport-https  
  
RUN curl https://repo.varnish-cache.org/ubuntu/GPG-key.txt | apt-key add -  
  
RUN echo "deb https://repo.varnish-cache.org/ubuntu/ trusty varnish-4.0" >>
/etc/apt/sources.list.d/varnish-cache.list  
  
RUN apt-get update  
  
RUN apt-get install -y varnish  
  
ADD docker/varnish/varnish /etc/default/varnish  
ADD docker/varnish/default.vcl /etc/varnish/default.vcl  
  
### RUN  
EXPOSE 22 80 8080  
CMD env | grep _ >> /etc/environment && supervisord -c
/etc/supervisor/conf.d/supervisord.conf  

