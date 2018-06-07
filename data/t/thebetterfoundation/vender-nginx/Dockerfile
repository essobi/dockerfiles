FROM ubuntu:14.04  
MAINTAINER colhom@gmail.com  
RUN apt-get update  
RUN apt-get install -y nginx-extras nginx ca-certificates  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
VOLUME ["/var/cache/nginx"]  
  
EXPOSE 80  
ADD nginx_prod.conf /etc/nginx/nginx.conf  
  
CMD ["-g", "daemon off;"]  
ENTRYPOINT ["nginx"]  

