FROM ubuntu:vivid  
MAINTAINER Christophe Burki, christophe.burki@gmail.com  
  
# Install system requirements  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y \  
apache2-mpm-prefork \  
curl \  
libapache2-mod-php5 \  
mysql-client \  
php5-curl \  
php5-gd \  
php5-imagick \  
php5-intl \  
php5-mcrypt \  
php5-memcache \  
php5-mysql \  
php5-ps \  
php5-pspell \  
php5-xmlrpc \  
python-pip \  
pwgen  
  
# Configure locales and timezone  
RUN locale-gen en_US.UTF-8 en_GB.UTF-8 fr_CH.UTF-8  
RUN cp /usr/share/zoneinfo/Europe/Zurich /etc/localtime  
RUN echo "Europe/Zurich" > /etc/timezone  
  
# Apache config  
COPY configs/virtualhost.conf /etc/apache2/sites-available/default.conf  
RUN ln -sf /etc/apache2/sites-available/default.conf /etc/apache2/sites-
enabled/000-default.conf  
  
# Supervisor config  
RUN mkdir /var/log/supervisor  
RUN pip install supervisor  
COPY configs/supervisord.conf /etc/supervisord.conf  
  
# Startup script  
COPY scripts/start.sh /opt/start.sh  
RUN chmod 755 /opt/start.sh  
  
CMD ["/bin/bash", "/opt/start.sh"]  

