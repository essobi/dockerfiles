FROM fedora:20  
MAINTAINER Enrico Hoffmann <dasrick@gmail.com>  
  
# Expose environment variables  
ENV NGINX_VERSION 1.7.12  
# Install wget, gcc, make, regex and openssl  
RUN yum -y update && yum install -y wget gcc make pcre pcre-devel openssl-
devel && yum -y clean all  
  
# Create folder for specific nginx binaries  
RUN mkdir -p /opt/nginx  
  
# Download and install nginx in/with specific version/settings  
RUN wget -P /tmp/nginx/
http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz && cd /tmp/nginx/ &&
tar -zxvf nginx-${NGINX_VERSION}.tar.gz && rm -f nginx-${NGINX_VERSION}.tar.gz
&& cd /tmp/nginx/nginx-${NGINX_VERSION} && ./configure --with-ipv6 --with-
http_stub_status_module --with-http_ssl_module --with-http_spdy_module
--prefix=/opt/nginx && make && make install && rm -rf /tmp/nginx  
  
# Set property for remove behavior and clean up the system  
RUN echo "clean_requirements_on_remove=1" >> /etc/yum.conf  
RUN yum remove -y wget gcc make  
  
VOLUME ["/var/www", "/var/log/nginx", "/opt/nginx/conf/nginx.conf",
"/opt/nginx/certs"]  
  
EXPOSE 80:80 443:443  
CMD ["/opt/nginx/sbin/nginx"]

