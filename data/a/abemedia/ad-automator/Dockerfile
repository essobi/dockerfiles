FROM ubuntu:trusty  
MAINTAINER Adam Bouqdib <adam@abemedia.co.uk>  
  
# Install base packages  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq install \  
git \  
curl \  
apache2 \  
libapache2-mod-php5 \  
php5-mysql \  
php5-mcrypt \  
php5-gd \  
php5-curl \  
php5-intl \  
php-apc && \  
rm -rf /var/lib/apt/lists/* && \  
/usr/sbin/php5enmod mcrypt && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# set up apache vhost  
ADD vhost.conf /etc/apache2/sites-enabled/000-default.conf  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf && \  
sed -i "s/variables_order.*/variables_order = \"EGPCS\"/g"
/etc/php5/apache2/php.ini  
  
# Add image scripts  
ADD *.sh /  
RUN chmod 755 /*.sh  
  
# Configure app folder  
RUN mkdir -p /app && chown www-data:www-data /app -R && \  
rm -fr /var/www && ln -s /app /var/www  
  
ADD . /app/  
  
ENV db_name ""  
ENV db_table ""  
ENV facebook_app_id ""  
ENV facebook_app_secret ""  
ENV facebook_ad_account_id ""  
WORKDIR /app  
  
RUN composer install  
  
EXPOSE 80  
CMD ["/run.sh"]

