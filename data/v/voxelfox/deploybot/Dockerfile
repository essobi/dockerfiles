from php:7.0.14-cli  
  
# Update apt repos for Nodejs and Yarn  
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash -  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
RUN apt-get update && \  
apt-get install -y build-essential bzip2 inotify-tools nodejs yarn git
zlib1g-dev libbz2-dev libpng12-dev libjpeg-dev unzip curl && \  
docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr && \  
docker-php-ext-install zip bz2 gd  
  
# Allow Composer to be run as root  
ENV COMPOSER_ALLOW_SUPERUSER 1  
  
# Install Composer and make it available in the PATH  
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

