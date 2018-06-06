FROM symball/php_symfony_alpine  
MAINTAINER Simon Ball <contact@simonball.me>  
  
RUN apk --update add \  
autoconf \  
bash \  
ca-certificates \  
curl \  
git \  
libsasl \  
nodejs \  
openssh \  
wget \  
&& ssh-keygen -A \  
&& rm -rf /var/cache/apk/*  
  
# Grab the latest Symfony dedicated installer  
RUN curl -LsS https://symfony.com/installer -o /usr/local/bin/symfony && \  
chmod a+x /usr/local/bin/symfony && symfony --version  
  
# Grab the latest Composer install  
RUN curl -sS https://getcomposer.org/installer | \  
php -- --install-dir=/usr/local/bin --filename=composer && composer --version  
  
# Install PHPUnit  
COPY phpunit-5.7.9.phar /usr/local/bin/phpunit  
RUN chmod +x /usr/local/bin/phpunit && \  
phpunit --version  
  
# Install Phing  
COPY phing-2.16.0.phar /usr/local/bin/phing  
RUN chmod +x /usr/local/bin/phing && \  
phing -v  
  
# GulpJS task runner  
RUN npm install gulp -g && gulp -v  
# bower package manager  
RUN npm install bower -g && bower -v  
  
CMD ["/bin/bash"]  

