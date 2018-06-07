FROM circleci/php:5.6  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 7.4.0  
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -  
RUN sudo apt-get install libxml2-dev libzip-dev libwebp-dev libjpeg-dev
libpng-dev libz-dev libxpm-dev libmcrypt-dev libssl-dev mysql-client libicu-
dev nodejs  
RUN sudo pecl channel-update pecl.php.net  
RUN sudo pecl install zip && sudo docker-php-ext-enable zip  
RUN sudo pecl install mongo && sudo docker-php-ext-enable mongo  
RUN sudo docker-php-ext-install bcmath && sudo docker-php-ext-enable bcmath  
RUN sudo docker-php-ext-install mcrypt && sudo docker-php-ext-enable mcrypt  
RUN sudo docker-php-ext-install mysqli && sudo docker-php-ext-enable mysqli  
RUN sudo docker-php-ext-install pdo_mysql && sudo docker-php-ext-enable
pdo_mysql  
RUN sudo docker-php-ext-install soap && sudo docker-php-ext-enable soap  
RUN sudo docker-php-ext-install intl && sudo docker-php-ext-enable intl  
RUN sudo docker-php-ext-enable xdebug  
RUN echo "[PHP]\\\ndate.timezone=UTC" | sudo tee -a
/usr/local/etc/php/conf.d/tzone.ini  
RUN sudo npm install -g junit-merge  
CMD ["/bin/sh"]  

