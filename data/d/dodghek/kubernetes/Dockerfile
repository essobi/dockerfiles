# Base Image  
FROM vutran/docker-nginx-php5-fpm  
  
# Set the author  
MAINTAINER Youngho Jo <dodghek1@naver.com>  
  
# Update cache and install base packages  
RUN apt-get update && apt-get -y install \  
vim \  
git  
  
# Configure PHP settings  
RUN perl -pi -e 's/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g'
/etc/php5/fpm/php.ini  
RUN perl -pi -e 's/allow_url_fopen = Off/allow_url_fopen = On/g'
/etc/php5/fpm/php.ini  
  
# Boot up Nginx, and PHP5-FPM when container is started  
CMD service php5-fpm start && nginx  
  
# Set the current working directory  
WORKDIR /var/www/html  
  
# Expose port  
EXPOSE 80  
EXPOSE 22  
EXPOSE 443  

