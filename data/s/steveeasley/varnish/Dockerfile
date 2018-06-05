FROM centos:6  
MAINTAINER Steve Easley <steve.easley@gmail.com>  
  
RUN yum update -y && \  
yum install -y epel-release && \  
rpm --nosignature -i https://repo.varnish-cache.org/redhat/varnish-4.1.el6.rpm
&& \  
yum install -y varnish && \  
yum clean all  
  
EXPOSE 80 6082  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["varnishd", "-F", "-a", ":80", "-T", ":6082", "-f",
"/etc/varnish/default.vcl", "-s", "malloc,1G"]  

