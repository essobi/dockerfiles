FROM phusion/baseimage:0.9.20  
MAINTAINER Fernando Mayo <fernando@tutum.co>  
  
# Install base packages  
RUN add-apt-repository ppa:ondrej/php  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq install \  
curl \  
apache2 \  
libapache2-mod-php5.6 \  
php5.6-mysql \  
php5.6-mbstring \  
php5.6-mcrypt \  
php5.6-gd \  
php5.6-curl \  
php5.6-xml \  
php-pear && \  
rm -rf /var/lib/apt/lists/* && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN /usr/sbin/phpenmod -v 5.6 mbstring  
  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf && \  
sed -i "s/variables_order.*/variables_order = \"EGPCS\"/g"
/etc/php/5.6/apache2/php.ini  
  
ENV ALLOW_OVERRIDE **False**  
  
# Add image configuration and scripts  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
  
# Configure /app folder with sample app  
RUN mkdir -p /app && rm -fr /var/www/html && ln -s /app /var/www/html  
ADD sample/ /app  
  
EXPOSE 80  
WORKDIR /app  
CMD ["/sbin/my_init", "/run.sh"]  

