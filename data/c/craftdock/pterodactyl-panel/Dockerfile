FROM craftdock/alpine-php7:7.2  
  
LABEL maintainer="Hexosse <hexosse@gmail.com>" \  
description="Pterodactyl panel image based on alpine with runit process
supervisor."  
# Pterodactyl version  
ENV PTERODACTYL_PANEL_VERSION 0.7.6  
  
RUN \  
# Print executed commands  
set -x \  
# Update repository indexes  
&& apk-update \  
# Make sure composer is up to date  
&& composer self-update \  
# Download Pterodactyl  
&& curl -Lo "pterodactyl-panel.tar.gz"
"https://github.com/Pterodactyl/Panel/releases/download/v${PTERODACTYL_PANEL_VERSION}/panel.tar.gz"
\  
&& tar --strip-components=1 -xzvf pterodactyl-panel.tar.gz -C /var/www/ \  
&& rm pterodactyl-panel.tar.gz \  
# set correct permissions  
&& chmod -R 755 /var/www/storage/* /var/www/bootstrap/cache \  
# Install pterodactyl  
&& composer install --ansi --no-dev --no-scripts --working-dir=/var/www/ \  
# Create folders  
&& mkdir -p /var/www/storage \  
&& mkdir -p /var/www/storage/app \  
&& mkdir -p /var/www/storage/app/public \  
&& mkdir -p /var/www/storage/framework \  
&& mkdir -p /var/www/storage/framework/cache \  
&& mkdir -p /var/www/storage/framework/sessions \  
&& mkdir -p /var/www/storage/framework/views \  
&& mkdir -p /var/www/storage/logs \  
&& mkdir -p /var/www/bootstrap/cache \  
&& chown -R www-data:www-data /var/www \  
# Clear apk's cache  
&& apk-cleanup \  
# Remove default php-fpm service  
&& rm -rf /etc/service.d/php-fpm  
  
# Copy scripts  
COPY /rootfs /  
# Add volume to allow persistence  
VOLUME [ "/pterodactyl", "/var/www" ]  

