FROM softeu/ubuntu-apache-php-perl-mysql  
  
MAINTAINER Jindrich Vimr <jvimr@softeu.com>  
  
ENV SERVER_NAME docker-bugzilla  
  
COPY run_apache.sh /var/www/  
  
# for main web interface:  
EXPOSE 80  
WORKDIR /var/www/html  
  
CMD ["/var/www/run_apache.sh"]  

