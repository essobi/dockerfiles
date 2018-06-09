## TODO clear php build files  
## TODO remove *-dev packages after build  
  
FROM php:apache  
  
RUN apt-get update && apt-get install -y \  
git \  
libicu-dev \  
libpq-dev \  
libmcrypt-dev \  
libnotify-bin \  
&& rm -r /var/lib/apt/lists/* \  
&& docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd \  
&& docker-php-ext-install \  
intl \  
mbstring \  
mcrypt \  
pcntl \  
pdo_mysql \  
pdo_pgsql \  
pgsql \  
zip \  
opcache  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Install nodejs  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get install -y nodejs \  
&& npm update -g npm \  
&& npm install -g gulp  
  
# Get Laravel source  
RUN mkdir /tmp/app \  
&& cd /tmp/app \  
&& composer create-project "laravel/laravel=5.2.31" /tmp/app --prefer-dist  
  
COPY rootfs/ /  
  
RUN a2enmod rewrite \  
&& a2dissite 000-default \  
&& a2ensite app  
  
WORKDIR /app  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/start.sh"]

