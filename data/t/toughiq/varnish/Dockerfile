FROM centos:7  
MAINTAINER toughiq@gmail.com  
# idea based on https://hub.docker.com/r/million12/varnish/  
RUN yum -y update \  
&& yum install -y epel-release \  
&& rpm --nosignature -i https://repo.varnish-
cache.org/redhat/varnish-4.1.el7.rpm \  
&& yum install -y varnish \  
&& yum clean all  
  
ADD start.sh /start.sh  
  
ENV VCL_CONFIG /etc/varnish/default.vcl  
ENV VCL_SECRET /etc/varnish/secret  
ENV CACHE_SIZE 64m  
ENV VARNISHD_PARAMS -a :80 -T localhost:6082 -p default_ttl=3600 -p
default_grace=3600  
CMD /start.sh  
EXPOSE 80  

