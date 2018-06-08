FROM former03/dev03-apache-php-base-squeeze  
MAINTAINER Christian Simon <simon@swine.de>  
# Install FORMER 03 PHP 5.2  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install
former03-php-5-2  
# Set default php  
RUN for i in /usr/former03/php/5.2/bin/*; do ln -s $i
/usr/local/bin/$(basename $i) ; done  

