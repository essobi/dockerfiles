# Build Docker image for Zenoss 5 Network Weathermap  
  
FROM centos:centos6  
MAINTAINER "Jan Garaj" <jan.garaj@gmail.com> (www.jangaraj.com)  
  
RUN yum install -y php php-gd php-pear rrdtool httpd wget unzip && \  
cd /tmp && \  
wget http://network-weathermap.com/files/php-weathermap-0.97c.zip && \  
unzip php-weathermap-0.97c.zip && \  
mv /tmp/weathermap/* /var/www/html/ && \  
rm -rf /tmp/weathermap/ && \  
yum remove -y wget unzip  
  
COPY php-weathermap-zenoss5-plugin/lib/* /var/www/html/  
#COPY php-weathermap-zenoss5-plugin/example/ /etc/httpd/conf.d/  
#COPY network-weathermap.conf /etc/httpd/conf.d/  
  
CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]  
  
# expose config /etc/php.ini  

