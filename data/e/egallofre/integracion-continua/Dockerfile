FROM ubuntu:16.04  
MAINTAINER Eduard Gallofre  
RUN apt-get update  
RUN apt-get install -y apache2 php7.0 libapache2-mod-php7.0 php7.0-mysql
php7.0-mcrypt php7.0-cli php7.0-intl php7.0-curl php7.0-gd php7.0-xml curl
nano vim git unzip net-tools iputils-ping npm && apt-get clean  
  
EXPOSE 80  
WORKDIR /var/www/html  
  
#ENV TERM xterm  
COPY apache2-foreground /usr/local/bin/  
  
RUN chmod +x /usr/local/bin/apache2-foreground  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
CMD ["apache2-foreground"]  
  
ADD src/. /var/www/html  

