FROM centos:latest  
MAINTAINER github.com/blindly  
  
# Install HTTPD  
RUN yum install httpd php* -y  
  
# Install EPEL  
RUN rpm -i http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
  
# Install git  
RUN yum install git -y  
  
# Get latest Lavern Minifield  
RUN git clone -b gh-pages https://github.com/Laverna/static-laverna
/var/www/html/public  
  
# Add HTTPD Conf  
ADD httpd.conf /etc/httpd/conf/httpd.conf  
  
EXPOSE 80  
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]  

