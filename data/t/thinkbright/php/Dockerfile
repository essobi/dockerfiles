FROM php:fpm  
MAINTAINER "Jacco Meijer" <jacco@thinkbright.nl>  
  
RUN apt-get update && apt-get install -y \  
git \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libmagickwand-dev \  
subversion \  
wget \  
gdebi-core \  
xfonts-base \  
xfonts-75dpi \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN docker-php-ext-install -j$(nproc) iconv mcrypt mysqli pdo pdo_mysql
mbstring  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& export CFLAGS="$PHP_CFLAGS" CPPFLAGS="$PHP_CPPFLAGS" LDFLAGS="$PHP_LDFLAGS"  
  
RUN pecl install imagick-3.4.3 \  
&& docker-php-ext-enable imagick  
  
# Copy imagemagick policy  
COPY ./config/imagick/policy.xml /etc/ImageMagick-6/  
  
# Install composer  
RUN (curl --fail -sS https://getcomposer.org/installer | php) && \  
chmod +x composer.phar && \  
mv composer.phar /usr/bin/composer && \  
composer -V  
  
# install wp cli using composer  
RUN composer create-project wp-cli/wp-cli:v1.3.0 /usr/share/wp-cli --no-dev &&
\  
ln -s /usr/share/wp-cli/bin/wp /usr/bin/wp && \  
ln -s /usr/share/wp-cli/bin/wp /usr/bin/wp-cli && \  
echo 'alias wp="wp --allow-root"' >> ~/.bashrc  
COPY ./wordpress/wp-cli.yml /wp-cli.yml  
  
#install wkhtmltopdf  
RUN wget -q
https://downloads.wkhtmltopdf.org/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-
jessie-amd64.deb && \  
gdebi -n wkhtmltox-0.12.2.1_linux-jessie-amd64.deb && \  
rm wkhtmltox-*  

