FROM ubuntu:trusty  
  
WORKDIR /var/dev  
  
COPY . .  
  
RUN apt-get update  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y php5 php5-mysqlnd
php5-gd wget curl git  
  
RUN ["/bin/bash", "-c", "curl -sS https://getcomposer.org/installer | \  
php -- --install-dir=/usr/local/bin --filename=composer"]  
  
RUN composer install  
  
RUN ["/bin/bash", "-c", "curl -sL https://deb.nodesource.com/setup_9.x | sudo
-E bash - \  
&& apt-get install -y nodejs"]  
  
RUN npm install  
  
RUN npm install -g bower  
  
RUN bower install --allow-root  
  
RUN npm install -g gulp-cli && npm install gulp-cli  
  
RUN gulp clean \  
&& gulp css \  
&& gulp css-images \  
&& gulp fonts \  
&& gulp scripts  
  
RUN a2enmod ssl  
RUN a2enmod rewrite  
RUN a2dissite 000-default.conf  
  
RUN rm -rf /etc/apache2/sites-enabled && rm -rf /etc/apache2/sites-available  
  
RUN cp -r dev/sites-available /etc/apache2  
  
RUN mkdir /etc/apache2/sites-enabled  
  
RUN a2ensite 000-default.conf  
RUN a2ensite default-ssl.conf  
  
RUN sed '/<Directory \/var\/www\/>/,/<\/Directory>/ s/AllowOverride
None/AllowOverride all/' /etc/apache2/apache2.conf  
  
RUN service apache2 restart  
  
RUN /bin/bash -c "source dev/mysql.sh"  
  
EXPOSE 80 443  
ENTRYPOINT rm -r /var/www/* && cp -r /var/dev/. /var/www && service apache2
restart && service mysql restart && php /var/www/lovesound migrate &&
/bin/bash

