FROM uofa/apache2-php7-dev:shepherd  
  
RUN apt update \  
&& apt-get -y install software-properties-common apt-transport-https ca-
certificates \  
&& LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php \  
&& apt update \  
&& apt-get -y install \  
php5.6 php5.6-curl php5.6-gd php5.6-mysql php5.6-mbstring php5.6-xdebug
php5.6-xml libapache2-mod-php5.6 \  
php7.0 libapache2-mod-php7.0 php-common php-curl php-gd php-curl php-gettext
php-gd php-mysql php-memcached \  
&& a2dismod php7.0 \  
&& a2enmod php5.6 \  
&& ln -sfn /usr/bin/php5.6 /etc/alternatives/php \  
&& apt-get -y install libedit-dev \  
&& apt-get -y autoremove && apt-get -y autoclean && apt-get clean && rm -rf
/var/lib/apt/lists /tmp/* /var/tmp/*  
  
RUN echo "sendmail_path = /usr/sbin/ssmtp -t" > /etc/php/5.6/mods-
available/sendmail.ini  
  
COPY ./files/xdebug.ini /etc/php/5.6/mods-available/xdebug.ini  
COPY ./files/apache2-foreground /apache2-foreground  
RUN chmod +x /apache2-foreground  
  
RUN wget https://github.com/drush-
ops/drush/releases/download/8.1.14/drush.phar -O /usr/local/bin/drush  
  
# Configure apache modules, php modules, error logging.  
RUN phpenmod -v 5.6 -s ALL curl sendmail xdebug  

