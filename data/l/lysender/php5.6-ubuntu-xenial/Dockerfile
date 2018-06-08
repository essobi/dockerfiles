FROM ubuntu:xenial  
MAINTAINER Leonel Baer <leonel@lysender.com>  
  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG C.UTF-8  
# Configure services  
ADD ./start-apache2.sh /start-apache2.sh  
ADD ./install-composer.sh /install-composer.sh  
  
# Combined RUN commands to reduce layer size  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
add-apt-repository ppa:ondrej/php && \  
apt-get update && \  
apt-get install -y \  
wget \  
supervisor \  
php5.6 \  
php5.6-cgi \  
php5.6-cli \  
php5.6-common \  
php5.6-fpm \  
php5.6-mysql \  
php5.6-mbstring \  
php5.6-curl \  
php5.6-dev \  
php5.6-gd \  
php5.6-xml \  
php5.6-mcrypt \  
php5.6-xmlrpc \  
php5.6-zip \  
libxrender1 \  
libxext6 \  
libfontconfig1 \  
git \  
curl \  
apache2 \  
libapache2-mod-php5.6 \  
openssl && \  
apt-get clean && \  
chmod 755 /*.sh && \  
mkdir -p /etc/supervisor/conf.d && \  
echo "ServerName localhost" >> /etc/apache2/apache2.conf && \  
phpenmod mcrypt && \  
phpenmod curl && \  
a2enmod rewrite && \  
a2enmod headers && \  
a2enmod deflate && \  
a2enmod env && \  
a2enmod expires && \  
chmod +x /install-composer.sh && \  
/install-composer.sh && \  
mv composer.phar /usr/bin/composer  
  
ADD ./supervisor-apache2.conf /etc/supervisor/conf.d/apache2.conf  
ADD apache-default.conf /etc/apache2/sites-available/000-default.conf  
  
VOLUME ["/var/www/html", "/var/log/apache2"]  
  
EXPOSE 80  
  
CMD ["/usr/bin/supervisord", "-n"]  
  

