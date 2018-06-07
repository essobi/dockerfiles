FROM fvigotti/env-fatubuntu-supervisord  
  
ENV NGINX_UBUNTU_DIST trusty  
ENV NGINX_UBUNTU_ARCHITECTURE amd64  
  
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62  
RUN echo "deb http://nginx.org/packages/mainline/ubuntu/ ${NGINX_UBUNTU_DIST}
nginx" >> /etc/apt/sources.list  
  
ENV NGINX_VERSION "1.9.9-1~trusty"  
#RUN export NGINX_VERSION=$(curl --silent
"http://nginx.org/packages/mainline/ubuntu/dists/${NGINX_UBUNTU_DIST}/nginx/binary-${NGINX_UBUNTU_ARCHITECTURE}/Packages"
| grep -A 1 -e 'Package: nginx$' | grep -e '^Version:' | sed 's/^Version: //')
&& \  
RUN echo "NGINX_VERSION=${NGINX_VERSION}" && apt-get update && apt-get upgrade
-y && \  
apt-get install -y ca-certificates nginx=${NGINX_VERSION} && \  
rm -rf /var/lib/apt/lists/*  
  
# delete conf.d/default.conf && prepare base dirs structure  
RUN rm -rf /etc/nginx/*.d && \  
mkdir -p /etc/nginx/addon.d /etc/nginx/conf.d /etc/nginx/host.d
/etc/nginx/nginx.d && \  
mkdir -p /data/http/ /data/logs/ /data/config/  
  
# add /etc/nginx configuration, but do not overwrite existing default nginx
configuration (Exception for /etc/nginx/nginx.conf )  
ADD etc /etc  
  

