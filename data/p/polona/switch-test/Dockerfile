FROM ubuntu:16.04  
MAINTAINER Polona Stefanic <polly.st@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
php \  
php-zip \  
php-mbstring \  
php-dom \  
php-mysql \  
composer \  
nodejs \  
nodejs-legacy \  
npm \  
apache2  
  
WORKDIR /var/www/switch-test  
  
RUN git clone https://github.com/PolonaS/switch-test.git /var/www/switch-test  
  
ADD .env /var/www/switch-test/.env  
ADD run.sh /var/www/switch-test/run.sh  
  
RUN chmod +x /var/www/switch-test/run.sh  
  
EXPOSE 8080  
CMD ["/var/www/switch-test/run.sh"]

