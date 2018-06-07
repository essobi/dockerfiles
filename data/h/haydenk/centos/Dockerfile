FROM centos:7  
RUN yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm && yum update -y && rm -rf /var/cache/yum/*  
RUN yum install -y httpd && yum update -y && yum clean all && rm -rf
/var/cache/yum/*  
  
EXPOSE 80  
EXPOSE 443  
VOLUME ["/var/www/html"]  
  
# Simple startup script to avoid some issues observed with container restart  
ADD run-httpd.sh /run-httpd.sh  
RUN chmod -v +x /run-httpd.sh  
  
CMD ["/run-httpd.sh"]  

