FROM pinedamg/apache-php  
MAINTAINER MPineda <pinedamg@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
#INSTALL COMPOSER  
RUN /usr/bin/curl -sS https://getcomposer.org/installer |/usr/bin/php  
RUN /bin/mv composer.phar /usr/local/bin/composer  
  
#INSTALL LARAVEL  
RUN /usr/local/bin/composer global require "laravel/installer"  
RUN ln -s /root/.composer/vendor/laravel/installer /usr/local/bin/laravel  
  
#INSTALL NODE AND EXTENSIONS  
RUN /usr/bin/curl -sL https://deb.nodesource.com/setup_7.x | bash -  
RUN apt-get install -y nodejs  
  
#NODEJS INSTALL BOWER GULP  
RUN npm install --global gulp  
RUN npm install --global bower  
RUN export DISABLE_NOTIFIER=true  
  
#INSTALL LARAVEL COMMAND  
RUN composer global require "laravel/installer"  
  
#INSTALL LARAVEL MIX  
RUN node -v  
RUN npm -v  
RUN npm install  
  
#ADD LARAVEL RECOMMEND SETTINGS  
COPY zz-laravel.ini /etc/php5/mods-available/zz-laravel.ini  
RUN php5enmod laravel  
  
#ADD LARAVEL ALIASES  
COPY ./aliases /root/aliases  
RUN cat /root/aliases >> /root/.bash_aliases && rm -f /root/aliases  
  
#ADD VIRTUALHOST  
COPY vhost.conf /etc/apache2/sites-enabled/000-default.conf  
COPY vhost.conf /etc/apache2/sites-available/000-default.conf  
  
RUN apt-get update && apt-get -y autoremove && apt-get clean && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /var/www

