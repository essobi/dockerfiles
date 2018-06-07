FROM debian:jessie  
  
ENV NGINX_VERSION 1.9.14-1~jessie  
  
ADD packages/nginx_${NGINX_VERSION}_amd64.deb /tmp/nginx.deb  
  
RUN apt-get update && \  
apt-get install -y ca-certificates && \  
dpkg -i /tmp/nginx.deb && \  
rm -rf /var/lib/apt/lists/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
VOLUME ["/var/cache/nginx"]  
VOLUME ["/var/cache/pagespeed"]  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

