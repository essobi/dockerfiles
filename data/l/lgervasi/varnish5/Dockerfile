FROM centos:centos7  
MAINTAINER Luca Gervasi <varnish5@ashetic.net>  
  
ADD varnishcache5.repo /etc/yum.repos.d/varnishcache5.repo  
ADD start.sh /start.sh  
  
# Needed to satisfy jemalloc library  
RUN yum -y install epel-release && \  
yum install -y varnish && \  
yum clean all && \  
rm -rf /var/cache/yum && \  
chmod 755 /start.sh  
  
ENV VCL_CONFIG /etc/varnish/default.vcl  
ENV CACHE_SIZE 64m  
ENV VARNISHD_PARAMS -p thread_pool_min=5 -p thread_pool_max=500 -p
thread_pool_timeout=300  
CMD /start.sh  
EXPOSE 80  
EXPOSE 6086  

