FROM centos:7  
ADD ./nginx.repo /etc/yum.repos.d/nginx.repo  
  
RUN yum install -y nginx  
  
RUN rm /etc/nginx/nginx.conf  
  
RUN ln -sf /var/www/conf/nginx.conf /etc/nginx/nginx.conf  
  
CMD ["nginx", "-g", "daemon off;"]  
  
EXPOSE 80  

