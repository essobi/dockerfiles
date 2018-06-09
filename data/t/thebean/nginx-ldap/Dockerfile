FROM centos:7  
  
LABEL Author="Ravindra Bhadti <rbhadti@gmail.com>"  
  
ENV NGINX_VERSION 1.11.13  
ENV HTTP_LISTEN_PORT 80  
ENV HTTPS_LISTEN_PORT 443  
ENV APP_USER app-user  
ENV APP_UID 1001  
  
COPY run.sh /run.sh  
  
RUN useradd ${APP_USER} -u ${APP_UID} -g 0 && \  
yum -y update && \  
yum install -y git gcc pcre pcre-devel openssl openssl-devel openldap-devel
wget openldap openldap-clients && \  
mkdir /var/log/nginx \  
&& mkdir /etc/nginx \  
&& cd ~ \  
&& git clone https://github.com/kvspb/nginx-auth-ldap.git \  
&& git clone https://github.com/nginx/nginx.git \  
&& cd ~/nginx \  
&& git checkout tags/release-${NGINX_VERSION} \  
&& ./auto/configure \  
\--add-module=/root/nginx-auth-ldap \  
\--with-http_ssl_module \  
\--with-debug \  
\--conf-path=/etc/nginx/nginx.conf \  
\--sbin-path=/usr/sbin/nginx \  
\--pid-path=/var/log/nginx/nginx.pid \  
\--error-log-path=/var/log/nginx/error.log \  
\--http-log-path=/var/log/nginx/access.log \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-debug \  
\--with-file-aio \  
\--with-threads \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_v2_module \  
\--with-http_auth_request_module \  
&& make install \  
&& cd .. \  
&& rm -rf nginx-auth-ldap \  
&& rm -rf nginx \  
&& wget -O /tmp/dockerize.tar.gz
https://github.com/jwilder/dockerize/releases/download/v0.2.0/dockerize-linux-
amd64-v0.2.0.tar.gz \  
&& tar -C /usr/local/bin -xzvf /tmp/dockerize.tar.gz \  
&& rm -rf /tmp/dockerize.tar.gz && \  
yum remove -y git wget && \  
yum clean all  
  
EXPOSE 80 443  
  
COPY resources/configuration/nginx.conf /etc/nginx/nginx.conf  
COPY clair-reports /usr/share/nginx/  
  
CMD ["/run.sh"]

