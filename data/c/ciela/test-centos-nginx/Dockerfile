FROM centos:centos6  
  
MAINTAINER ciela <zektbach@gmail.com>  
  
RUN yum -y update  
RUN rpm -ihv http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-
centos-6-0.el6.ngx.noarch.rpm  
RUN yum -y install nginx  
  
EXPOSE 80  
ENTRYPOINT ["/usr/sbin/nginx", "-g", "daemon off;"]  

