FROM ubuntu:16.04  
MAINTAINER Deepak Sinnamani <skdeepak.nz@gmail.com>  
  
# Ensure UTF-8  
RUN apt-get update && apt-get -y install locales  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# Setting up repositories  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq install \  
software-properties-common \  
python-software-properties  
RUN add-apt-repository ppa:ondrej/php -y  
  
# Install base packages  
RUN apt-get remove php7.0  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq install \  
php7.1 \  
curl \  
apache2 \  
libapache2-mod-php7.1 \  
php7.1-mysql \  
php7.1-mcrypt \  
php7.1-mbstring \  
php7.1-gd \  
php7.1-curl \  
php-pear \  
php-apcu \  
php-soap \  
php-zip  
  
# SSL packages  
RUN apt-get -yq install \  
libcurl4-openssl-dev \  
pkg-config \  
libssl-dev \  
libsslcommon2-dev  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Clean the apt cache  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN /usr/sbin/phpenmod mcrypt  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf && \  
sed -i "s/variables_order.*/variables_order = \"EGPCS\"/g"
/etc/php/7.1/apache2/php.ini  
  
ENV ALLOW_OVERRIDE **False**  
  
# Add image configuration and scripts  
ADD scripts/run.sh /run.sh  
RUN chmod 755 /*.sh  
  
# Configure /app folder with sample app  
RUN mkdir -p /app && rm -fr /var/www/html && ln -s /app /var/www/html  
ADD sample/ /app  
  
RUN usermod -u 33 www-data  
  
RUN a2enmod expires  
RUN a2enmod headers  
RUN phpenmod mcrypt  
RUN phpenmod mbstring  
RUN a2enmod proxy  
RUN a2enmod proxy_http  
RUN a2enmod proxy_ajp  
RUN a2enmod rewrite  
RUN a2enmod deflate  
RUN a2enmod proxy_balancer  
RUN a2enmod proxy_connect  
RUN a2enmod xml2enc  
RUN a2enmod proxy_html  
  
# Custom config to handle logs  
ADD config/apache.conf /etc/apache2/sites-available/000-default.conf  
RUN service apache2 restart  
  
EXPOSE 80  
WORKDIR /app  
CMD ["/run.sh"]

