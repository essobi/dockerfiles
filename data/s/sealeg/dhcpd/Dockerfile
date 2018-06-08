FROM centos:7  
MAINTAINER Giles Thomas <giles@lemonman.org.uk>  
  
RUN yum -y update && \  
yum -y install dhcp && \  
yum clean all  
  
COPY entrypoint.sh /  
RUN chmod u+x /entrypoint.sh  
  
VOLUME ["/data"]  
  
ENTRYPOINT ["/entrypoint.sh"]  
  

