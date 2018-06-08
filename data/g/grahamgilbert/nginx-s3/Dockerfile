FROM ubuntu:14.04.4  
ENV NGINX_VERSION=1.9.12  
RUN apt-get update && \  
apt-get -y install curl build-essential libpcre3 libpcre3-dev zlib1g-dev
libssl-dev git && \  
curl -LO http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz && \  
tar zxf nginx-${NGINX_VERSION}.tar.gz && \  
cd nginx-${NGINX_VERSION} && \  
git clone https://github.com/anomalizer/ngx_aws_auth.git && \  
./configure --with-http_ssl_module --add-module=ngx_aws_auth
--prefix=/etc/nginx --conf-path=/var/log/nginx --conf-
path=/etc/nginx/nginx.conf --sbin-path=/usr/sbin/nginx && \  
make install && \  
cd /tmp && \  
rm -f nginx-${NGINX_VERSION}.tar.gz && \  
rm -rf nginx-${NGINX_VERSION} && \  
apt-get purge -y curl git && \  
apt-get autoremove -y && \  
update-rc.d -f nginx remove && \  
rm -f /etc/nginx/sites-enabled/default && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD nginx.conf /etc/nginx/nginx.conf  
# Define mountable directories.  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d",
"/var/log/nginx", "/var/www/html"]  
  
WORKDIR /etc/nginx  
  
EXPOSE 80  
EXPOSE 443  
CMD /usr/sbin/nginx  

