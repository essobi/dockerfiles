FROM php:7.0-fpm  
  
#to have color and alias in bash  
ENV TERM xterm  
ADD .bashrc /root/.bashrc  
  
#apt-update && composer  
RUN apt-get -y update && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
#install dependencies  
RUN apt-get -y install \  
imagemagick \  
gcc nasm build-essential make wget \  
git vim  
  
#install MozJPEG  
RUN \  
wget
"https://github.com/mozilla/mozjpeg/releases/download/v3.1/mozjpeg-3.1-release-
source.tar.gz" && \  
tar xvf "mozjpeg-3.1-release-source.tar.gz" && \  
cd mozjpeg && \  
./configure && \  
make && \  
make install  
  
#install phpUnit  
RUN \  
wget https://phar.phpunit.de/phpunit.phar && \  
chmod +x phpunit.phar && \  
mv phpunit.phar /usr/local/bin/phpunit  
  
#add www-data + mdkdir var folder  
RUN usermod -u 1000 www-data && \  
mkdir -p /var/www/html/var && \  
chown -R www-data:www-data /var/www/html/var  
  
WORKDIR /var/www/html  
  
#Init.sh as entrypoint  
ADD init.sh docker/php7-fpm/init.sh  
RUN chmod a+x docker/php7-fpm/init.sh  
  
CMD ["php-fpm"]  

