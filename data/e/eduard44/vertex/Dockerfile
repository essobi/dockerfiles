FROM ubuntu:14.04  
MAINTAINER Eduardo Trujillo <ed@chromabits.com>  
  
# Set environment to non-interactive  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update the Ubuntu image  
RUN apt-get update  
RUN apt-get install -y software-properties-common python-software-properties  
RUN add-apt-repository ppa:chris-lea/node.js  
RUN add-apt-repository -y ppa:nginx/stable  
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ precise universe" >>
/etc/apt/sources.list  
RUN apt-get update  
  
## TOOLS  
RUN apt-get install -y vim wget git curl build-essential make  
  
## NODE.JS  
# Install Node and Git  
RUN apt-get install -y nodejs  
  
# Install Gulp, Bower, Grunt, and some other tools  
RUN npm install -g gulp bower grunt-cli supervisor forever  
  
## PHP, LARAVEL  
# Install Nginx  
RUN apt-get install -y nginx php5-fpm php5-cli php5-mcrypt php5-curl &&
service nginx stop  
  
# Install HHVM  
RUN wget -O - http://dl.hhvm.com/conf/hhvm.gpg.key | sudo apt-key add -  
RUN echo deb http://dl.hhvm.com/ubuntu trusty main | sudo tee
/etc/apt/sources.list.d/hhvm.list  
RUN apt-get update  
RUN apt-get install -y hhvm libgmp10 && /usr/share/hhvm/install_fastcgi.sh  
  
# Make HHVM the default interpreter  
RUN /usr/bin/update-alternatives --install /usr/bin/php php /usr/bin/hhvm 60  
  
# Install composer  
RUN bash -c "wget http://getcomposer.org/composer.phar && chmod +x
composer.phar && mv composer.phar /usr/local/bin/composer"  
  
# Install PHPUnit  
RUN bash -c "wget https://phar.phpunit.de/phpunit.phar && chmod +x
phpunit.phar && mv phpunit.phar /usr/local/bin/phpunit"  
  
# Install Laravel installer tool  
RUN composer global require "laravel/installer=~1.1"  
  
# Add config files  
ADD docker /  
  
# Set permission for startup script  
RUN chmod u+x /scripts/start.sh  
  
# Set permissions so that HHVM can execute the default project  
RUN chown -R www-data:www-data /var/www/vertex/public  
  
# Append "daemon off;" to the beginning of the configuration  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# Expose ports  
EXPOSE 80  
CMD ["/scripts/start.sh"]  

