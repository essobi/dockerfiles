FROM berenberg/web-base:7.2.3-fpm-nginx1.13.9  
  
COPY docker/ /  
  
ENV WORDPRESS_VERSION=4.9.4 \  
WORDPRESS_SHA1=0e630bf940fd586b10e099cd9195b3e825fb194c  
  
RUN set -ex \  
# add addtional envs to php-fpm runtime  
&& echo 'env[WORDPRESS_DB_HOST] = $WORDPRESS_DB_HOST;' >> /usr/local/etc/php-
fpm.conf \  
&& echo 'env[WORDPRESS_DB_NAME] = $WORDPRESS_DB_NAME;' >> /usr/local/etc/php-
fpm.conf \  
&& echo 'env[WORDPRESS_DB_PASSWORD] = $WORDPRESS_DB_PASSWORD;' >>
/usr/local/etc/php-fpm.conf \  
&& echo 'env[WORDPRESS_DB_USER] = $WORDPRESS_DB_USER;' >> /usr/local/etc/php-
fpm.conf \  
# create unique authentication keys and salts  
&& sed -i -- "s/replace_auth_key/`< /dev/urandom tr -dc _A-Z-a-z-0-9 | head
-c${1:-32};echo;`/g" /var/www/html/wp-config.php \  
&& sed -i -- "s/replace_secure_auth_key/`< /dev/urandom tr -dc _A-Z-a-z-0-9 |
head -c${1:-32};echo;`/g" /var/www/html/wp-config.php \  
&& sed -i -- "s/replace_logged_in_key/`< /dev/urandom tr -dc _A-Z-a-z-0-9 |
head -c${1:-32};echo;`/g" /var/www/html/wp-config.php \  
&& sed -i -- "s/replace_nonce_key/`< /dev/urandom tr -dc _A-Z-a-z-0-9 | head
-c${1:-32};echo;`/g" /var/www/html/wp-config.php \  
&& sed -i -- "s/replace_auth_salt/`< /dev/urandom tr -dc _A-Z-a-z-0-9 | head
-c${1:-32};echo;`/g" /var/www/html/wp-config.php \  
&& sed -i -- "s/replace_secure_auth_salt/`< /dev/urandom tr -dc _A-Z-a-z-0-9 |
head -c${1:-32};echo;`/g" /var/www/html/wp-config.php \  
&& sed -i -- "s/replace_logged_in_salt/`< /dev/urandom tr -dc _A-Z-a-z-0-9 |
head -c${1:-32};echo;`/g" /var/www/html/wp-config.php \  
&& sed -i -- "s/replace_nonce_salt/`< /dev/urandom tr -dc _A-Z-a-z-0-9 | head
-c${1:-32};echo;`/g" /var/www/html/wp-config.php \  
# install the PHP extensions we need  
&& apk add --no-cache --virtual .build-deps \  
autoconf \  
&& docker-php-ext-install \  
mysqli \  
&& runDeps="$( \  
scanelf --needed --nobanner --format '%n#p' --recursive
/usr/local/lib/php/extensions \  
| tr ',' '\n' \  
| sort -u \  
| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1
}' \  
)" \  
&& apk add --no-cache --virtual .wordpress-phpexts-rundeps $runDeps \  
&& apk del .build-deps \  
# download wordpress source  
&& curl -o wordpress.tar.gz -fSL
"https://wordpress.org/wordpress-${WORDPRESS_VERSION}.tar.gz" \  
&& echo "$WORDPRESS_SHA1 *wordpress.tar.gz" | sha1sum -c - \  
&& tar -xzf wordpress.tar.gz --strip 1 -C /var/www/html \  
&& rm wordpress.tar.gz \  
# remove all preinstalled plugins and themes  
&& rm -rf /var/www/html/wp-content \  
&& rm -f /var/www/html/readme.html \  
&& chown -R www-data:www-data /var/www/html  

