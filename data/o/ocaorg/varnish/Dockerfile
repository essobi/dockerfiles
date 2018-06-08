# Forked from million12/varnish  
FROM centos:centos7  
  
RUN yum update -y && \  
yum install -y epel-release && \  
yum install -y varnish && \  
yum install -y libmhash-devel && \  
yum clean all  
  
ENV CACHE_SIZE 2g  
ENV VARNISHD_PARAMS -t 120  
COPY config.vcl /config.vcl  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT /entrypoint.sh  
  
EXPOSE 80  

