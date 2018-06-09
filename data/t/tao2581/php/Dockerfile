FROM tetraweb/php  
  
MAINTAINER Tao2581 <tao2581@126.com>  
  
  
# Install the zip  
RUN apt-get -y update && \  
apt-get -y upgrade && \  
apt-get -y install zip unzip  
  
# Install composer  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
&& \  
php composer-setup.php && \  
php -r "unlink('composer-setup.php');"  

