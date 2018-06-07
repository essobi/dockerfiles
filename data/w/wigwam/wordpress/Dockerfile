FROM debian:stretch  
  
  
# Install Apache2 + PHP 7.0  
ENV DEBIAN_FRONTEND noninteractive  
RUN set -ex; \  
apt-get update; \  
apt-get install -y apache2 libapache2-mod-php7.0 php7.0-gd php7.0-mysql \  
php7.0-opcache php7.0-cli curl jq unzip; \  
apt-get clean; \  
rm -rf /var/lib/apt/lists/*; \  
a2enmod rewrite expires; \  
touch /etc/apache2/sites-available/wordpress.conf; \  
a2dissite 000-default; \  
a2ensite wordpress  
  
# Install Wordpress  
ENV WORDPRESS_VERSION 4.9.1  
ENV WORDPRESS_SHA1 892d2c23b9d458ec3d44de59b753adb41012e903  
  
RUN set -ex; \  
curl -o wordpress.tar.gz -fSL
"https://wordpress.org/wordpress-${WORDPRESS_VERSION}.tar.gz"; \  
echo "$WORDPRESS_SHA1 *wordpress.tar.gz" | sha1sum -c -; \  
# upstream tarballs include ./wordpress/ so this gives us /var/www/wordpress  
tar -xzf wordpress.tar.gz -C /var/www/; \  
rm wordpress.tar.gz  
  
VOLUME /var/www/wordpress/wp-content/uploads  
  
# Add a themes/plugins installation wrapper script  
COPY wp-install.sh /usr/local/bin/  
  
# Configure Apache, PHP and Wordpress  
COPY apache2-foreground /usr/local/bin/  
COPY wordpress.conf /etc/apache2/sites-available/  
COPY opcache-recommended.ini /etc/php/7.0/apache2/conf.d/  
  
# Configure apache/wordpress settings on the first run  
COPY docker-entrypoint.sh /usr/local/bin/  
  
WORKDIR /var/www/wordpress  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["apache2-foreground"]  

