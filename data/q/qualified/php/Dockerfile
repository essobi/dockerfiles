FROM php:7.0.24-cli-alpine  
  
RUN set -ex; \  
adduser -D codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
RUN set -ex; \  
curl -fsSL https://phar.phpunit.de/phpunit-5.7.phar -o
/usr/local/bin/phpunit.phar; \  
chmod 755 /usr/local/bin/phpunit.phar; \  
ln -s /usr/local/bin/phpunit.phar /usr/local/bin/phpunit;  
  
WORKDIR /workspace  
  
COPY rootfs/runner /runner  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior  

