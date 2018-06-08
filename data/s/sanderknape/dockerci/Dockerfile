FROM centos:7  
MAINTAINER Sander Knape  
  
COPY nginx/nginx.repo /etc/yum.repos.d/nginx.repo  
  
RUN yum -y update \  
&& yum -y install nginx curl \  
&& rm -rf /etc/nginx/conf.d  
  
COPY nginx/nginx.conf /etc/nginx/nginx.conf  
COPY app/index.html /var/www/index.html  
  
EXPOSE 80  
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]  

