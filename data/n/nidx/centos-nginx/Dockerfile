FROM centos  
MAINTAINER Jon Dell  
ADD nginx.repo /etc/yum.repos.d/nginx.repo  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD default.conf /etc/nginx/conf.d/default.conf  
ADD run_nginx.sh /root/run_nginx.sh  
RUN chmod +x /root/run_nginx.sh  
RUN yum install -y nginx  
VOLUME ["/var/log/nginx"]  
EXPOSE 80  
CMD ["/root/run_nginx.sh"]  

