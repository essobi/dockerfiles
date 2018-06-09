FROM php:5.6-apache  
  
# install the PHP extensions we need  
RUN set -ex; \  
\  
apt-get update; \  
apt-get install -y \  
libjpeg-dev \  
libpng12-dev \  
; \  
rm -rf /var/lib/apt/lists/*; \  
\  
docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr; \  
docker-php-ext-install gd mysqli opcache  
# TODO consider removing the *-dev deps and only keeping the necessary lib*
packages  
#ENV WORDPRESS_TITLE  
#ENV WORDPRESS_ADMINUSER  
#ENV WORDPRESS_ADMINPASSWORD  
#ENV WORDPRESS_URL  
#ENV WORDPRESS_ADMINEMAIL  
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
  
#VOLUME /home/site/wwwroot  
ENV WORDPRESS_VERSION 4.8  
ENV WORDPRESS_SHA1 3738189a1f37a03fb9cb087160b457d7a641ccb4  
  
RUN set -ex; \  
curl -o wordpress.tar.gz -fSL
"https://wordpress.org/wordpress-${WORDPRESS_VERSION}.tar.gz"; \  
echo "$WORDPRESS_SHA1 *wordpress.tar.gz" | sha1sum -c -; \  
# upstream tarballs include ./wordpress/ so this gives us /usr/src/wordpress  
tar -xzf wordpress.tar.gz -C /usr/src/; \  
rm wordpress.tar.gz; \  
cp -r /usr/src/wordpress/. /var/www/html/; \  
chown -R www-data:www-data /var/www/html  
  
# Install wp-cli  
RUN curl -L https://github.com/wp-cli/wp-cli/releases/download/v0.24.1/wp-
cli-0.24.1.phar -o /usr/local/bin/wp \  
&& chmod +x /usr/local/bin/wp  
  
# Download WP-Azure-Storage  
RUN curl -L https://downloads.wordpress.org/plugin/windows-azure-
storage.4.0.2.zip -o /tmp/wp-azure-storage.zip  
  
COPY init_container.sh /bin/  
  
RUN apt-get update \  
&& apt install -y --no-install-recommends \  
openssh-server \  
&& apt install -y vim \  
&& apt install -y mysql-client \  
&& chmod 755 /bin/init_container.sh \  
&& echo "root:Docker!" | chpasswd  
  
RUN \  
rm -f /var/log/apache2/* \  
&& rmdir /var/lock/apache2 \  
&& rmdir /var/run/apache2 \  
&& rmdir /var/log/apache2 \  
&& chmod 777 /var/log \  
&& chmod 777 /var/run \  
&& chmod 777 /var/lock \  
&& chmod 777 /bin/init_container.sh \  
&& rm -rf /var/log/apache2 \  
&& mkdir -p /home/LogFiles \  
&& ln -s /home/LogFiles /var/log/apache2  
  
COPY sshd_config /etc/ssh/  
  
EXPOSE 2222  
EXPOSE 80  
#ENV PATH ${PATH}:/home/site/wwwroot  
WORKDIR /var/www/html  
  
ENTRYPOINT ["/bin/init_container.sh"]  
CMD ["apache2-foreground"]  

