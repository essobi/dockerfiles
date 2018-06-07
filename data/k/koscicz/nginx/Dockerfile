FROM modularitycontainers/boltron-preview:latest  
  
# Image metadata  
ENV NAME=nginx \  
NGINX_VERSION=1.10.3 \  
VERSION=0 \  
RELEASE=1 \  
ARCH=x86_64  
  
# Labels  
LABEL com.redhat.component="$NAME" \  
name="$FGC/$NAME" \  
summary="nginx is a web server." \  
description="nginx is a web server, which can also be used as a reverse proxy,
load balancer and HTTP cache." \  
version="$VERSION" \  
release="$RELEASE.$DISTTAG" \  
architecture="$ARCH" \  
usage="docker run -p 8080:80 -v <DIR>:/usr/share/nginx/html/" \  
atomic.has_install_files="true" \  
io.k8s.description="nginx is a web server, which can also be used as a reverse
proxy, load balancer and HTTP cache." \  
io.k8s.display-name="nginx" \  
io.openshift.expose-services="80:http" \  
io.openshift.tags="http,proxy,server,nginx"  
  
# Add neccessary configuration files  
COPY files/nginx.conf /etc/nginx/nginx.conf  
COPY files/service.template /exports/hostfs/usr/lib/systemd/system/nginx-
container.service  
COPY root/* /  
  
RUN dnf install -y --nodocs nginx  
  
RUN mkdir -p /exports/hostfs/{usr/share,etc} && \  
cp -ar /usr/share/nginx /exports/hostfs/usr/share/ && \  
cp -ar /etc/nginx /exports/hostfs/etc && \  
mkdir -p /var/www/html && \  
chmod +x /var/www/html  
  
# Export port for nginx frontend  
EXPOSE 80  
# Start nginx  
CMD ["/usr/sbin/nginx"]  

