FROM debian:jessie  
  
# Install PHP  
RUN apt-get update && apt-get install -y \  
curl \  
git \  
ca-certificates \  
php5 \  
php5-cli \  
php5-mysql \  
php5-mcrypt \  
php5-gd \  
php5-common \  
php5-curl \  
\--no-install-recommends && rm -r /var/lib/apt/lists/*  
  
# Install Composer  
RUN php -r "readfile('https://getcomposer.org/installer');" > composer-
setup.php \  
&& php -r "if (hash('SHA384', file_get_contents('composer-setup.php')) ===
'7228c001f88bee97506740ef0888240bd8a760b046ee16db8f4095c0d8d525f2367663f22a46b48d072c816e7fe19959')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" \  
&& php composer-setup.php \  
&& php -r "unlink('composer-setup.php');" \  
&& mv composer.phar /usr/local/bin/composer  
  
COPY drupal /var/www/drupal  
WORKDIR /var/www/drupal  
  
# Install Drupal  
RUN composer install --ignore-platform-reqs --ansi --no-interaction  
  
# Remove dependencies  
RUN AUTO_ADDED_PACKAGES=`apt-mark showauto` \  
&& apt-get remove --purge -y \  
curl \  
git \  
ca-certificates \  
php5 \  
php5-cli \  
php5-mysql \  
php5-mcrypt \  
php5-gd \  
php5-common \  
php5-curl \  
$AUTO_ADDED_PACKAGES  
  
VOLUME ["/var/www/drupal"]  

