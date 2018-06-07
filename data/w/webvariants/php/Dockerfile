FROM php:7.2-apache  
  
MAINTAINER Martin Schnabel <martin@webvariants.de>  
  
ENV WEB_ROOT /app  
  
RUN sed -i "s|/var/www/html|\$\{WEB_ROOT\}|" /etc/apache2/apache2.conf \  
&& sed -i "s|/var/www|\$\{WEB_ROOT\}|" /etc/apache2/apache2.conf \  
&& sed -i "s|/var/www/html|\$\{WEB_ROOT\}|" /etc/apache2/sites-
enabled/000-default.conf \  
&& { \  
echo 'ServerName localhost'; \  
echo '<Directory ${WEB_ROOT}/>'; \  
echo ' Options Indexes FollowSymLinks'; \  
echo ' AllowOverride All'; \  
echo ' Require all granted'; \  
echo '</Directory>'; \  
} >> /etc/apache2/sites-enabled/000-default.conf \  
\  
&& echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup \  
&& echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache \  
&& apt-get update && apt-get install -y gnupg2 \  
&& curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
\  
&& apt-get install -y \  
nodejs \  
nano \  
locales \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libcurl4-openssl-dev \  
libpng16-16 \  
libpng-dev \  
libxslt1.1 \  
libxslt1-dev \  
libxml2-dev \  
libicu57 \  
icu-devtools \  
libicu-dev \  
libtidy5 \  
libtidy-dev \  
zlib1g-dev \  
libxml2-dev \  
curl \  
graphicsmagick \  
msmtp \  
git \  
mercurial \  
postgresql-client-common \  
postgresql-server-dev-all \  
libsqlite3-dev \  
libssl-dev \  
\  
&& npm install --quiet -g npm \  
&& npm install --quiet -g grunt-cli bower \  
&& npm cache clean --force \  
\  
&& a2enmod rewrite headers expires \  
\  
&& echo "de_DE.UTF-8 UTF-8" >> /etc/locale.gen \  
&& echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \  
&& echo "en_GB.UTF-8 UTF-8" >> /etc/locale.gen \  
&& echo "fr_FR.UTF-8 UTF-8" >> /etc/locale.gen \  
&& echo "it_IT.UTF-8 UTF-8" >> /etc/locale.gen \  
&& echo "nl_NL.UTF-8 UTF-8" >> /etc/locale.gen \  
&& locale-gen \  
&& /usr/sbin/update-locale LANG=en_US.UTF-8 \  
\  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
\  
&& MAKEFLAGS="-j$(nproc)" pecl install mongodb \  
&& echo "extension=mongodb.so" > /usr/local/etc/php/conf.d/mongodb.ini \  
\  
&& MAKEFLAGS="-j$(nproc)" pecl install apcu \  
&& echo "extension=apcu.so" > /usr/local/etc/php/conf.d/apcu.ini \  
\  
&& docker-php-ext-install -j$(nproc) \  
opcache \  
tidy \  
iconv \  
curl \  
zip \  
mbstring \  
intl \  
xmlrpc \  
xsl \  
gd \  
pdo_mysql \  
pdo_pgsql \  
pdo_sqlite \  
mysqli \  
soap \  
\  
&& apt-get remove -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libcurl4-openssl-dev \  
libpng-dev \  
libxslt1-dev \  
libxml2-dev \  
libicu-dev \  
libtidy-dev \  
zlib1g-dev \  
libxml2-dev \  
libssl-dev \  
\  
&& php -r "readfile('https://getcomposer.org/installer');" > /bin/composer-
setup.php && php /bin/composer-setup.php --install-dir=/bin \  
&& ln -s /bin/composer.phar /bin/composer \  
\  
&& rm -r /usr/share/doc \  
&& rm -r /var/lib/apt/lists/*  
  
COPY apache2-foreground-user /usr/local/bin/  
  
WORKDIR /app  
  
CMD ["apache2-foreground-user"]  
  
# VOLUME /app/data  

