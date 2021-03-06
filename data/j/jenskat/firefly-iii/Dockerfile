FROM php:7-apache  
  
RUN apt-get update -y && \  
apt-get install -y --no-install-recommends libcurl4-openssl-dev \  
zlib1g-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
libicu-dev \  
libmcrypt-dev \  
libedit-dev \  
libtidy-dev \  
libxml2-dev \  
libsqlite3-dev \  
libpq-dev \  
libbz2-dev \  
gettext-base \  
locales && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN docker-php-ext-install -j$(nproc) curl gd intl json mcrypt readline tidy
zip bcmath xml mbstring pdo_sqlite pdo_mysql bz2 pdo_pgsql  
  
# Generate locales supported by firefly  
RUN echo "en_US.UTF-8 UTF-8\nde_DE.UTF-8 UTF-8\nnl_NL.UTF-8 UTF-8\npt_BR.UTF-8
UTF-8" > /etc/locale.gen && locale-gen  
  
COPY docker/apache2.conf /etc/apache2/apache2.conf  
# Enable apache mod rewrite..  
RUN a2enmod rewrite  
  
# Setup the Composer installer  
run curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN cd /var/www && composer create-project grumpydictator/firefly-iii --no-dev
--prefer-dist firefly-iii 4.6.4  
COPY docker/entrypoint.sh /var/www/firefly-iii/docker/entrypoint.sh  
ADD docker/apache-firefly.conf /etc/apache2/sites-available/000-default.conf  
RUN chown -R www-data:www-data /var/www && chmod -R 775 /var/www/firefly-
iii/storage  
  
WORKDIR /var/www/firefly-iii  
EXPOSE 80  
ENTRYPOINT ["/var/www/firefly-iii/docker/entrypoint.sh"]  

