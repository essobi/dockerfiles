FROM meuhmeuhconcept/php-fpm  
  
MAINTAINER jn.germon@gmail.com  
  
RUN apk update && \  
apk add \  
openssh \  
curl \  
make \  
git \  
nodejs \  
nodejs-npm \  
yarn \  
zsh && \  
rm -rf /var/cache/apk/*  
  
# Install composer  
RUN curl --silent --show-error https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer  
  
# Install php-cs-fixer  
RUN curl --silent --show-error -L https://github.com/FriendsOfPHP/PHP-CS-
Fixer/releases/download/v1.12.0/php-cs-fixer.phar -o /usr/local/bin/php-cs-
fixer  
RUN chmod a+x /usr/local/bin/php-cs-fixer  
  
ENV CONTAINER_SHELL /bin/bash  
  
VOLUME /home/developer  
  
RUN touch /var/log/dmesg  
  
ADD entrypoint.sh /  
  
RUN chmod u+x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["tail", "-f", "/var/log/dmesg"]  

