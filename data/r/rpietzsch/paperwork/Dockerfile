FROM centurylink/apache-php:latest  
MAINTAINER Derek Myers <arcticpro@gmail.com>  
  
# Install packages  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y upgrade && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install supervisor pwgen && \  
apt-get -y install mysql-client libmcrypt4 php5-mcrypt php5-json php5-curl \  
php5-cli nodejs nodejs-legacy npm git git-core  
  
# Override default apache conf  
ADD ./deploy/apache.conf /etc/apache2/sites-enabled/000-default.conf  
  
# Enable apache rewrite module  
RUN a2enmod rewrite  
  
# Enable php mcrypt module  
RUN php5enmod mcrypt  
  
RUN echo "#!/bin/bash" > /start.sh && \  
echo "cd /app && php artisan migrate --force && cd -" >> /start.sh && \  
echo "source /etc/apache2/envvars" >> /start.sh && \  
echo "exec apache2 -D FOREGROUND" >> /start.sh  
  
# Configure /app folder  
RUN mkdir -p /app && rm -fr /var/www/html  
  
# Copy application + install dependencies  
ADD . /app  
RUN ln -s /app/public /var/www/html  
  
WORKDIR /app  
RUN composer self-update  
RUN composer install  
RUN npm update && npm install  
RUN sudo npm install -g gulp && gulp  
  
# Fix permissions for apache  
RUN chown -R www-data:www-data /app && chmod +x /app/docker-runner.sh  
  
# Override environment to ensure laravel is running migrations.  
RUN sed -i 's/return $app;//' /app/bootstrap/start.php  
RUN echo '$env = $app->detectEnvironment(function() { return "development";
}); return $app;' >> /app/bootstrap/start.php  
  
CMD ["/app/docker-runner.sh"]  
  

