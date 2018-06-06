FROM debian:wheezy  
MAINTAINER Colin Densem "hello@summit360.co.uk"  
ENV DEBIAN_FRONTEND noninteractive  
  
#modified slightly for wheezy from https://github.com/nginxinc/docker-nginx  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62  
RUN echo deb http://nginx.org/packages/mainline/debian/ wheezy nginx >>
/etc/apt/sources.list.d/nginx.list  
  
ENV NGINX_VERSION 1.9.1-1~wheezy  
  
#Install and prepare for our setup model  
RUN apt-get update && \  
apt-get install -y \  
ca-certificates \  
nginx=${NGINX_VERSION} \  
procps && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log && \  
  
rm -rf /etc/nginx/*.d /etc/nginx/*_params && \  
  
mkdir -p /srv/application/public && \  
echo "Welcome to NGINX:Wheezy ${NGINX_VERSION}" >>
/srv/application/public/index.html  
  
COPY config/etc /etc  
  
VOLUME ["/srv/application"]  
  
# EXPOSE  
EXPOSE 80 443  
CMD ["nginx"]  
  

