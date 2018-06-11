FROM centos:centos6  
MAINTAINER tyler.hoadley[AT]computersthatwork[DOT]ca  
RUN yum update -y  
RUN yum install -y httpd  
RUN yum clean all  
RUN rm -fr /var/cache/yum/*  
ONBUILD ADD . /var/www/html/  
EXPOSE 80  
ENTRYPOINT ["/usr/sbin/httpd"]  
CMD ["-D", "FOREGROUND"]  

