FROM ubuntu:xenial  
  
MAINTAINER Apptivity Lab<dev@apptivitylab.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y \  
git-core curl apache2 libapache2-mod-php7.0 php7.0-common php7.0-cli
php7.0-curl php7.0-json php7.0-mcrypt php7.0-mysqlnd php7.0-pgsql
php7.0-sqlite \  
php-pear php7.0-dev php7.0-ldap php7.0-sybase php7.0-mbstring php7.0-zip
php7.0-soap openssl pkg-config python nodejs python-pip zip ssmtp  
  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
RUN pip install bunch  
  
RUN pecl install mongodb && \  
echo "extension=mongodb.so" > /etc/php/7.0/mods-available/mongodb.ini && \  
phpenmod mongodb  
  
RUN mkdir -p /usr/lib /usr/include  
ADD v8/usr/lib/libv8* /usr/lib/  
ADD v8/usr/include /usr/include/  
ADD v8/usr/lib/php/20151012/v8js.so /usr/lib/php/20151012/v8js.so  
RUN echo "extension=v8js.so" > /etc/php/7.0/mods-available/v8js.ini &&
phpenmod v8js  
  
RUN echo 'sendmail_path = "/usr/sbin/ssmtp -t"' >
/etc/php/7.0/cli/conf.d/mail.ini  
  
ADD ./config/dreamfactory-php.ini /etc/php/7.0/apache2/conf.d/  
  
# install composer  
RUN curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
chmod +x /usr/local/bin/composer  
  
RUN echo "ServerName localhost" | tee /etc/apache2/conf-
available/servername.conf && \  
a2enconf servername  
RUN rm /etc/apache2/sites-enabled/000-default.conf  
ADD ./config/dfp-apache.conf /etc/apache2/sites-available/dreamfactory.conf  
  
ADD headers.conf /etc/apache2/mods-available/headers.conf  
RUN a2ensite dreamfactory  
RUN a2enmod headers  
RUN a2enmod rewrite  
RUN a2enmod ssl  
  
# Copy the dreamfactory app  
RUN usermod -u 1000 www-data  
ADD ./dreamfactory-2.12.0 /var/www  
RUN chown -R www-data:www-data /var/www/bootstrap /var/www/storage  
RUN chmod 775 /var/www  
RUN chmod 777 /var/www/bootstrap  
  
# Install MomentJS  
ADD ./js/moment.min.js /var/www/storage/scripting/moment.min.js  
RUN chmod 755 /var/www/storage/scripting/moment.min.js  
  
WORKDIR /var/www  
  
# install packages  
RUN composer install --no-dev  
  
RUN php artisan df:setup --no-app-key  
  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stderr /var/log/apache2/error.log  
  
EXPOSE 80  
EXPOSE 443  
CMD ["/docker-entrypoint.sh"]  

