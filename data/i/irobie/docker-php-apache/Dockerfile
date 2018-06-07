FROM phusion/baseimage:latest  
  
MAINTAINER Robert Crandall <offlinegeek@outlook.com>  
  
  
# Install base packages  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq install \  
curl \  
apache2 \  
libapache2-mod-php5 \  
php5-mysql \  
php5-mcrypt \  
php5-gd \  
php5-curl \  
php-pear \  
php-apc && \  
rm -rf /var/lib/apt/lists/* && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN /usr/sbin/php5enmod mcrypt  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf && \  
sed -i "s/variables_order.*/variables_order = \"EGPCS\"/g"
/etc/php5/apache2/php.ini  
  
ENV ALLOW_OVERRIDE **False**  
  
# Copy config files to a temporary location, used for restoring default files  
RUN mkdir /tmp/php5/ && mkdir /tmp/apache2/  
RUN cp -a /etc/php5/. /tmp/php5/ && cp -a /etc/apache2/. /tmp/apache2/  
  
# Add image configuration and scripts  
ADD startup.sh /startup.sh  
RUN chmod 755 /*.sh  
  
EXPOSE 80  
CMD ["/startup.sh"]  

