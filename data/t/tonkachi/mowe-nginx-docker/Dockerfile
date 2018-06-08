FROM centos:centos7  
MAINTAINER FURUSAWA MAKOTO violafuru@gmail.com  
  
ENV NGINX_VERSION 1.8.0  
# Install packages for building ruby  
RUN yum install -y openssl openssl-devel \  
pcre pcre-devel \  
zlib zlib-devel \  
gcc tar  
  
# make dir, and user  
RUN adduser mowe  
RUN mkdir -p /apps/src  
RUN chown -R mowe:mowe /apps  
USER mowe  
  
# Install nginx  
WORKDIR /apps/src  
RUN curl -O http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz ;\  
tar zxvf nginx-${NGINX_VERSION}.tar.gz  
WORKDIR /apps/src/nginx-${NGINX_VERSION}  
RUN ./configure --prefix=/apps/nginx --with-http_ssl_module --with-
http_spdy_module ;\  
make; make install  
ADD ./nginx.conf /apps/nginx/conf/nginx.conf  
  
# forward request and error logs to docker log collector  
#RUN ln -sf /dev/stdout /apps/nginx/logs/access.log  
#RUN ln -sf /dev/stderr /apps/nginx/logs/error.log  
# Run  
USER root  
EXPOSE 80 443  
CMD ["/apps/nginx/sbin/nginx", "-g", "daemon off;"]  

