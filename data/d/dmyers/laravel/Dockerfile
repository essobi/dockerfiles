FROM centurylink/apache-php:latest  
MAINTAINER Derek Myers <arcticpro@gmail.com>  
  
# Install packages  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y upgrade && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install supervisor pwgen && \  
apt-get -y install mysql-client libmcrypt4 php5-mcrypt php5-json php5-curl
php5-cli  
  
# Override default apache conf  
ADD apache.conf /etc/apache2/sites-enabled/000-default.conf  
  
# Enable apache rewrite module  
RUN a2enmod rewrite  
  
# Enable php mcrypt module  
RUN php5enmod mcrypt  
  
# Configure /app folder  
RUN mkdir -p /app && rm -fr /var/www/html && ln -s /app/public /var/www/html  
  
# Download Laravel into /app  
RUN rm -fr /app && mkdir /app && \  
composer create-project laravel/laravel /app --prefer-source  
  
# Fix permissions for apache  
RUN chown -R www-data:www-data /app  
RUN chmod -R 0777 /app/app/storage  
  
# Add database config with info for Laravel to connect to DB  
ADD database.php /app/app/config/database.php  
RUN chmod 644 /app/app/config/database.php  
  
# Add script to create 'laravel' DB  
ADD run.sh run.sh  
RUN chmod 755 /*.sh  
  
EXPOSE 80  
CMD ["/run.sh"]  

