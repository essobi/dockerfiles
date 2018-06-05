FROM centos:latest  
MAINTAINER github.com/blindly  
  
# Install HTTPD  
RUN yum install httpd mod_ssl php* -y  
  
# Install EPEL  
RUN rpm -i http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
  
# Install MBstring and Mcrypt  
RUN yum install mbstring php-mbstring mcrypt php-mcrypt -y  
  
# Install ITK  
RUN yum install httpd-itk -y  
  
# Add HTTPD Conf  
ADD httpd.conf /etc/httpd/conf/httpd.conf  
  
# Add HTTPD System Configuration  
ADD httpd /etc/sysconfig/httpd  
  
# Add PHP.conf  
ADD php.conf /etc/httpd/conf.d/php.conf  
  
EXPOSE 80  
CMD ["/usr/sbin/httpd.itk", "-D", "FOREGROUND"]  

