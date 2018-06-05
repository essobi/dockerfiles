FROM wordpress:4-apache  
  
ENV BEDROCK_VERSION=1.7.0 \  
BEDROCK_SHA1=b32866ea48932a2997b77997487eb92f52623da6 \  
WP_CLI_VERSION=0.23.1 \  
WP_CLI_SHA1=359b41d7cabd4f1a6ea83400b6a337443e6e7331  
  
ENV LC_ALL=C.UTF-8 \  
LANG=C.UTF-8 \  
WP_ENV=production \  
DEFAULT_TIMEZONE=Australia/Melbourne \  
WEBROOT=/app/web  
  
RUN set -xe && \  
apt-get -qq update && \  
apt-get -qq install \  
git \  
zlib1g-dev \  
less \  
\--no-install-recommends \  
&& \  
docker-php-ext-install zip && \  
apt-get clean && \  
rm -r /var/lib/apt/lists/* && \  
true  
  
RUN set -xe && \  
curl -sS -o /usr/local/bin/wp \  
-L https://github.com/wp-cli/wp-cli/releases/download/v${WP_CLI_VERSION}/wp-cli-${WP_CLI_VERSION}.phar && \  
sha1sum /usr/local/bin/wp && \  
echo "$WP_CLI_SHA1 */usr/local/bin/wp" | sha1sum -c - && \  
chmod +x /usr/local/bin/wp && \  
curl -sS -o /tmp/composer-setup.php \  
-L https://getcomposer.org/installer && \  
php /tmp/composer-setup.php \--install-dir=/usr/bin \--filename=composer && \  
rm /tmp/composer-setup.php && \  
true  
  
WORKDIR /app  
  
RUN set -xe && \  
curl -sS -o /tmp/bedrock.tar.gz \  
-L https://github.com/roots/bedrock/archive/${BEDROCK_VERSION}.tar.gz && \  
echo "$BEDROCK_SHA1 */tmp/bedrock.tar.gz" | sha1sum -c - && \  
tar \--strip-components=1 -xzf /tmp/bedrock.tar.gz -C /app && \  
rm /tmp/bedrock.tar.gz && \  
chown -R www-data:www-data /app && \  
composer install \--no-interaction \--no-dev && \  
composer remove \  
johnpbloch/wordpress \  
\--no-interaction && \  
composer install \--no-interaction \--no-dev && \  
composer clear-cache && \  
rm -rf /app/web/wp && \  
ln -s /usr/src/wordpress /app/web/wp && \  
true  
  
COPY wordpress-rewrite.conf /etc/apache2/conf-available/wordpress-rewrite.conf  
RUN set -xe && \  
{ \  
echo 'date.timezone = ${DEFAULT_TIMEZONE}'; \  
} > /usr/local/etc/php/conf.d/date-timezone.ini && \  
{ \  
echo 'upload_max_filesize=20M'; \  
echo 'post_max_size=60M'; \  
} > /usr/local/etc/php/conf.d/upload-limit.ini && \  
echo "DocumentRoot /app/web" >> /etc/apache2/apache2.conf && \  
rm /etc/apache2/sites-enabled/000-default.conf && \  
sed -i 's#<Directory /var/www/>.*#<Directory /app/web/>#'
/etc/apache2/apache2.conf && \  
ln -s /etc/apache2/conf-available/wordpress-rewrite.conf /etc/apache2/conf-
enabled/wordpress-rewrite.conf && \  
{ \  
echo "<?php"; \  
echo "require('/app/web/wp-config.php');"; \  
echo "require_once(ABSPATH . 'wp-settings.php');"; \  
} > /usr/src/wordpress/wp-config.php && \  
{ \  
echo ""; \  
echo "if (file_exists(__DIR__ . '/application.local.php')) {"; \  
echo " require(__DIR__ . '/application.local.php');"; \  
echo "}"; \  
} >> /app/config/application.php && \  
mkdir -p /app/web/app/uploads && \  
true  
  
VOLUME /app/web/app/uploads  
  
ENTRYPOINT []  
CMD ["apache2-foreground"]

