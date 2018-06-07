FROM xavren/php:7.2  
MAINTAINER Xavier RENAUDIN <renaudin.xavier@gmail.com>  
  
ADD rootfs /  
RUN yum install -y php-twig && yum --enablerepo=remi install -y phpunit  
  
ENTRYPOINT ["/init"]  

