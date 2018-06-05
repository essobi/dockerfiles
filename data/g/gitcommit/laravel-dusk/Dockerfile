FROM phpdockerio/php71-fpm:latest  
  
RUN apt-get update \  
&& apt-get -y --no-install-recommends install php7.1-memcached php7.1-mysql
php7.1-imagick php7.1-mbstring php7.1-gd php7.1-zip php7.1-xml php7.1-mcrypt
php7.1-bcmath \  
&& apt-get install -y git wget curl chromium-browser \  
&& apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/doc/*  
  
# Laravel Dusk  
RUN google-chrome &  
  
# check installed modules  
RUN php -m  
  
# install node and npm  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && apt-get install
-y nodejs && \  
nodejs --version  
  
# Install yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update && apt-get install -y yarn  
  
# add node and npm to path so the commands are available  
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH  
  
# Install Composer Package manager  
ENV COMPOSER_ALLOW_SUPERUSER 1  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
&& php composer-setup.php \  
php -r "unlink('composer-setup.php');" && mv composer.phar
/usr/local/bin/composer  
  
# confirm installed versions  
RUN node -v  
RUN npm -v  
RUN php -v  
RUN yarn -v  
RUN chromium-browser --version  
RUN composer --version  
RUN php -m  

