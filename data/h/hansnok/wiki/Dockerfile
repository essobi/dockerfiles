FROM php:7.1-apache  
  
# install the PHP extensions we need  
RUN set -ex; \  
\  
apt-get update; \  
apt-get install -y \  
libjpeg-dev \  
libpng-dev \  
libbz2-dev \  
zlib1g-dev \  
unzip \  
; \  
rm -rf /var/lib/apt/lists/*; \  
\  
docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr; \  
docker-php-ext-install gd mysqli opcache  
# TODO consider removing the *-dev deps and only keeping the necessary lib*
packages  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=2'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
RUN a2enmod rewrite expires  
  
VOLUME /var/www/html  
  
ENV WORDPRESS_VERSION 4.9.6  
ENV WORDPRESS_SHA1 40616b40d120c97205e5852c03096115c2fca537  
ENV KNOWLEDGEBASE_VERSION 1.1.8  
ENV SUPER_CACHE_VERSION 1.6.1  
ENV ARCADIA_VERSION 1.1.1  
ENV SPACIOUS_VERSION 1.5.2  
ENV IXION_VERSION 1.1.2  
ENV JETPACK_VERSION 6.1.1  
  
RUN set -ex; \  
curl -o wordpress.tar.gz -fSL
"https://wordpress.org/wordpress-${WORDPRESS_VERSION}.tar.gz"; \  
echo "$WORDPRESS_SHA1 *wordpress.tar.gz" | sha1sum -c -; \  
# upstream tarballs include ./wordpress/ so this gives us /usr/src/wordpress  
tar -xzf wordpress.tar.gz -C /usr/src/; \  
rm wordpress.tar.gz; \  
# Add wp-super_cache plugin to the current container  
curl -o supercache.tar.gz -fSL "https://github.com/Automattic/wp-super-
cache/archive/${SUPER_CACHE_VERSION}.tar.gz"; \  
tar -xzf supercache.tar.gz -C /usr/src/wordpress/wp-content/plugins/; \  
rm supercache.tar.gz; \  
# Add wp-knowledgebase plugin  
curl -o knowledgebase.tar.gz -fSL "https://github.com/maevelander/wp-
knowledgebase/archive/${KNOWLEDGEBASE_VERSION}.tar.gz"; \  
tar -xzf knowledgebase.tar.gz -C /usr/src/wordpress/wp-content/plugins/; \  
rm knowledgebase.tar.gz; \  
# Add Jetpack plugin  
curl -o jetpack.zip -fSL
"https://downloads.wordpress.org/plugin/jetpack.${JETPACK_VERSION}.zip"; \  
unzip jetpack.zip -d /usr/src/wordpress/wp-content/plugins/; \  
rm jetpack.zip; \  
# Add Arcadia Basic theme  
curl -o arcadia.zip -fSL "https://downloads.wordpress.org/theme/arcade-
basic.${ARCADIA_VERSION}.zip"; \  
unzip arcadia.zip -d /usr/src/wordpress/wp-content/themes/; \  
rm arcadia.zip; \  
# Add Spacious theme  
curl -o spacious.zip -fSL
"https://downloads.wordpress.org/theme/spacious.${SPACIOUS_VERSION}.zip"; \  
unzip spacious.zip -d /usr/src/wordpress/wp-content/themes/; \  
rm spacious.zip; \  
# Add Ixion theme  
curl -o ixion.zip -fSL
"https://downloads.wordpress.org/theme/ixion.${IXION_VERSION}.zip"; \  
unzip ixion.zip -d /usr/src/wordpress/wp-content/themes/; \  
rm ixion.zip; \  
# Add Spanish languague to Wordpress  
curl -o wordpress.tar.gz -fSL
"https://es.wordpress.org/wordpress-${WORDPRESS_VERSION}-es_ES.tar.gz"; \  
mkdir /usr/src/temp/; \  
tar -xzf wordpress.tar.gz -C /usr/src/temp/; \  
rm wordpress.tar.gz; \  
cp -R /usr/src/temp/wordpress/wp-content/languages/ /usr/src/wordpress/wp-
content/; \  
rm -R /usr/src/temp; \  
chown -R www-data:www-data /usr/src/wordpress;  
  
COPY docker-entrypoint.sh /usr/local/bin/  
  
RUN chmod 777 /usr/local/bin/docker-entrypoint.sh \  
&& ln -s /usr/local/bin/docker-entrypoint.sh /  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["apache2-foreground"]

