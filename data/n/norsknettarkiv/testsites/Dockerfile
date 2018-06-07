FROM centos:7  
MAINTAINER Norsk Nettarkiv  
  
RUN yum -y --setopt=tsflags=nodocs update && \  
yum -y --setopt=tsflags=nodocs install httpd dnsmasq bind-utils && \  
yum clean all  
  
EXPOSE 80  
EXPOSE 53  
RUN mkdir -p /var/www/html/test/  
  
ADD dnsmasq.conf /etc/  
ADD httpd.conf /etc/httpd/conf/  
ADD apache-icon.gif /var/www/html/test/static.com/  
ADD bigpic.png /var/www/html/test/static.com/  
ADD create_sites.sh /var/www/html/test/  
  
# Simple startup script to avoid some issues observed with container restart  
ADD run-httpd.sh /run-httpd.sh  
RUN chmod -v +x /run-httpd.sh && \  
chmod +x /var/www/html/test/create_sites.sh  
ENV NUMBER_OF_SITES='2500' \  
DOMAIN_DEPTH='5'  
RUN ["/var/www/html/test/create_sites.sh"]  
CMD ["/run-httpd.sh"]  
  

