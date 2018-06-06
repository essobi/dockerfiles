FROM ubuntu:trusty  
MAINTAINER Warren Legg  
  
# Install base packages  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq install \  
curl \  
apache2 \  
libapache2-mod-php5 \  
php5-mysql \  
php5-gd \  
php5-curl \  
php-pear \  
php5-dev \  
php-apc \  
ssmtp \  
&& \  
rm -rf /var/lib/apt/lists/* && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf && \  
sed -i "s/variables_order.*/variables_order = \"EGPCS\"/g"
/etc/php5/apache2/php.ini  
  
# Add image configuration and scripts  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
  
# Configure /app folder with sample app  
#RUN mkdir -p /app && rm -fr /var/www/html && ln -s /app /var/www/html  
ADD app /var/www/html/app  
  
#Add xdebug components. Only used subsequently if container set with DEBUG=1  
ADD xdebug-2.2.3.tar /xdebugsrc  
  
EXPOSE 80  
WORKDIR /var/www/html/app  
CMD ["/run.sh"]

