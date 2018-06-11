FROM tubssp/docker-ubuntu  
MAINTAINER Andreas Lemke <andreas.lemke@tu-braunschweig.de>  
  
# Install everything needed  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get -y install git && \  
apt-get -y install apache2 libapache2-mod-php5 php5 php5-cli php5-curl php5-gd
php5-imagick php5-sqlite php5-intl php5-mcrypt php5-xdebug php5-apcu  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  

