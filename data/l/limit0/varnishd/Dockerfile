FROM centos:7  
RUN yum -y update && yum install -y epel-release  
  
ARG VERSION=4.0.5  
RUN yum -y install varnish-${VERSION}  
  
VOLUME /etc/varnish  
WORKDIR /etc/varnish  
  
EXPOSE 80  
ENTRYPOINT [ "/sbin/varnishd", "-Ff", "/etc/varnish/default.vcl" ]  

