FROM uofa/apache2-php7  
  
# Upgrade all currently installed packages and install web server packages.  
RUN apt update \  
&& apt-get -y install apache2 php7.0-common libapache2-mod-php7.0 php-apcu
php7.0-curl php7.0-gd php7.0-ldap php7.0-mysql php7.0-opcache php7.0-mbstring
php7.0-bcmath php7.0-xml libedit-dev ssmtp \  
&& apt-get -y install php7.0 php7.0-cli php-xdebug php-memcached libedit-dev
tig vim wget curl ssh git-flow silversearcher-ag mysql-client netcat-openbsd
pv ruby rubygems-integration nodejs nodejs-legacy sudo zip ssmtp python \  
&& apt-get -y install mariadb-server mariadb-common supervisor \  
&& apt-get -y autoremove && apt-get -y autoclean && apt-get clean && rm -rf
/var/lib/apt/lists /tmp/* /var/tmp/*  
  
# PHP config  
COPY ./files/php.ini /etc/php/7.0/mods-available/ua.ini  
COPY ./files/supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-
apache2.conf  
COPY ./files/supervisord-mysqld.conf /etc/supervisor/conf.d/supervisord-
mysqld.conf  
COPY ./files/mysqld-foreground /usr/local/bin/mysqld-foreground  
COPY ./files/run.sh /run.sh  
COPY ./files/my.cnf /etc/mysql/conf.d/ua.cnf  
COPY ./files/create_mysql_user.sh /usr/local/bin/create_mysql_user.sh  
  
# Install robo  
RUN wget -O /usr/local/bin/robo http://robo.li/robo.phar && chmod +x
/usr/local/bin/robo \  
&& wget -q https://getcomposer.org/installer -O - | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& wget https://drupalconsole.com/installer -O /usr/local/bin/drupal && chmod
+x /usr/local/bin/drupal && /usr/local/bin/drupal init \  
&& ln -s /code/vendor/drush/drush/drush /usr/local/bin/drush  
  
# Setup local mysql alias  
RUN echo "127.0.0.1 mysql" >> /etc/hosts  
  
WORKDIR /web  
  
CMD ["/run.sh"]  

