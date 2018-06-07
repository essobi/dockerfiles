FROM wordpress:php7.1-apache  
  
# Install the PHP extensions we need  
RUN set -ex; \  
\  
apt-get update; \  
apt-get install -y \  
mysql-client \  
sudo \  
; \  
rm -rf /var/lib/apt/lists/*;  
  
# Install wp-cli, and allow it to regenerate .htaccess files  
# Use /usr/local/bin/wp-cli.phar to run it as root  
# and wp to run it as www-data (your own user)  
COPY wp-su.sh /usr/local/bin/wp  
RUN curl -o /usr/local/bin/wp-cli.phar https://raw.githubusercontent.com/wp-
cli/builds/gh-pages/phar/wp-cli.phar; \  
chmod a+x /usr/local/bin/wp-cli.phar; \  
{ \  
echo 'apache_modules:'; \  
echo ' - mod_rewrite'; \  
} > /var/www/wp-cli.yml  
  
WORKDIR /var/www/html  
VOLUME /var/www/html  
  
# Change www-data user to match the host system UID and GID and chown www
directory  
RUN usermod --non-unique --uid 1000 www-data \  
&& groupmod --non-unique --gid 1000 www-data \  
&& chown -R www-data:www-data /var/www  
  
EXPOSE 80 443  
# Overrides wp docker default entrypoint  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["apache2-foreground"]  

