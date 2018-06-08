FROM centos:latest  
MAINTAINER James Gaspari  
LABEL License=MIT  
  
# Updates the Container and installs httpd  
RUN yum -y update && yum clean all  
RUN yum install -y httpd openssl mod_ssl mod_proxy_html  
  
# Exposes http and https ports  
EXPOSE 80 443  
# Adds the script to clean locks  
ADD run-httpd.sh /run-httpd.sh  
RUN chmod -v +x /run-httpd.sh  
  
CMD ["/run-httpd.sh"]  

