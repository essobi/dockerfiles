FROM centos:centos6  
MAINTAINER github.com/blindly  
  
# Install HTTPD  
RUN yum install httpd -y  
  
# Install repo  
RUN rpm -Uvh http://mirror.webtatic.com/yum/el6/latest.rpm  
  
# Install MBstring  
RUN yum install mbstring php54w php54w-mysql php54w-mbstring -y  
  
# Install Mcrypt  
RUN yum install mcrypt php54w-mcrypt -y  
  
# Install GD, XML  
RUN yum install php54w-gd php54w-xml -y  
  
# Install EPEL  
RUN rpm -i http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
  
# Install ITK  
RUN yum install httpd-itk -y  
  
# Add HTTPD Conf  
ADD httpd.conf /etc/httpd/conf/httpd.conf  
  
# Add HTTPD System Configuration  
ADD httpd /etc/sysconfig/httpd  
  
# Add PHP.conf  
ADD php.conf /etc/httpd/conf.d/php.conf  
  
#EXPOSE 80  
#EXPOSE 443  
CMD ["/usr/sbin/httpd.itk", "-D", "FOREGROUND"]  

