FROM ubuntu:16.04  
  
LABEL maintainer="Carlo van Wyk - https://www.humankode.com/contact"  
  
RUN apt-get update \  
&& apt-get install software-properties-common python-software-properties
checkinstall -y \  
&& DEBIAN_FRONTEND=noninteractive add-apt-repository ppa:nginx/stable  
  
#install essential packages  
RUN apt-get update && apt-get install -y \  
curl \  
wget \  
nginx \  
git \  
build-essential \  
zlib1g-dev \  
libpcre3-dev \  
libssl-dev \  
libxslt1-dev \  
libxml2-dev \  
libgd2-xpm-dev \  
libgeoip-dev \  
libgoogle-perftools-dev \  
libperl-dev  
  
#download nginx  
RUN cd /usr/local/src \  
&& wget http://nginx.org/download/nginx-1.13.8.tar.gz \  
&& tar -xzvf nginx-1.13.8.tar.gz  
  
RUN cd /usr/local/src \  
&& git clone https://github.com/google/ngx_brotli.git --recursive \  
&& cd ngx_brotli \  
&& git submodule update --recursive  
  
  
RUN ls -la /usr/local/src/ngx_brotli  
  
WORKDIR /usr/local/src/nginx-1.13.8  
RUN ./configure --with-cc-opt='-g -O2 -fPIE -fstack-protector-strong -Wformat
-Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2' \  
\--with-ld-opt='-Wl,-Bsymbolic-functions -fPIE -pie -Wl,-z,relro -Wl,-z,now' \  
\--prefix=/usr/share/nginx \  
\--conf-path=/etc/nginx/nginx.conf \  
\--http-log-path=/var/log/nginx/access.log \  
\--error-log-path=/var/log/nginx/error.log \  
\--lock-path=/var/lock/nginx.lock \  
\--pid-path=/run/nginx.pid \  
\--http-client-body-temp-path=/var/lib/nginx/body \  
\--http-fastcgi-temp-path=/var/lib/nginx/fastcgi \  
\--http-proxy-temp-path=/var/lib/nginx/proxy \  
\--http-scgi-temp-path=/var/lib/nginx/scgi \  
\--http-uwsgi-temp-path=/var/lib/nginx/uwsgi \  
\--with-debug \  
\--with-pcre-jit \  
\--with-ipv6 \  
\--with-http_ssl_module \  
\--with-http_stub_status_module \  
\--with-http_realip_module \  
\--with-http_auth_request_module \  
\--with-http_addition_module \  
\--with-http_dav_module \  
\--with-http_geoip_module \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_image_filter_module \  
\--with-http_v2_module \  
\--with-http_sub_module \  
\--with-http_xslt_module \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-mail \  
\--with-mail_ssl_module \  
\--with-threads \  
\--add-module=/usr/local/src/ngx_brotli \  
\--sbin-path=/usr/sbin/nginx  
  
RUN make \  
&& apt-get remove nginx -y \  
&& apt-get remove nginx-common -y \  
&& checkinstall -y \  
&& mkdir -p /var/lib/nginx \  
&& mkdir -p /var/lib/nginx/body \  
&& mkdir -p /var/lib/nginx/fastcgi  
  
WORKDIR /  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]

