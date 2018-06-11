FROM ubuntu:16.04  
MAINTAINER Veerendra <veeru538@gmail.com>  
  
# This dockerfile is suitable for installing Wordpress  
# installation. The script will also look for /data volume  
# in anticipation of an existing wordpress install. If it's  
# found, then it will analyse it's contents and will  
# link assets like this:  
#  
# data/wp-content folder symlinked  
# data/.htaccess symlinked  
# data/init.sh script initialized  
RUN apt-get update  
RUN apt-get -y upgrade  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install \  
php \  
libapache2-mod-php \  
php-mcrypt \  
php-mysql \  
apache2 \  
php-curl \  
php-gd \  
git \  
unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
#RUN sed -i "s/variables_order.*/variables_order = \"EGPCS\"/g"
/etc/php5/apache2/php.ini  
#RUN sed -i "s/upload_max_filesize.*/upload_max_filesize = 20M/g"
/etc/php5/apache2/php.ini  
#RUN sed -i "s/variables_order.*/variables_order = \"EGPCS\"/g"
/etc/php5/cli/php.ini  
ENV PHP_UPLOAD_MAX_FILESIZE 10M  
ENV PHP_POST_MAX_SIZE 10M  
  
  
RUN a2enmod rewrite  
RUN a2enmod headers  
  
##RUN mkdir -p /app && rm -fr /var/www/html && ln -s /app /var/www/html  
# Install vanilla wordpress  
#ADD https://wordpress.org/latest.tar.gz /wordpress.tar.gz  
#RUN tar xvzf /wordpress.tar.gz  
#RUN cp -aR /wordpress/* /app  
##RUN chown -R www-data:www-data /app  
RUN rm -rf /var/www/html/index.html  
  
# Use our default config  
#ADD wp-config.php /app/wp-config.php  
#ADD * /app/  
##COPY . /app/  
# Initialize custom config from volume  
#ADD volume-init.sh /volume-init.sh  
#RUN chmod 755 /volume-init.sh  
VOLUME /var/www/html  
COPY . /var/www/html/  
RUN chown -R www-data:www-data /var/www/html  
  
# Configure and start apache  
ADD vhost.conf /etc/apache2/sites-enabled/000-default.conf  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
EXPOSE 80  
EXPOSE 3306  
#WORKDIR /app  
#CMD ["/run.sh"]  
#ENTRYPOINT ["/run.sh"]  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

