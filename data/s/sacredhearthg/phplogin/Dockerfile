FROM centos:7  
MAINTAINER SHU  
  
RUN yum -y --setopt=tsflags=nodocs update && \  
yum -y --setopt=tsflags=nodocs install httpd && \  
yum -y install php php-mysql &&\  
yum clean all  
  
EXPOSE 80  
# Simple startup script to avoid some issues observed with container restart  
ADD run-httpd.sh /run-httpd.sh  
ADD index.html /var/www/html/index.html  
ADD gamep.jpg /var/www/html/gamep.jpg  
ADD gamep.jpg /gamep.jpg  
  
RUN chmod -v +x /run-httpd.sh  
  
CMD ["/run-httpd.sh"]  

