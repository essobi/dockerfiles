FROM centos:latest  
  
RUN yum update -y && \  
yum install epel-release -y && \  
yum install nginx php-fpm php-mysql php-gd php-mcrypt php-xml php-mbstring -y
&& \  
yum clean all  
  
VOLUME ["/etc/nginx"]  
  
EXPOSE 80 9000  
COPY ["nginx.conf", "/etc/nginx/"]  
COPY ["startup.sh", "/home/"]  
  
ENTRYPOINT ["/home/startup.sh"]  

