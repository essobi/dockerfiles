FROM centos:centos7  
MAINTAINER Przemyslaw Ozgo linux@ozgo.info, Marcin Ryzycki marcin@m12.io, Joe
Constant joe@joeconstant.com  
  
RUN yum update -y && \  
yum install -y epel-release && \  
yum install -y https://repo.varnish-cache.org/redhat/varnish-4.0.el6.rpm && \  
yum install -y varnish && \  
yum install -y libmhash-devel && \  
yum clean all  
  
ADD start.sh /start.sh  
  
ADD varnish-conf/default.vcl /etc/varnish/default.vcl  
ADD varnish-conf/varnish /etc/sysconfig/varnish  
ENV VCL_CONFIG /etc/varnish/default.vcl  
ENV CACHE_SIZE 64m  
ENV VARNISHD_PARAMS -p default_ttl=3600 -p default_grace=3600  
  
CMD /start.sh  
EXPOSE 80  
EXPOSE 6082  

