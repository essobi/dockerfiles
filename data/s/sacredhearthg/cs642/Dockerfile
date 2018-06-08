FROM centos:7  
MAINTAINER SHU  
  
RUN yum -y --setopt=tsflags=nodocs update && \  
yum -y --setopt=tsflags=nodocs install httpd && \  
yum clean all  
  
EXPOSE 80  
ADD run-httpd.sh /run-httpd.sh  
RUN chmod -v +x /run-httpd.sh  
  
CMD ["/run-httpd.sh"]  

