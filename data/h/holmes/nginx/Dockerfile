#  
# Based on https://github.com/nginxinc/docker-nginx  
#  
FROM centos:centos7  
MAINTAINER Holmes Team <holmes@holmesdoc.com>  
  
ENV NGINX_VERSON 1.7.7  
RUN yum install -y openssl  
  
RUN rpm -Uhv
http://nginx.org/packages/mainline/centos/7/x86_64/RPMS/nginx-${NGINX_VERSON}-1.el7.ngx.x86_64.rpm  
  
VOLUME ["/var/cache/nginx"]  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]

