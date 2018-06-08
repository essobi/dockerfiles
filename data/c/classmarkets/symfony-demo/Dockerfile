FROM php:7-fpm-alpine  
  
# Install any dependencies we need during build, testing, or at runtime that  
# are not in the base image and also not installed by composer. This includes  
# composer itself, PHP extensions and build systems such as grunt or gulp.  
#  
# For instance:  
#  
# RUN apk add --update --no-cache libmcrypt-dev && docker-php-ext-install
mcrypt  
#  
# This would also be a good place to configure php.ini if necessary. See  
# https://hub.docker.com/_/php/ for other customization options.  
RUN curl https://getcomposer.org/composer.phar > /usr/local/bin/composer && \  
chmod 0755 /usr/local/bin/composer  
  
WORKDIR /app  
ENV SYMFONY_ENV prod  
  
# Installing dependencies can take a long time but they usually don't change  
# very often. If we copy only composer.json and composer.lock for now we can  
# leverage the docker cache to not install the same dependencies with every  
# build.  
# Because we don't have the actual application code yet, we can't run any  
# scripts or build the autoloader. We'll do that later.  
COPY composer.json /app/composer.json  
COPY composer.lock /app/composer.lock  
RUN composer install --no-scripts --no-autoloader  
  
# COPY . will invalidate the docker cache. So everything from this point  
# forward will run with every build.  
COPY . /app  
  
# PHP doesn't come with an HTTP server suitable for production use. We need  
# something else to translate between FastCGI and HTTP. We are going to use  
# NGINX for that.  
# The server configuration for NGINX depends very much on our application --  
# webroot location, listening port of the php-fpm process, fastcgi_params,
etc.  
# An NGINX container can't possibly know all these details. So we are going to  
# add the NGINX configuration to this image and then share it with the NGINX  
# container at runtime using volumes.  
COPY app/config/nginx /etc/nginx/conf.d  
  
# Now that we have the application code we can finish the composer setup  
# (remember that we skipped script handlers and autoloader generation
earlier).  
#  
# This is also the time to run any other build steps, such as compiling
assets.  
#  
# Lastly, we empty the cache (otherwise any parameters specifed at runtime  
# wouldn't take effect) and set appropriate ownership.  
#  
# > The echo command amending config_prod.yml is a hack, required because  
# > doctrine/orm is still at 2.4.8 (see config_dev.yml). An update to >= 2.5.5  
# > should make this unnecessary.  
RUN composer dump-autoload --optimize && \  
composer run-script post-install-cmd && \  
echo -e '\ndoctrine: {dbal: {path: "%kernel.root_dir%/data/blog.sqlite" }}' >>
app/config/config_prod.yml && \  
rm -rf app/cache/* && \  
chown -R www-data.www-data app/cache app/logs app/data  
  
USER www-data  
  
# Share our webroot and server config with an NGINX container at runtime.  
# Assuming there is a container named "app" running this image, we can launch  
# NGINX like so  
#  
# docker run --volumes-from app:ro nginx  
#  
# Both webroot and configuration will magically appear in the right place in  
# the NGINX container.  
VOLUME /app/web /etc/nginx/conf.d  

