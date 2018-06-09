FROM centos:7  
MAINTAINER Swapnil Jain <swapnil@linux.com>  
  
RUN yum -y install epel-release && rm -rf /var/cache/yum/* && yum clean all  
RUN yum -y install php php-opcache php-pdo php-mbstring php-mcrypt php-mysql
wget httpd openssl mod_ssl && rm -rf /var/cache/yum/* && yum clean all  
EXPOSE 80  
EXPOSE 443  
CMD ["/usr/sbin/apachectl", "-DFOREGROUND"]  

