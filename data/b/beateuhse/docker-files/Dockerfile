FROM alpine:3.5  
  
ENV NGINX_VERSION 1.13.8  
ENV NAXSI_VERSION 0.55.3  
  
ENV NGINX_AMPLIFY_VERSION 1.0.0  
  
RUN GPG_KEYS=B0F4253373F8F6F510D42178520A9993A1C052F8 \  
&& CONFIG="\  
\--prefix=/etc/nginx \  
\--sbin-path=/usr/sbin/nginx \  
\--modules-path=/usr/lib/nginx/modules \  
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
\--add-module=/usr/src/naxsi-$NAXSI_VERSION/naxsi_src/ \  
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
\--with-http_xslt_module=dynamic \  
\--with-http_image_filter_module=dynamic \  
\--with-http_geoip_module=dynamic \  
\--with-threads \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-stream_ssl_preread_module \  
\--with-stream_realip_module \  
\--with-stream_geoip_module=dynamic \  
\--with-http_slice_module \  
\--with-mail \  
\--with-mail_ssl_module \  
\--with-compat \  
\--with-file-aio \  
\--with-http_v2_module \  
" \  
&& addgroup -S nginx \  
&& adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx \  
&& apk add --no-cache --virtual .build-deps \  
gcc \  
libc-dev \  
make \  
openssl-dev \  
pcre-dev \  
zlib-dev \  
linux-headers \  
curl \  
gnupg \  
libxslt-dev \  
gd-dev \  
geoip-dev \  
&& curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz -o
nginx.tar.gz \  
&& curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz.asc -o
nginx.tar.gz.asc \  
&& curl -fSL https://github.com/nbs-system/naxsi/archive/$NAXSI_VERSION.tar.gz
-o naxsi.tar.gz \  
&& curl -fSL https://github.com/nbs-
system/naxsi/releases/download/$NAXSI_VERSION/naxsi-$NAXSI_VERSION.tar.gz.asc
-o naxsi.tar.gz.asc \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& found=''; \  
for server in \  
ha.pool.sks-keyservers.net \  
hkp://keyserver.ubuntu.com:80 \  
hkp://p80.pool.sks-keyservers.net:80 \  
pgp.mit.edu \  
; do \  
echo "Fetching GPG key $GPG_KEYS from $server"; \  
gpg --keyserver "$server" --keyserver-options timeout=10 --recv-keys
"$GPG_KEYS" && found=yes && break; \  
done; \  
test -z "$found" && echo >&2 "error: failed to fetch GPG key $GPG_KEYS" &&
exit 1; \  
gpg --batch --verify nginx.tar.gz.asc nginx.tar.gz \  
&& rm -r "$GNUPGHOME" nginx.tar.gz.asc naxsi.tar.gz.asc \  
&& mkdir -p /usr/src \  
&& tar -zxC /usr/src -f nginx.tar.gz \  
&& tar -zxC /usr/src -f naxsi.tar.gz \  
&& rm nginx.tar.gz naxsi.tar.gz \  
&& cd /usr/src/nginx-$NGINX_VERSION \  
&& ./configure $CONFIG --with-debug \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& mv objs/nginx objs/nginx-debug \  
&& mv objs/ngx_http_xslt_filter_module.so objs/ngx_http_xslt_filter_module-
debug.so \  
&& mv objs/ngx_http_image_filter_module.so objs/ngx_http_image_filter_module-
debug.so \  
&& mv objs/ngx_http_geoip_module.so objs/ngx_http_geoip_module-debug.so \  
&& mv objs/ngx_stream_geoip_module.so objs/ngx_stream_geoip_module-debug.so \  
&& ./configure $CONFIG \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& rm -rf /etc/nginx/html/ \  
&& mkdir /etc/nginx/conf.d/ \  
&& mkdir -p /usr/share/nginx/html/ \  
&& install -m644 /usr/src/naxsi-$NAXSI_VERSION/naxsi_config/naxsi_core.rules
/etc/nginx \  
&& install -m644 html/index.html /usr/share/nginx/html/ \  
&& install -m644 html/50x.html /usr/share/nginx/html/ \  
&& install -m755 objs/nginx-debug /usr/sbin/nginx-debug \  
&& install -m755 objs/ngx_http_xslt_filter_module-debug.so
/usr/lib/nginx/modules/ngx_http_xslt_filter_module-debug.so \  
&& install -m755 objs/ngx_http_image_filter_module-debug.so
/usr/lib/nginx/modules/ngx_http_image_filter_module-debug.so \  
&& install -m755 objs/ngx_http_geoip_module-debug.so
/usr/lib/nginx/modules/ngx_http_geoip_module-debug.so \  
&& install -m755 objs/ngx_stream_geoip_module-debug.so
/usr/lib/nginx/modules/ngx_stream_geoip_module-debug.so \  
&& ln -s ../../usr/lib/nginx/modules /etc/nginx/modules \  
&& strip /usr/sbin/nginx* \  
&& strip /usr/lib/nginx/modules/*.so \  
&& rm -rf /usr/src/nginx-$NGINX_VERSION \  
&& rm -rf /usr/src/naxsi-$NAXSI_VERSION \  
\  
# Bring in gettext so we can get `envsubst`, then throw  
# the rest away. To do this, we need to install `gettext`  
# then move `envsubst` out of the way so `gettext` can  
# be deleted completely, then move `envsubst` back.  
&& apk add --no-cache --virtual .gettext gettext \  
&& mv /usr/bin/envsubst /tmp/ \  
\  
&& runDeps="$( \  
scanelf --needed --nobanner --format '%n#p' /usr/sbin/nginx
/usr/lib/nginx/modules/*.so /tmp/envsubst \  
| tr ',' '\n' \  
| sort -u \  
| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1
}' \  
)" \  
&& apk add --no-cache --virtual .nginx-rundeps $runDeps \  
&& apk del .build-deps \  
&& apk del .gettext \  
&& mv /tmp/envsubst /usr/local/bin/ \  
\  
# Bring in tzdata so users could set the timezones through the environment  
# variables  
&& apk add --no-cache tzdata \  
\  
# forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY nginx.vh.default.conf /etc/nginx/conf.d/default.conf  
  
RUN cd ~ && \  
apk update && \  
apk upgrade && \  
apk add --no-cache \  
ca-certificates \  
wget \  
python \  
python-dev \  
py-configobj \  
git \  
util-linux \  
procps \  
gcc \  
musl-dev \  
linux-headers && \  
wget -q --no-check-certificate https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py --ignore-installed --user && \  
~/.local/bin/pip install setuptools --upgrade --user && \  
rm -rf nginx-amplify-agent && \  
git clone "https://github.com/nginxinc/nginx-amplify-agent" && \  
cd nginx-amplify-agent && \  
~/.local/bin/pip install --upgrade \  
\--target=amplify --no-compile \  
-r packages/requirements && \  
python setup.py install && \  
cp nginx-amplify-agent.py /usr/bin && \  
mkdir -p /var/log/amplify-agent && \  
chmod 755 /var/log/amplify-agent && \  
mkdir -p /var/run/amplify-agent && \  
chmod 755 /var/run/amplify-agent && \  
rm -rf ~/.local && \  
apk del \  
ca-certificates \  
wget \  
python-dev \  
py-configobj \  
git \  
gcc \  
musl-dev \  
linux-headers &&\  
rm -rf /var/cache/apk/* &&\  
mkdir -p /etc/amplify-agent  
  
  
COPY ./conf/agent.conf /etc/amplify-agent/agent.conf  
COPY ./entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh; \  
chmod +r /proc;  
  
VOLUME "/etc/nginx/conf.d" \  
"/etc/nginx/naxsi" \  
"/etc/nginx/ssl" \  
"/usr/share/nginx/html" \  
"/var/log/nginx"  
  
EXPOSE 80/tcp 443/tcp  
  
STOPSIGNAL SIGQUIT  
  
# CMD ["nginx", "-g", "daemon off;"]  
ENTRYPOINT ["/entrypoint.sh"]  

