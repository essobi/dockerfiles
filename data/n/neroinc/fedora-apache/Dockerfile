#  
# fedora-apache-php  
#  
FROM fedora:20  
# Update distribution  
RUN yum -y update; yum clean all  
  
# Need Apache in simplest way  
RUN yum -y install httpd; yum clean all  
RUN mkdir -p /var/www/html  
RUN mkdir -p /var/log/httpd  
  
# Create Apache test page  
RUN echo "Apache set up successfully." > /var/www/html/index.html  
  
# Copy apache run script  
ADD httpd-run /bin/httpd-run  
  
# Done  
EXPOSE 80  
CMD ["/bin/httpd-run"]  

