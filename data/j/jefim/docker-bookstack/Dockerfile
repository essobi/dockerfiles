FROM phusion/baseimage:0.9.18  
MAINTAINER Jefim Borissov jefim.borissov@gmail.com  
  
# Install Apache2 and PHP5  
RUN apt-get update && apt-get install -y \  
apache2 \  
php5 \  
php5-mysql \  
php5-curl \  
php5-gd \  
git \  
wget  
  
# Get latest BookStack release  
RUN cd /tmp && \  
git clone https://github.com/ssddanbrown/BookStack.git --branch release
--single-branch && \  
rm /var/www/html/index.html && \  
mv /tmp/BookStack/* /var/www/html  
  
# Install Composer (required by BookStack)  
WORKDIR /tmp  
COPY install-composer.sh /tmp  
RUN /tmp/install-composer.sh  
  
# Install BookStack dependencies using composer  
WORKDIR /var/www/html  
RUN php /tmp/composer.phar config -g github-oauth.github.com
48d49a561c67d23657b41a57b10c871764b35676 && \  
php /tmp/composer.phar install && \  
php artisan key:generate  
  
RUN chmod a+w -R storage && \  
chmod a+w -R public/uploads && \  
a2enmod rewrite  
  
#php artisan migrate  
RUN wget
https://github.com/jwilder/dockerize/releases/download/v0.2.0/dockerize-linux-
amd64-v0.2.0.tar.gz && \  
tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.2.0.tar.gz  
  
COPY .htaccess /var/www/html/public  
COPY .env.template /var/www/html  
COPY create-db.template.php /tmp  
COPY 000-default.conf /etc/apache2/sites-enabled/000-default.conf  
  
# Copy and run our entry point  
COPY apache-foreground.sh /usr/local/bin/  
EXPOSE 80  
CMD ["/usr/local/bin/apache-foreground.sh"]  

