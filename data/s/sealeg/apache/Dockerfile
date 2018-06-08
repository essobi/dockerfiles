FROM centos:7  
MAINTAINER sealeg <https://github.com/sealeg>  
  
RUN yum -y update \  
&& yum -y install httpd \  
&& yum clean all  
  
EXPOSE 80 443  
COPY httpd.conf /etc/httpd/conf/httpd.conf  
  
VOLUME ["/config", "/data", "/logs"]  
  
COPY entrypoint.sh /  
RUN chmod u+x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

