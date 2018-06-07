# Inherit from Heroku's stack  
FROM heroku/cedar:14  
  
# Internally, we arbitrarily use port 3000  
ENV PORT 8080  
  
  
#RUN export http_proxy=http://192.168.57.78:3128  
#RUN export https_proxy=http://192.168.57.78:3128  
  
# Which versions?  
ENV PHP_VERSION 5.6.15  
ENV HTTPD_VERSION 2.4.17  
ENV NGINX_VERSION 1.8.0  
  
# Create some needed directories  
RUN mkdir -p /app/.heroku/php /app/.profile.d  
WORKDIR /app/user  
  
# so we can run PHP in here  
ENV PATH /app/.heroku/php/bin:/app/.heroku/php/sbin:$PATH  
RUN yes | apt upgrade && \  
apt update && \  
yes | apt install -y \  
nano \  
mc \  
net-tools  
  
# Install Apache  
#--proxy http://192.168.57.78:3128  
RUN curl --location https://lang-php.s3.amazonaws.com/dist-
cedar-14-master/apache-$HTTPD_VERSION.tar.gz | tar xz -C /app/.heroku/php  
# Config  
RUN curl --location https://raw.githubusercontent.com/heroku/heroku-buildpack-
php/5a770b914549cf2a897cbbaf379eb5adf410d464/conf/apache2/httpd.conf.default >
/app/.heroku/php/etc/apache2/httpd.conf  
# FPM socket permissions workaround when run as root  
  
RUN echo "\n\  
Group root\n\  
" >> /app/.heroku/php/etc/apache2/httpd.conf  
  
# Install Nginx  
RUN curl --location https://lang-php.s3.amazonaws.com/dist-
cedar-14-master/nginx-$NGINX_VERSION.tar.gz | tar xz -C /app/.heroku/php  
# Config  
RUN curl --location https://raw.githubusercontent.com/heroku/heroku-buildpack-
php/5a770b914549cf2a897cbbaf379eb5adf410d464/conf/nginx/nginx.conf.default >
/app/.heroku/php/etc/nginx/nginx.conf  
# FPM socket permissions workaround when run as root  
  
RUN echo "\n\  
user nobody root;\n\  
" >> /app/.heroku/php/etc/nginx/nginx.conf  
  
# Install PHP  
RUN curl --location https://lang-php.s3.amazonaws.com/dist-
cedar-14-master/php-$PHP_VERSION.tar.gz | tar xz -C /app/.heroku/php  
# Config  
RUN mkdir -p /app/.heroku/php/etc/php/conf.d  
RUN curl --location https://raw.githubusercontent.com/heroku/heroku-buildpack-
php/5a770b914549cf2a897cbbaf379eb5adf410d464/conf/php/php.ini >
/app/.heroku/php/etc/php/php.ini  
# Enable all optional exts  
  
#RUN pear config-set http_proxy http://192.168.57.78:3128  
#RUN pear config-set https_proxy http://192.168.57.78:3128  
#RUN pecl upgrade-all  
RUN yes | pecl channel-update pecl.php.net \  
&& pecl install xdebug \  
&& pecl install mongodb \  
&& pecl install mongo  
#&& echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name
xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \  
#&& echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \  
#&& echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/xdebug.ini  
  
RUN echo "\n\  
user_ini.cache_ttl = 30 \n\  
zend_extension = opcache.so \n\  
opcache.enable_cli = 1 \n\  
opcache.validate_timestamps = 1 \n\  
opcache.revalidate_freq = 0 \n\  
opcache.fast_shutdown = 0 \n\  
extension=bcmath.so \n\  
extension=calendar.so \n\  
extension=exif.so \n\  
extension=ftp.so \n\  
extension=gd.so \n\  
extension=gettext.so \n\  
extension=intl.so \n\  
extension=mbstring.so \n\  
extension=pcntl.so \n\  
extension=shmop.so \n\  
extension=soap.so \n\  
extension=sqlite3.so \n\  
extension=pdo_sqlite.so \n\  
extension=xmlrpc.so \n\  
extension=xsl.so \n\  
extension=mongo.so \n\  
zend_extension=$(find / -name xdebug.so) \n\  
xdebug.remote_enable=on \n\  
xdebug.remote_autostart=on \n\  
xdebug.remote=9000 \n\  
extension=mongodb.so \n\  
xdebug.remote_connect_back=1 \n\  
error_reporting = E_ALL \n\  
display_errors = On \n\  
display_startup_errors = On \n\  
" >> /app/.heroku/php/etc/php/php.ini  
  
# Install Composer  
RUN curl --location "https://lang-php.s3.amazonaws.com/dist-
cedar-14-master/composer-1.0.0alpha11.tar.gz" | tar xz -C /app/.heroku/php  
  
# copy dep files first so Docker caches the install step if they don't change  
# COPY composer.lock /app/user/  
# COPY composer.json /app/user/  
  
# run install but without scripts as we don't have the app source yet  
# RUN composer install  
# RUN composer update  
# require the buildpack for execution  
# RUN composer show --installed heroku/heroku-buildpack-php || { echo 'Your
composer.json must have "heroku/heroku-buildpack-php" as a "require-dev"
dependency.'; exit 1; }  
# rest of app  
#ADD . /app/user/  
# run install hooks  
# RUN cat composer.json | python -c 'import sys,json; sys.exit("post-install-
cmd" not in json.load(sys.stdin).get("scripts", {}));' && composer run-script
post-install-cmd || true  
  
  
# TODO: run "composer compile", like Heroku?  
  
# ENTRYPOINT ["/usr/bin/init.sh"]  
  
  

