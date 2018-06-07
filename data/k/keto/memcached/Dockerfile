FROM centos:centos7  
  
MAINTAINER Mikael Keto  
  
# install memcached  
RUN yum -y install memcached && yum clean all && rm -rf /var/cache/yum  
  
EXPOSE 11211  
ENTRYPOINT ["memcached"]  
CMD ["-u", "memcached", "-v"]  

