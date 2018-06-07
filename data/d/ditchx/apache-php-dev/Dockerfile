FROM ubuntu:12.04.5  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -yqq \  
curl \  
apt-utils \  
libapache2-mod-php5 \  
php5 \  
apache2-mpm-prefork \  
php5-dev \  
php-apc \  
php-pear \  
php5-cgi \  
php5-cli \  
php5-common \  
php5-curl \  
php5-gd \  
php5-imap \  
php5-mcrypt \  
php5-memcache \  
php5-memcached \  
php5-mysqlnd \  
php5-snmp \  
php5-xmlrpc \  
php5-xsl  
  
  
# Install wkhtmltopdf 0.12.1 and its dependencies  
RUN apt-get install -yqq \  
fontconfig \  
libxext6 \  
libxrender1  
RUN curl --output wkhtmltox-0.12.1_linux-precise-amd64.deb --location
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.1/wkhtmltox-0.12.1_linux-
precise-amd64.deb  
RUN dpkg -i wkhtmltox-0.12.1_linux-precise-amd64.deb  
  
# Install pdftk and its dependencies  
RUN curl --output gcc-4.9-base_4.9.2-10ubuntu13_amd64.deb --location
http://launchpadlibrarian.net/203276913/gcc-4.9-base_4.9.2-10ubuntu13_amd64.deb  
RUN dpkg -i gcc-4.9-base_4.9.2-10ubuntu13_amd64.deb  
  
RUN apt-get install -yqq \  
libgcj-common \  
libasound2  
  
RUN curl --output libgcj15_4.9.2-10ubuntu13_amd64.deb --location
http://launchpadlibrarian.net/203276965/libgcj15_4.9.2-10ubuntu13_amd64.deb  
RUN dpkg -i libgcj15_4.9.2-10ubuntu13_amd64.deb  
  
RUN curl --output pdftk_2.02-2_amd64.deb --location
https://launchpad.net/ubuntu/+archive/primary/+files/pdftk_2.02-2_amd64.deb  
RUN dpkg -i pdftk_2.02-2_amd64.deb  
  
# Install imagemagick  
RUN apt-get install -yqq imagemagick  
  
# Setup apache server config  
COPY default /etc/apache2/sites-available/default  
  
# Copy dev site's php.init config  
COPY php.ini /etc/php5/apache2/php.ini  
  
RUN a2enmod rewrite  
  
EXPOSE 80  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

