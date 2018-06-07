######################################################  
#  
# PHP 5.6 \+ wordpress  
# Tag: deardooley/wordpress  
#  
# This is a minimal alpine-based php 5.6 image with  
# apache2 and composer installed.  
#  
######################################################  
  
FROM deardooley/php-composer:5.6  
MAINTAINER Rion Dooley <dooley@tacc.utexas.edu  
  
RUN echo "Installing opcache..." && \  
apk --update add php5-opcache php5-mysqli && \  
rm -f /var/cache/apk/* && \  
{ \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=60'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=0'; \  
} > /etc/php5/conf.d/opcache-recommended.ini && \  
  
curl -sS -o /usr/local/bin/wp https://raw.githubusercontent.com/wp-
cli/builds/gh-pages/phar/wp-cli.phar && \  
chmod +x /usr/local/bin/wp && \  
sed -i 's#%DOCUMENT_ROOT%#/var/www/html#g' /etc/apache2/httpd.conf && \  
sed -i 's#%DOCUMENT_ROOT%#/var/www/html#g' /etc/apache2/conf.d/ssl.conf && \  
  
#sed -i 's/^#LoadModule deflate_module/LoadModule deflate_module/g'
/etc/apache2/httpd.conf && \  
#sed -i 's/^#LoadModule expires_module/LoadModule expires_module/g'
/etc/apache2/httpd.conf && \  
  
# enable any environment variables to be read from php scripts  
sed -i 's/safe_mode_allowed_env_vars/;safe_mode_allowed_env_vars/g'
/etc/php5/php.ini && \  
  
echo "Checking wordpress cli install..." && \  
wp --info --allow-root && \  
wp --allow-root core download && \  
{ \  
echo "\$redis_server = array("; \  
echo " 'host' => '%WP_REDIS_HOST%',"; \  
echo " 'port' => %WP_REDIS_PORT%,"; \  
echo " 'auth' => '%WP_REDIS_PASSWORD%',"; \  
echo " 'database' => %WP_REDIS_DATABASE%, // Optionally use a specific numeric
Redis database. Default is 0."; \  
echo ");"; \  
echo "define('WP_MEMORY_LIMIT', '256M');"; \  
echo "define('WP_MAX_MEMORY_LIMIT', '256M');"; \  
echo "define('WP_DEBUG', true);"; \  
echo "define('WP_DEBUG_DISPLAY', false );"; \  
echo "define('SAVEQUERIES', true);"; \  
echo "define('SCRIPT_DEBUG', true);"; \  
echo "define('DISALLOW_FILE_EDIT', true);"; \  
echo "define('FORCE_SSL_ADMIN', true);"; \  
echo "define('WP_HTTP_BLOCK_EXTERNAL', false);"; \  
echo "define('WP_ACCESSIBLE_HOSTS', '*');"; \  
echo "define('DISABLE_WP_CRON', false);"; \  
echo "if (\$_SERVER['HTTP_X_FORWARDED_PROTO'] == 'https')
\$_SERVER['HTTPS']='on';"; \  
echo "\$sgenv =
array('USERNAME','PASSWORD','API_KEY','SEND_METHOD','FROM_NAME','FROM_EMAIL','REPLY_TO','CATEGORIES','TEMPLATE');";
\  
echo "foreach(\$sgenv as \$sgvar) { "; \  
echo " if (isset(\$_ENV['SENDGRID_'.\$sgvar])) {"; \  
echo " define('SENDGRID_'.\$sgvar, \$_ENV['SENDGRID_'.\$sgvar]); "; \  
echo " }"; \  
echo "}"; \  
} | wp --allow-root core config --dbname='%%DB_NAME%%' --dbuser='%%DB_USER%%'
--dbpass='%%DB_PASS%%' --dbhost='%%DB_HOST%%' --skip-check --extra-php && \  
chown -R apache:apache /var/www/html/*  
  
ADD docker_entrypoint.sh /docker_entrypoint.sh  

