FROM alpine:latest  
MAINTAINER Charlie Francis <charliefrancis@gmail.com>  
  
# Install CURL & PHP  
RUN apk --update add \  
bash \  
curl \  
nodejs \  
php5-cli php5-phar \  
unzip \  
sudo \  
wget  
  
# Install WordPress CLI  
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar \  
&& php wp-cli.phar --info \  
&& chmod +x wp-cli.phar \  
&& sudo mv wp-cli.phar /usr/bin/wp  
  
# Install Composer  
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }"  

