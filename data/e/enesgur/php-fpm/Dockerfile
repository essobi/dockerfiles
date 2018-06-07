FROM enesgur/php-fpm:7.1  
  
MAINTAINER Enes Gür  
  
# Install Packages  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN curl -s
"https://packagecloud.io/install/repositories/phalcon/stable/script.deb.sh" |
bash  
RUN apt-get update  
RUN apt-get install php7.1-phalcon -y  
  
# Enable PHP Extension Settings Before Run PHP-FPM  
RUN phpenmod phalcon  
  
CMD ["supervisord"]  

