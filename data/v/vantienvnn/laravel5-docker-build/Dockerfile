FROM ubuntu:16.04  
MAINTAINER "Tien Vo" <tienvv.it@gmail.com>  
  
# Add locales after locale-gen as needed  
# Upgrade packages on image  
# Preparations for sshd  
RUN locale-gen en_US.UTF-8 \  
&& apt-get -q update \  
&& apt-get install -y net-tools \  
software-properties-common python-software-properties  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /home/jenkins  
  
# Set user jenkins to the image  
RUN groupadd -g 117 jenkins \  
&& useradd -g 117 -u 112 -d /home/jenkins -s /bin/sh jenkins \  
&& echo "jenkins:jenkins" | chpasswd  
  
# Volume for cache  
VOLUME /home/jenkins  
  
# run install git, curl  
RUN add-apt-repository ppa:ondrej/php \  
&& apt-get update && apt-get install -y unzip git curl \  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get install -y nodejs  
  
# run install mysql-server  
RUN apt-get install -y mysql-server  
  
# run install php  
RUN apt-get install -y php5.6-fpm php5.6-curl php5.6-gd php5.6-geoip \  
php5.6-imap php5.6-json php5.6-ldap php5.6-mcrypt php5.6-redis \  
php5.6-mbstring php5.6-xml php5.6-pdo php5.6-pdo-mysql  
  
# Configure PHP-FPM  
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/"
/etc/php/5.6/fpm/php.ini \  
&& sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php/5.6/fpm/php.ini
\  
&& sed -i "s/display_errors = Off/display_errors = stderr/"
/etc/php/5.6/fpm/php.ini \  
&& sed -i "s/upload_max_filesize = 2M/upload_max_filesize = 30M/"
/etc/php/5.6/fpm/php.ini  
  
# run install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Create cache home  
RUN mkdir -p "/home/jenkins" \  
&& chown jenkins:jenkins "/home/jenkins" \  
&& chmod 0777 "/home/jenkins"  
  
ADD config/init-start.sh /init-start.sh  
RUN chmod +x /init-start.sh  
# Default command  
ENTRYPOINT ["/init-start.sh"]

