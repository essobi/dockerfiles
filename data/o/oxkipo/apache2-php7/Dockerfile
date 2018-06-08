FROM ubuntu:xenial  
  
RUN apt update  
RUN apt upgrade -y  
RUN apt install -y apache2 php7.0 php7.0-cli php7.0-zip php7.0-mcrypt
php7.0-curl php7.0-dom php7.0-mbstring php7.0-mysql php-imagick
libapache2-mod-php7.0 composer wget curl git  
RUN a2enmod rewrite headers php7.0  
  
COPY ./apache/ /etc/apache2/sites-available/  
  
WORKDIR /var/www  
RUN rm -rf *  
  
EXPOSE 80  
CMD /usr/sbin/apache2ctl -D FOREGROUND  

