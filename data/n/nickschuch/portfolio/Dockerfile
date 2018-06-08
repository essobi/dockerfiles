FROM ubuntu:14.04  
RUN apt-get update  
  
##  
# Base  
##  
RUN apt-get install -y python-setuptools git curl  
  
##  
# PHP & nginx  
##  
RUN apt-get install -y php5-cli php5-fpm nginx  
RUN echo "cgi.fix_pathinfo = 0;" >> /etc/php5/fpm/php.ini  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
ADD docker/nginx.conf /etc/nginx/sites-available/default  
  
##  
# Composer  
##  
RUN (curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer)  
  
##  
# Build.  
##  
ADD . /var/www  
RUN cd /var/www && composer install --prefer-dist --dev --no-progress  
  
EXPOSE 80  
CMD ["sh", "-c", "service php5-fpm start && nginx"]  

