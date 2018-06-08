FROM nott/baseimage:latest  
MAINTAINER Stas Rudakou "stas@garage22.net"  
RUN yum -y update; yum clean all;  
RUN yum -y install nginx  
  
ADD confd /etc/confd  
ADD bin/confd-watch /usr/local/bin/confd-watch  
RUN chmod +x /usr/local/bin/confd-watch  
  
EXPOSE 80  
EXPOSE 443  
CMD ["/usr/local/bin/confd-watch"]  

