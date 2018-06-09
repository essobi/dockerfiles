FROM fedora:21  
MAINTAINER Colin Kenny  
  
RUN yum -y install httpd && yum -y update; yum clean all  
  
EXPOSE 80  
VOLUME /home/colin/  
ENTRYPOINT [ "/usr/sbin/httpd" ]

