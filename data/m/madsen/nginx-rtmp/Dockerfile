FROM debian:jessie  
  
MAINTAINER Anders K. Madsen <lillesvin@gmail.com>  
  
ARG NGINX_VERSION="1.9.14"  
ARG NGINX_RTMP_VERSION="1.1.7"  
ENV DEBIAN_FRONTEND=noninteractive  
ENV PATH=$PATH:/usr/local/nginx/sbin  
  
# Install stuff for building  
RUN apt-get update && apt-get install -y \  
build-essential \  
libpcre3-dev \  
libssl-dev \  
wget \  
zlib1g-dev  
  
RUN mkdir -p /src /config /logs /recordings /html && \  
chmod 777 /recordings && \  
cd /src && \  
wget http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz && \  
tar -zxf nginx-${NGINX_VERSION}.tar.gz && \  
wget https://github.com/arut/nginx-rtmp-
module/archive/v${NGINX_RTMP_VERSION}.tar.gz && \  
tar -zxf v${NGINX_RTMP_VERSION}.tar.gz && \  
cp nginx-rtmp-module-${NGINX_RTMP_VERSION}/stat.xsl /html && \  
cd nginx-${NGINX_VERSION} && \  
./configure \  
\--with-http_ssl_module \  
\--add-module=/src/nginx-rtmp-module-${NGINX_RTMP_VERSION} \  
\--conf-path=/config/nginx.conf \  
\--error-log-path=/logs/error.log \  
\--http-log-path=/logs/access.log && \  
make && \  
make install && \  
ln -s /dev/stdout /logs/access.log && \  
ln -s /dev/stderr /logs/error.log  
  
# Clean up  
RUN rm -rf /src && \  
rm -rf /var/lib/apt/lists/*  
  
VOLUME ["/config", "/recordings"]  
  
COPY ["nginx.conf", "/config/nginx.conf"]  
  
EXPOSE 80 1935  
CMD ["nginx", "-g", "daemon off;"]  

