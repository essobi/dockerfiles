FROM absalomedia/mini  
MAINTAINER Lawrence Meckan <media@absalom.biz>  
  
# Set correct environment variables.  
ENV DOCKER_NAME rev_nginx  
ENV NGINX_VERSION 1.12.0  
ENV OPENSSL_VERSION 1.1.0e  
# Enable ssh access  
RUN rm -f /etc/service/sshd/down  
  
# Regenerate SSH host keys. baseimage-docker does not contain any, so you  
# have to do that yourself. You may also comment out this instruction; the  
# init system will auto-generate one during boot.  
# RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
# !!! Enabling the insecure key permanently !!! REMOVE ME AT PRODUCTION  
# RUN /usr/sbin/enable_insecure_key  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
### ...put your own build instructions here... ###  
  
EXPOSE 80 443  
  
RUN useradd -r -s /usr/sbin/nologin nginx && mkdir -p /var/log/nginx
/var/cache/nginx  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get upgrade -y  
RUN apt-get -y --no-install-recommends install wget build-essential zlib1g-dev
libpcre3-dev libxslt1-dev libxml2-dev libgd2-xpm-dev libgeoip-dev libgoogle-
perftools-dev libperl-dev  
RUN echo "Downloading nginx v${NGINX_VERSION} ..." && wget -qO -
http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz | tar zxf - -C /tmp  
RUN echo "Downloading openssl v${OPENSSL_VERSION} ..." && wget -qO -
https://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz | tar xzf -
-C /tmp  
RUN cd /tmp/nginx-${NGINX_VERSION} && ./configure \  
\--prefix=/etc/nginx \  
\--sbin-path=/usr/sbin/nginx \  
\--conf-path=/etc/nginx/nginx.conf \  
\--error-log-path=/var/log/nginx/error.log \  
\--http-log-path=/var/log/nginx/access.log \  
\--pid-path=/var/run/nginx.pid \  
\--lock-path=/var/run/nginx.lock \  
\--http-client-body-temp-path=/var/cache/nginx/client_temp \  
\--http-proxy-temp-path=/var/cache/nginx/proxy_temp \  
\--http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \  
\--http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \  
\--http-scgi-temp-path=/var/cache/nginx/scgi_temp \  
\--user=nginx \  
\--group=nginx \  
\--with-http_ssl_module \  
\--with-http_realip_module \  
\--with-http_addition_module \  
\--with-http_sub_module \  
\--with-http_dav_module \  
\--with-http_flv_module \  
\--with-http_mp4_module \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_random_index_module \  
\--with-http_secure_link_module \  
\--with-http_stub_status_module \  
\--with-http_auth_request_module \  
\--without-http_autoindex_module \  
\--without-http_ssi_module \  
\--with-threads \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-mail \  
\--with-mail_ssl_module \  
\--with-file-aio \  
\--with-http_slice_module \  
\--with-http_v2_module \  
\--with-cc-opt='-g -O2 -fstack-protector --param=ssp-buffer-size=4 -Wformat
-Werror=format-security -Wp,-D_FORTIFY_SOURCE=2' \  
\--with-ld-opt='-Wl,-Bsymbolic-functions -Wl,-z,relro -Wl,--as-needed' \  
\--with-ipv6 \  
\--with-pcre-jit \  
\--with-openssl=/tmp/openssl-${OPENSSL_VERSION} && make && make install  
RUN rm -Rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
apt-get purge -yqq build-essential && \  
apt-get autoremove -yqq && \  
apt-get clean  
  
  
ENV DEFAULT_APP_USER nginx  
ENV DEFAULT_APP_GROUP nginx  
ENV DEFAULT_APP_UID 1000  
ENV DEFAULT_APP_GID 1000  
ENV DEFAULT_UPLOAD_MAX_SIZE 30M  
ENV DEFAULT_NGINX_MAX_WORKER_PROCESSES 8  
ENV DEFAULT_CHOWN_APP_DIR true  
  
ENV SSL_ENABLED true  
  
COPY . /app  
  
RUN chmod 750 /app/bin/*.sh  
  
RUN /app/bin/init_nginx.sh  
  
CMD ["/sbin/my_init"]  
  

