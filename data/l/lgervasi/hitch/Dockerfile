FROM centos:centos7  
MAINTAINER Luca Gervasi <docker@ashetic.net>  
  
ADD start.sh /start.sh  
  
# Needed to satisfy jemalloc library  
RUN yum -y install epel-release && \  
yum install -y hitch && \  
yum clean all && \  
rm -rf /var/cache/yum && \  
chmod 755 /start.sh  
  
CMD /start.sh  
EXPOSE 443  

