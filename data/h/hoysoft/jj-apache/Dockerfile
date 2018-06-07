FROM centos:7.3.1611  
MAINTAINER Justin.h<justin@5nas.cc>  
  
#修改容器时区  
RUN rm -rf /etc/localtime  
RUN ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
RUN yum --setopt=tsflags=nodocs -y update  
RUN yum --setopt=tsflags=nodocs -y install httpd \  
&& yum clean all  
  
VOLUME /var/www/html  
  
WORKDIR /var/www/html  
  
COPY httpd.conf /etc/httpd/conf/httpd.conf  
EXPOSE 80  
CMD ["httpd", "-D", "FOREGROUND"]  
  

