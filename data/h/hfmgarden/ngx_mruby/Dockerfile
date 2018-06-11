FROM ubuntu:16.04  
MAINTAINER OKUMURA Takahiro <hfm.garden@gmail.com>  
  
ENV NGINX_CONFIG_OPT_ENV \  
--prefix=/etc/nginx \  
--sbin-path=/usr/sbin/nginx \  
--modules-path=/usr/lib/nginx/modules \  
--conf-path=/etc/nginx/nginx.conf \  
--error-log-path=/var/log/nginx/error.log \  
--http-log-path=/var/log/nginx/access.log \  
--pid-path=/var/run/nginx.pid \  
--lock-path=/var/run/nginx.lock \  
--http-client-body-temp-path=/var/cache/nginx/client_temp \  
--http-proxy-temp-path=/var/cache/nginx/proxy_temp \  
--http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \  
--http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \  
--http-scgi-temp-path=/var/cache/nginx/scgi_temp \  
--user=nginx \  
--group=nginx \  
--with-http_addition_module \  
--with-http_auth_request_module \  
--with-http_gunzip_module \  
--with-http_gzip_static_module \  
--with-http_random_index_module \  
--with-http_realip_module \  
--with-http_secure_link_module \  
--with-http_slice_module \  
--with-http_ssl_module \  
--with-http_stub_status_module \  
--with-http_sub_module \  
--with-http_v2_module \  
--with-stream \  
--with-stream_realip_module \  
--with-stream_ssl_module \  
--with-stream_ssl_preread_module  
  
ENV NGX_MRUBY_VERSION v1.18.10  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN addgroup --system nginx \  
&& adduser --system --disabled-password --no-create-home --gecos "nginx user"
--ingroup nginx nginx \  
&& adduser --system --disabled-password --no-create-home --home /nonexistent
--gecos "nginx user" --ingroup nginx nginx \  
&& apt-get -qq update \  
&& build_deps="git wget g++ make rake bison libxml2-dev libpcre3-dev" \  
&& apt-get --no-install-recommends -qq install $build_deps libssl-dev libpcre3
\  
&& git clone --depth=1 --branch=$NGX_MRUBY_VERSION
https://github.com/matsumoto-r/ngx_mruby.git /usr/local/src/ngx_mruby \  
&& cd /usr/local/src/ngx_mruby \  
&& sh build.sh \  
&& make install \  
&& rm -rf /etc/nginx/html \  
&& mkdir -p /etc/nginx/conf.d \  
&& install -o nginx -g nginx -d /var/cache/nginx \  
&& rm -rf /usr/local/src/ngx_mruby /var/lib/apt/lists/* \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false $build_deps \  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY nginx.default.conf /etc/nginx/conf.d/default.conf  
  
EXPOSE 80 443  
  
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]  

