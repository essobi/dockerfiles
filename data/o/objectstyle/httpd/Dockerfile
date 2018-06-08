FROM centos:latest  
  
MAINTAINER Andrus Adamchik <andrus at objectstyle dot com>  
  
LABEL name=objectstyle-httpd  
  
RUN yum -y install httpd; yum -y install mod_ssl  
RUN yum -y update; yum clean all  
  
COPY run-httpd.sh /run-httpd.sh  
RUN chmod -v +x /run-httpd.sh  
  
CMD ["/run-httpd.sh"]

