FROM php:7.1-fpm-alpine  
  
RUN apk update && apk upgrade && apk add \--no-cache git \  
&& apk add \--no-cache libmcrypt-dev && docker-php-ext-install mcrypt \  
&& apk add \--no-cache postgresql-dev libpq && docker-php-ext-install
pdo_pgsql \  
&& apk add \--no-cache zip unzip && docker-php-ext-install zip \  
&& apk add \--no-cache libxslt-dev && docker-php-ext-install xsl dom  
  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer  
  
RUN apk add \--no-cache nodejs && npm install npm@latest -g \  
&& echo -e 'http://dl-cdn.alpinelinux.org/alpine/edge/main\nhttp://dl-
cdn.alpinelinux.org/alpine/edge/community\nhttp://dl-
cdn.alpinelinux.org/alpine/edge/testing' > /etc/apk/repositories \  
&& apk add \--no-cache yarn \  
&& yarn global add gulp  
  
RUN rm -rf /var/cache/apk/*  

