FROM centos:7  
MAINTAINER https://github.com/imehedi/CLAP7/  
LABEL Vendor="CAP7"  
LABEL License=GPLv3  
LABEL Version=0.1  
  
# Add & enable EPEL, REMI (for PHP7) Repos  
RUN yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm && \  
yum install -y http://rpms.remirepo.net/enterprise/remi-release-7.rpm && \  
yum install -y yum-utils deltarpm && \  
yum-config-manager --enable remi-php72 && \  
yum update -y  
  
RUN yum install -y php72-php-fpm php72-php-gd php72-php-json php72-php-
mbstring php72-php-mysqlnd php72-php-xml php72-php-xmlrpc php72-php-opcache
httpd  
RUN systemctl enable httpd  
EXPOSE 80 443 8443 8080  

