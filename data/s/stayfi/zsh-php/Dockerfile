FROM stayfi/php70-fpm-dev-alpine  
MAINTAINER Stayfi B. <stayfi@gmail.com>  
  
  
# Register the COMPOSER_HOME environment variable  
ENV COMPOSER_HOME /composer  
# Add global binary directory to PATH and make sure to re-export it  
ENV PATH /composer/vendor/bin:$PATH  
# Allow Composer to be run as root  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_VERSION master  
  
RUN apk add --update zsh git sudo \  
&& sudo sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-
zsh/master/tools/install.sh -O -)" \  
&& sudo sed -i -- 's/ZSH_THEME="robbyrussell"/ZSH_THEME="gallois"/g'
/root/.zshrc \  
&& sudo sed -i -- 's/plugins=(git)/plugins=(git composer symfony2)/g'
/root/.zshrc \  
  
# Setup the Composer installer  
&& curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }" \  
&& php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer --snapshot && rm -rf /tmp/composer-setup.php \  
  
# Install Symfony  
&& curl -LsS https://symfony.com/installer -o /bin/symfony \  
&& chmod a+x /bin/symfony  
  
ENV SHELL=/bin/zsh  
  
EXPOSE 8000  
  
WORKDIR /var/www  
  
ENTRYPOINT /bin/zsh

