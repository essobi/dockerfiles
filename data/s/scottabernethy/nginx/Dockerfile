# Dockerfile for scottabernethy/nginx  
FROM scottabernethy/debian  
  
ENV NGINX_VERSION 1.9.0-1~jessie  
  
RUN \  
apt-key adv --keyserver pgp.mit.edu --recv-keys
573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 && \  
echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
ca-certificates \  
nginx=${NGINX_VERSION} && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
VOLUME ["/var/cache/nginx"]  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

