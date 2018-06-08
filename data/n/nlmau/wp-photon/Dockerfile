FROM php:apache  
MAINTAINER SPP  
  
RUN apt-get update \  
&& apt-get -y --no-install-recommends install \  
subversion \  
optipng \  
pngquant \  
libgraphicsmagick1-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
&& rm -r /var/lib/apt/lists/* \  
&& yes "\n" | pecl -d preferred_state=beta install -s gmagick \  
&& a2enmod rewrite \  
&& echo "extension=gmagick.so" > /usr/local/etc/php/conf.d/gmagick.ini \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& svn checkout https://code.svn.wordpress.org/photon/ /var/www/html/ \  
&& { \  
echo '<Directory /var/www/html>'; \  
echo 'RewriteEngine on'; \  
echo 'RewriteCond %{REQUEST_FILENAME} !-d'; \  
echo 'RewriteCond %{REQUEST_FILENAME} !-f'; \  
echo 'RewriteRule . index.php [L]'; \  
echo '</Directory>'; \  
} | tee /etc/apache2/conf-available/photon.conf \  
&& a2enconf photon  

