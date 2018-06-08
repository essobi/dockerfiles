FROM former03/dev03-apache-php-base-wheezy  
MAINTAINER Christian Simon <simon@swine.de>  
# Install FORMER 03 PHP 5.5  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install former03-php-5-5  
# Set default php  
RUN for i in /usr/former03/php/5.5/bin/*; do ln -s $i
/usr/local/bin/$(basename $i) ; done  

