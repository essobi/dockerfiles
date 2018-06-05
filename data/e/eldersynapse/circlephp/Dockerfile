FROM circleci/php:7.1-fpm-node-browsers  
LABEL Matthew Ridehalgh <matthew.ridehalgh@elder-studios.co.uk>  
  
#Install the additional requirements plus AWS CLI  
RUN sudo apt-get update \  
&& sudo apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
&& sudo wget https://phar.phpunit.de/phpunit-6.5.phar \  
&& sudo chmod +x phpunit-6.5.phar \  
&& sudo mv phpunit-6.5.phar /usr/local/bin/phpunit \  
&& sudo docker-php-ext-install gd \  
&& sudo curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip" \  
&& sudo unzip awscli-bundle.zip \  
&& sudo ./awscli-bundle/install -b ~/bin/aws  
  

