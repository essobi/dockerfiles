FROM repositoryjp/centos:6.7  
MAINTAINER Shinya Kinoshita <skinoshita@repositories.jp>  
  
LABEL name="Nginx 1.8.1 Image" \  
description="The image for creating docker container of Nginx 1.8.1 Server." \  
distribution="centos" \  
centos-version="6.7" \  
nginx-version="1.8.1" \  
vendor="REPOSITORY <http://www.repositories.jp>" \  
license="MIT"  
  
ENV NGINX_VERSION 1.8.1  
USER root  
WORKDIR /tmp  
  
# Install Nginx.  
RUN wget
http://nginx.org/packages/centos/6/x86_64/RPMS/nginx-${NGINX_VERSION}-1.el6.ngx.x86_64.rpm
&& \  
rpm -U nginx-${NGINX_VERSION}-1.el6.ngx.x86_64.rpm  
COPY etc/nginx/nginx.conf /etc/nginx/nginx.conf  
  
# Configure container.  
EXPOSE 80 443  
VOLUME /etc/nginx/conf.d /usr/share/nginx /var/log/nginx  
  
USER root  
WORKDIR /root  
  
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]  

