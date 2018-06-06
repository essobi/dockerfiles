FROM php:5-apache  
  
RUN apt-get update  
  
# mysqli  
RUN docker-php-ext-install mysqli  
  
# ldap  
RUN apt-get install -y \  
libldap2-dev && \  
docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ && \  
docker-php-ext-install ldap  
  
# mcrypt  
RUN apt-get install -y \  
libmcrypt-dev && \  
docker-php-ext-install -j$(nproc) mcrypt  
  
# soap  
RUN apt-get install -y \  
libxml2-dev && \  
docker-php-ext-install soap  
  
# json  
RUN docker-php-ext-install json  
  
# gd  
RUN apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install gd && \  
docker-php-ext-enable gd  
  
# Graphviz  
RUN apt-get install -y \  
graphviz  
  
# cli  
# Não incluído  
RUN apt-get install -y \  
wget unzip  
  
# zip  
RUN apt-get install -y \  
zlib1g-dev && \  
docker-php-ext-install zip  
  
# Define session temp path  
RUN echo "session.save_path = /tmp" > /usr/local/etc/php/conf.d/session.ini  
  
# Download latest iTop  
RUN wget -O /tmp/itop.zip --trust-server-names
https://sourceforge.net/projects/itop/files/latest/download  
RUN unzip /tmp/itop.zip 'web/*' -d /var/www  
RUN rm -rf /var/www/html; mv /var/www/web /var/www/html  
WORKDIR /var/www/html  
  
# Download DataModel Tookit  
RUN wget -O /tmp/itop-datamodel-toolkit.zip --trust-server-names
https://www.combodo.com/documentation/iTopDataModelToolkit-2.3.zip  
RUN unzip /tmp/itop-datamodel-toolkit.zip -d .  
  
# Download Extension teemip  
RUN wget -O /tmp/teemip.zip --trust-server-names
https://sourceforge.net/projects/teemip/files/teemip%20-%20an%20iTop%20module/2.2.1/teemip-
core-ip-mgmt-2.2.1.zip/download  
RUN unzip /tmp/teemip.zip -d extensions/  
  
# Download Extension teemip-discovery  
RUN wget -O /tmp/teemip-discovery.zip --trust-server-names
http://wiki.teemip.com/extensions/teemip-discovery-module-0.1.1.zip  
RUN ls extensions/  
RUN unzip /tmp/teemip-discovery.zip -d extensions/  
  
# Download Extension itop-team-description  
RUN wget -O /tmp/itop-team-description.zip --trust-server-names
https://github.com/jonatasrenan/itop-team-
description/archive/9d23702e0553cd8559f325a4d5655e1e321abaf0.zip  
RUN unzip /tmp/itop-team-description.zip -d extensions/  
RUN mv extensions/itop-team-description-* extensions/itop-team-description  
  
# Check permissions  
RUN chown www-data:www-data -R /var/www/html  
  
# Clean Up  
RUN rm -rf /var/lib/apt/lists/* /tmp/*  
  
EXPOSE 80  

