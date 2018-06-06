FROM php:7.1-cli  
  
# Install our basic tools ssh & rsync  
RUN apt-get update -yqq && apt-get install openssh-client bash rsync git -yqq  
  
# Disable host key checking for ssh  
RUN mkdir /root/.ssh  
COPY config /root/.ssh/config  
  
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }"\  
&& php /tmp/composer-setup.php --no-ansi --install-dir=/usr/bin
--filename=composer  

