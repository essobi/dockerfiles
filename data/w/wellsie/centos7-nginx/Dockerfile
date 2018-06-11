FROM wellsie/centos7  
MAINTAINER Jono Wells <_oj.io>  
  
RUN yum -y install nginx \  
&& yum -y clean all  
  
EXPOSE 80 443  
CMD [ "nginx", "-g", "daemon off;" ]  

