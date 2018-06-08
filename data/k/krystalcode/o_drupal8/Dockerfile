FROM php:7.0-apache  
  
# Install OS packages required.  
# Required by php extensions: libcurl4-gnutls-dev libjpeg-dev libpng-dev
libfreetype6-dev  
# Required by composer for installing certain packages: git unzip  
# Required by Drupal/Drush for communicating with the database: mysql-client  
# Required for text editing: vim  
# Required for better shell experience: powerline fonts-powerline  
RUN apt-get update && \  
apt-get -y install libcurl4-gnutls-dev libjpeg-dev libpng-dev libfreetype6-dev
git unzip mysql-client vim powerline fonts-powerline && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
# Install php extensions required by Drupal.  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install -j$(nproc) mysqli pdo_mysql mbstring gd curl opcache
bcmath && \  
# Enable 'mod_expires' and 'mod_headers' apache modules required by the  
# 'advagg' module for properly setting headers.  
# Enable 'mod_rewrite' apache module for URL rewriting.  
a2enmod expires headers rewrite && \  
# Install 'drush-launcher'.  
curl -L -o /usr/local/bin/drush https://github.com/drush-ops/drush-
launcher/releases/download/0.5.1/drush.phar && \  
chmod +x /usr/local/bin/drush && \  
# Install 'drupal-console-launcher'.  
curl -L -o /usr/local/bin/drupal https://drupalconsole.com/installer && \  
chmod +x /usr/local/bin/drupal && \  
# Install 'composer'.  
curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer && \  
  
# Create a user that should own the application files.  
groupadd -r application && useradd -r -g application application && \  
  
# Export the TERM environment variable.  
# Configure bash shell to use "powerline" by default.  
printf '\n%s\n%s\n\n\n%s\n%s\n%s\n%s\n%s\n\n' '# Export TERM environment
variable' 'export TERM=xterm' '# Use powerline' 'powerline-daemon -q'
'POWERLINE_BASH_CONTINUATION=1' 'POWERLINE_BASH_SELECT=1' '.
/usr/share/powerline/bindings/bash/powerline.sh' >> ~/.bashrc  
# Add apache configuration file.  
# The only change compared to the default file is that it changes the document  
# root to be the /var/www/html/web folder as required by Drupal. We don't use
a  
# virtual host 1) because it is causing the container not to start, and 2) it
is  
# not needed since this is the only site served by this web server.  
#  
# @Issue(  
# "Include all .htaccess files when the server is starting"  
# type="improvement"  
# priority="normal"  
# labels="performance"  
# )  
COPY apache2.conf /etc/apache2/apache2.conf  

