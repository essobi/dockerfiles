FROM centos:latest  
MAINTAINER github.com/blindly  
  
# Install HTTPD  
RUN yum install httpd mod_ssl php* -y  
  
# Install EPEL  
RUN rpm -i http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
  
# Install MBstring  
RUN yum install mbstring php-mbstring -y  
  
# Install Mcrypt  
RUN yum install mcrypt php-mcrypt -y  
  
# Install wget and tar  
RUN yum install wget tar -y  
  
# Add IonCube Loaders  
RUN mkdir /tmp/ioncube_install  
WORKDIR /tmp/ioncube_install  
RUN wget
http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
-O /tmp/ioncube_install/ioncube_loaders_lin_x86-64.tar.gz  
RUN tar zxf /tmp/ioncube_install/ioncube_loaders_lin_x86-64.tar.gz  
RUN mv /tmp/ioncube_install/ioncube/ioncube_loader_lin_5.3.so
/usr/lib64/php/modules  
RUN rm -rf /tmp/ioncube_install  
  
# Add Ioncube.ini  
ADD 20-ioncube.ini /etc/php.d/20-ioncube.ini  
  
# Add HTTPD Conf  
ADD httpd.conf /etc/httpd/conf/httpd.conf  
  
EXPOSE 80  
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]  

