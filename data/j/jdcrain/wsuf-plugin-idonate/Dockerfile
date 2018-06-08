FROM php:7.1-apache  
  
LABEL version="1.0"  
LABEL description="WSU Foundation Online Giving WordPress Plugin"  
LABEL maintainer="Jared Crain <jared.crain@wsu.edu>"  
  
# Install curl, gnupg, node, npm and grunt  
RUN apt-get update \  
&& apt-get install -y \  
curl \  
gnupg \  
&& curl -sL https://deb.nodesource.com/setup_5.x | bash - \  
&& apt-get install -y nodejs \  
&& npm install -g grunt-cli  
  
# Install zip (for composer)  
RUN apt-get update && apt-get install -y zlib1g-dev \  
&& docker-php-ext-install zip  
  
# Install composer  
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
# Make sure we're installing what we think we're installing!  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }" \  
&& php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer --snapshot \  
&& rm -f /tmp/composer-setup.*  
  
COPY . /var/www/html  
  
RUN composer install  
  
# Install packages  
RUN npm install  
  
EXPOSE 8000  
# TODO: Environment variable to run in dev?

