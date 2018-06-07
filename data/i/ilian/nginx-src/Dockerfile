FROM debian:jessie  
  
MAINTAINER ilian  
  
ENV NGINX_VERSION 1.9.14  
# Download and extract source to /usr/src  
RUN apt-get -q update && apt-get -qyV install \  
wget gcc make libpcre3 libpcre3-dev libssl-dev  
RUN wget -O /tmp/nginx.tar.gz
http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz && \  
tar xvsf /tmp/nginx.tar.gz -C /usr/src/  
WORKDIR /usr/src/nginx-${NGINX_VERSION}  
# Configure and compile nginx from source  
RUN ./configure --with-http_ssl_module --with-http_realip_module --with-ipv6
&& \  
make && make install  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /usr/local/nginx/logs/access.log  
RUN ln -sf /dev/stderr /usr/local/nginx/logs/error.log  
  
EXPOSE 80 443  
CMD ["/usr/local/nginx/sbin/nginx", "-g", "daemon off;"]  

