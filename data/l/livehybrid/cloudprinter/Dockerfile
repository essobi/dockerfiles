#FROM livehybrid/apache2php  
FROM php:5.6-apache  
  
RUN apt-get -yq update && \  
apt-get -yqq install git nano  
  
MAINTAINER William Searle "will@livehybrid.com"  
  
  
RUN rm -rf /var/www/html  
  
RUN sed -i.bak "s/\${APACHE_LOG_DIR}\/\\(error\|access\\).log/\/dev\/stdout/g"
/etc/apache2/sites-available/000-default.conf  
RUN sed -i.bak "s/\${APACHE_LOG_DIR}\/access.log/\/dev\/stdout/g"
/etc/apache2/sites-available/default-ssl.conf  
RUN sed -i.bak "s/\${APACHE_LOG_DIR}\/error.log/\/dev\/stdout/g"
/etc/apache2/apache2.conf  
RUN sed -i.bak "s/\${APACHE_LOG_DIR}\/other_vhosts_access.log/\/dev\/stdout/g"
/etc/apache2/conf-available/other-vhosts-access-log.conf  
  
  
  
RUN git clone https://livehybrid@bitbucket.org/livehybrid/bowl_cloudprint.git
/var/www/html  

