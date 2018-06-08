FROM ubuntu:14.04  
MAINTAINER Matthew Wedgwood "mwedgwood@gmail.com"  
ENV NGINX_FLAVOR extras  
ENV NGINX_VERSION 1.4.6-1ubuntu3.3  
RUN apt-get update \  
&& apt-get install -y nginx-${NGINX_FLAVOR}=${NGINX_VERSION} \  
&& rm -f /etc/nginx/sites-enabled/default \  
&& rm -rf /var/lib/apt/lists/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
VOLUME ["/var/cache/nginx"]  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

