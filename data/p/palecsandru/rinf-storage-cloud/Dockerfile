FROM centos:centos7.4.1708  
  
###############################################################################  
# System dependencies  
###############################################################################  
RUN yum --enablerepo=extras install epel-release -y  
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm  
RUN yum update -y && yum install -y \  
vim \  
httpd \  
php70u \  
php70u-cli \  
php70u-json \  
php70u-mysqlnd  
  
COPY php.ini /etc  
COPY index.php /  
COPY start.sh /  
RUN chmod 777 /*.sh; \  
chmod 777 /*.php; \  
chmod 777 /etc/php.ini; \  
sync  
  
EXPOSE 80  
VOLUME ["/var/www/html/"]  
###############################################################################  
# Make sure that everything is written to disk  
###############################################################################  
RUN sync  
  
###############################################################################  
# Start container services  
###############################################################################  
ENTRYPOINT /start.sh && /bin/bash

