FROM alizarion/centos7base:latest  
  
MAINTAINER Selim BENSENOUCI "selim@openlinux.fr"  
RUN yum update -y  
RUN cd /tmp  
RUN wget
https://github.com/pingidentity/mod_auth_openidc/releases/download/v1.8.6/mod_auth_openidc-1.8.6-1.el7.centos.x86_64.rpm  
  
RUN yum -y install httpd mod_auth_openidc-1.8.6-1.el7.centos.x86_64.rpm  
  
RUN rm -f /tmp/mod_auth_openidc-1.8.6-1.el7.centos.x86_64.rpm  
  
RUN yum clean all  
  
ADD httpd-foreground /usr/local/bin/  
  
RUN chmod +x /usr/local/bin/httpd-foreground  
RUN rm -rf /etc/httpd/logs  
RUN mkdir /etc/httpd/logs  
  
EXPOSE 80  
CMD ["httpd-foreground"]  

