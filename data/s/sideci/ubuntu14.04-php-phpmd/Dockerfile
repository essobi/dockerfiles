FROM quay.io/actcat/buildpack_php:latest  
  
MAINTAINER Vexus2 <hikaru.tooyama@gmail.com>  
  
# install phpmd latest via phpmd site. PHP Mess Dedector  
RUN wget -c http://static.phpmd.org/php/latest/phpmd.phar  
RUN mv phpmd.phar /usr/bin/phpmd  
RUN chmod +x /usr/bin/phpmd  
RUN phpmd --version  

