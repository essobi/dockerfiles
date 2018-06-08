FROM livingobjects/debian-base:8.7_2  
  
# Based on https://github.com/nginxinc/docker-nginx  
  
# Docker Build Arguments  
ARG NGINX_VERSION="1.12.0"  
ARG CONFIG_OPTIONS="\  
--prefix=/etc/nginx \  
--sbin-path=/usr/sbin/nginx \  
--modules-path=/usr/lib/nginx/modules \  
--conf-path=/etc/nginx/nginx.conf \  
--error-log-path=/dev/stderr \  
--http-log-path=/dev/stdout \  
--pid-path=/var/run/nginx.pid \  
--lock-path=/var/run/nginx.lock \  
--http-client-body-temp-path=/var/cache/nginx/client_temp \  
--http-proxy-temp-path=/var/cache/nginx/proxy_temp \  
--http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \  
--http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \  
--http-scgi-temp-path=/var/cache/nginx/scgi_temp \  
--user=lo-daemon \  
--group=lo-daemon \  
--with-http_ssl_module \  
--with-http_realip_module \  
--with-http_addition_module \  
--with-http_sub_module \  
--with-http_dav_module \  
--with-http_gunzip_module \  
--with-http_gzip_static_module \  
--with-http_random_index_module \  
--with-http_secure_link_module \  
--with-http_stub_status_module \  
--with-http_auth_request_module \  
--with-threads \  
--with-stream \  
--with-stream_ssl_module \  
--with-stream_ssl_preread_module \  
--with-stream_realip_module \  
--with-http_slice_module \  
--with-mail \  
--with-mail_ssl_module \  
--with-compat \  
--with-file-aio \  
--with-http_v2_module \  
"  
  
ARG BUILD_DEPS="binutils bsdmainutils build-essential cpp cpp-4.9 debhelper
diffstat dpkg-dev file g++ g++-4.9 gcc gcc-4.9 gettext gettext-base groff-base
intltool-debian libasan1 libasprintf0c2 libatomic1 libc-dev-bin libc6-dev
libcilkrts5 libcloog-isl4 libcroco3 libdpkg-perl libexpat1 libgcc-4.9-dev
libgdbm3 libgomp1 libisl10 libitm1 liblsan0 libmagic1 libmpc3 libmpfr4
libpcre3-dev libpcrecpp0 libpipeline1 libpython-stdlib libpython2.7-minimal
libpython2.7-stdlib libquadmath0 libsqlite3-0 libssl-dev libstdc++-4.9-dev
libtimedate-perl libtsan0 libubsan0 libunistring0 linux-libc-dev lsb-release
make man-db mime-support patch perl perl-modules po-debconf python python-
minimal python2.7 python2.7-minimal quilt xz-utils zlib1g-dev"  
  
ADD auth_request_redirect.patch /usr/src/nginx-${NGINX_VERSION}/  
  
RUN apt-get update \  
&& apt-get install -y cron gzip ${BUILD_DEPS} \  
&& curl -fSL http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz -o
nginx.tar.gz \  
&& curl -fSL http://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz.asc -o
nginx.tar.gz.asc \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
"B0F4253373F8F6F510D42178520A9993A1C052F8" \  
&& gpg --batch --verify nginx.tar.gz.asc nginx.tar.gz \  
&& rm -r "$GNUPGHOME" nginx.tar.gz.asc \  
&& mkdir -p /usr/src \  
&& tar -zxC /usr/src -f nginx.tar.gz \  
&& rm nginx.tar.gz \  
&& cd /usr/src/nginx-${NGINX_VERSION} \  
&& patch -p1 < auth_request_redirect.patch \  
&& ./configure ${CONFIG_OPTIONS} --with-debug \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& mv objs/nginx objs/nginx-debug \  
&& ./configure ${CONFIG_OPTIONS} \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& rm -rf /etc/nginx/html/ \  
&& mkdir /etc/nginx/conf.d/ \  
&& mkdir -p /usr/share/nginx/html/ \  
&& mkdir -p /var/cache/nginx \  
&& install -m644 html/index.html /usr/share/nginx/html/ \  
&& install -m644 html/50x.html /usr/share/nginx/html/ \  
&& install -m755 objs/nginx-debug /usr/sbin/nginx-debug \  
&& ln -s ../../usr/lib/nginx/modules /etc/nginx/modules \  
&& strip /usr/sbin/nginx* \  
&& rm -rf /usr/src/nginx-${NGINX_VERSION} \  
  
# Define working directory.  
&& rm -rf /etc/nginx/conf.d/*.conf \  
&& apt-get purge -y ${BUILD_DEPS} \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/tmp/* \  
&& rm -rf /var/lib/apt/lists/*  
  
# Define mountable directories.  
VOLUME ["/etc/nginx/certs", "/var/log/nginx"]  
  
COPY etc /etc/  
  
# Expose ports.  
EXPOSE 80 443

