FROM ubuntu:trusty  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install --no-install-recommends --no-install-suggests -y \  
ca-certificates \  
nginx \  
nginx-extras \  
lua-socket \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
RUN rm -Rf /etc/nginx/*  
COPY conf-nginx /etc/nginx  
  
RUN mkdir -p /var/cache/nginx/tmp  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

