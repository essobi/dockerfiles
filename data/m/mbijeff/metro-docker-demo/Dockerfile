  
# Using Centos 7 base image and Apache Web server  
# Version 1  
# Pull the centos image from the local repository  
FROM centos:latest  
#USER root  
MAINTAINER Gefter Chongong  
  
  
  
# Update image  
RUN yum update -y  
RUN yum install httpd -y  
  
# Add configuration file  
COPY index.html /var/www/html/  
RUN chmod -R 755 /var/www/html/  
EXPOSE 80  
# Start the service  
CMD ["-D", "FOREGROUND"]  
ENTRYPOINT ["/usr/sbin/httpd"]  

