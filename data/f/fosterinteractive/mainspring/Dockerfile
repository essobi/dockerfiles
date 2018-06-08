FROM node:8 AS node  
  
RUN npm install -g gulp-cli  
  
FROM php:7.1-cli  
  
RUN apt-get update && apt-get install -y curl git subversion openssl
zlib1g-dev libpng-dev \  
&& echo "export PATH=~/.composer/vendor/bin:\$PATH" >> ~/.bash_profile \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN echo "memory_limit=-1" > "$PHP_INI_DIR/conf.d/memory-limit.ini" \  
&& echo "date.timezone=${PHP_TIMEZONE:-UTC}" >
"$PHP_INI_DIR/conf.d/date_timezone.ini"  
  
RUN docker-php-ext-install zip gd  
  
COPY \--from=node /usr/local/bin/node /usr/local/bin/node  
COPY \--from=node /opt/yarn /opt/yarn  
COPY \--from=node /usr/local/lib/node_modules /usr/local/lib/node_modules  
RUN cd /usr/local/bin; \  
ln -sf ../lib/node_modules/npm/bin/npm-cli.js npm; \  
ln -sf ../lib/node_modules/gulp-cli/bin/gulp.js gulp; \  
ln -sf /opt/yarn/bin/yarn yarn; \  
chmod +x npm; \  
chmod +x yarn; \  
chmod +x gulp  
  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV DRUSH_VERSION 8.1.15  
ENV TERMINUS_PLUGINS_DIR /usr/local/share/terminus-plugins  
  
COPY scripts /tmp/scripts/  
  
RUN php /tmp/scripts/composer-setup --install-dir=/usr/local/bin
--filename=composer; rm -f /tmp/setup  
RUN /tmp/scripts/drush-setup  
RUN /tmp/scripts/terminus-plugins-setup  

