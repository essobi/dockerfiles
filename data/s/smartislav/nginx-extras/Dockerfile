FROM debian:sid  
  
MAINTAINER Ilya Epifanov <elijah.epifanov@gmail.com>  
  
ENV NGINX_VERSION 1.9.3-1  
RUN apt-get update &&\  
apt-get -y upgrade &&\  
apt-get install -y ca-certificates "nginx-extras=$NGINX_VERSION" &&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
VOLUME ["/var/cache/nginx"]  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

