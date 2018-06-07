FROM ubuntu:16.04  
MAINTAINER khanhicetea@gmail.com  
  
RUN apt-get clean && apt-get -y update && apt-get install -y locales curl
software-properties-common git \  
&& locale-gen en_US.UTF-8  
RUN LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php  
RUN apt-get update  
RUN apt-get install -y php7.2-bcmath php7.2-bz2 php7.2-cli php7.2-common
php7.2-curl \  
php7.2-cgi php7.2-dev php7.2-fpm php7.2-gd php7.2-gmp php7.2-imap php7.2-intl
\  
php7.2-json php7.2-ldap php7.2-mbstring php7.2-mysql \  
php7.2-odbc php7.2-opcache php7.2-pgsql php7.2-phpdbg php7.2-pspell \  
php7.2-readline php7.2-recode php7.2-soap php7.2-sqlite3 \  
php7.2-tidy php7.2-xml php7.2-xmlrpc php7.2-xsl php7.2-zip \  
php-tideways php-mongodb  
  
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/"
/etc/php/7.2/cli/php.ini  
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/"
/etc/php/7.2/fpm/php.ini  
RUN sed -i "s/display_errors = Off/display_errors = On/"
/etc/php/7.2/fpm/php.ini  
RUN sed -i "s/upload_max_filesize = .*/upload_max_filesize = 10M/"
/etc/php/7.2/fpm/php.ini  
RUN sed -i "s/post_max_size = .*/post_max_size = 12M/"
/etc/php/7.2/fpm/php.ini  
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/"
/etc/php/7.2/fpm/php.ini  
  
RUN sed -i -e "s/pid =.*/pid = \/var\/run\/php7.2-fpm.pid/"
/etc/php/7.2/fpm/php-fpm.conf  
RUN sed -i -e "s/error_log =.*/error_log = \/proc\/self\/fd\/2/"
/etc/php/7.2/fpm/php-fpm.conf  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.2/fpm/php-
fpm.conf  
RUN sed -i "s/listen = .*/listen = 9000/" /etc/php/7.2/fpm/pool.d/www.conf  
RUN sed -i "s/;catch_workers_output = .*/catch_workers_output = yes/"
/etc/php/7.2/fpm/pool.d/www.conf  
  
RUN curl https://getcomposer.org/installer > composer-setup.php && php
composer-setup.php && mv composer.phar /usr/local/bin/composer && rm composer-
setup.php  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 9000  
CMD ["php-fpm7.2"]  

