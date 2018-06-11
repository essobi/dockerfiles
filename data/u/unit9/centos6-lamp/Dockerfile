FROM unit9/centos6:latest  
MAINTAINER Kamil Cholewiński <kamil.cholewinski@unit9.com>  
  
RUN yum install -y \  
httpd \  
php \  
php-mysql \  
&& yum clean all  
  
COPY httpd.run /etc/service/httpd/run  
COPY httpd.conf /etc/httpd/conf/httpd.conf  

