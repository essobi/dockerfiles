FROM alpine:3.7  
  
COPY docker/ /  
  
ENV NGINX_VERSION=1.13.11  
  
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
\--with-http_ssl_module \  
\--with-http_realip_module \  
\--with-http_addition_module \  
\--with-http_flv_module \  
\--with-http_mp4_module \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_secure_link_module \  
\--with-http_image_filter_module=dynamic \  
\--with-http_geoip_module=dynamic \  
\--with-threads \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-stream_ssl_preread_module \  
\--with-stream_realip_module \  
\--with-stream_geoip_module=dynamic \  
\--with-http_slice_module \  
\--with-compat \  
\--with-file-aio \  
\--with-http_v2_module \  
\--add-module=/usr/src/ModSecurity-nginx \  
" \  
\  
# https://github.com/cloudflare/sslconfig/issues/83  
# --with-http_v2_hpack_enc \  
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
patch \  
libxslt-dev \  
gd-dev \  
geoip-dev \  
&& apk add --no-cache --virtual .libmodsecurity-deps \  
pcre-dev \  
libxml2-dev \  
git \  
libtool \  
automake \  
autoconf \  
g++ \  
flex \  
bison \  
yajl-dev \  
&& apk add --no-cache --virtual .libmodsecurity-rundeps \  
libxml2 \  
libxslt \  
yajl \  
libstdc++ \  
&& curl -fSL https://nginx.org/download/nginx-$NGINX_VERSION.tar.gz -o
nginx.tar.gz \  
&& curl -fSL https://nginx.org/download/nginx-$NGINX_VERSION.tar.gz.asc -o
nginx.tar.gz.asc \  
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
&& rm -rf "$GNUPGHOME" nginx.tar.gz.asc \  
&& tar -zxC /usr/src -f nginx.tar.gz \  
&& rm nginx.tar.gz \  
\  
# Install & config ModSecurity  
&& mkdir -p /var/log/modsec \  
&& mkdir /etc/nginx/owasp-modsecurity-crs \  
&& cd /etc/nginx/owasp-modsecurity-crs \  
&& git clone https://github.com/SpiderLabs/owasp-modsecurity-crs . \  
&& install -m644 crs-setup.conf.example crs-setup.conf \  
&& sed -i -e 's/SecDefaultAction "phase:1,log,auditlog,pass"/#SecDefaultAction
"phase:1,log,auditlog,pass"/g' crs-setup.conf \  
&& sed -i -e 's/SecDefaultAction "phase:2,log,auditlog,pass"/#SecDefaultAction
"phase:1,log,auditlog,pass"/g' crs-setup.conf \  
&& sed -i -e 's/# SecDefaultAction
"phase:2,log,auditlog,deny,status:403"/SecDefaultAction
"phase:2,log,auditlog,deny,status:403"/g' crs-setup.conf \  
&& sed -i -e 's/# SecDefaultAction
"phase:1,log,auditlog,deny,status:403"/SecDefaultAction
"phase:1,log,auditlog,deny,status:403"/g' crs-setup.conf \  
&& cd /usr/src \  
&& git clone https://github.com/SpiderLabs/ModSecurity \  
&& cd ModSecurity \  
#&& git checkout v3/master \  
&& git checkout a2427df \  
&& git submodule init \  
&& git submodule update \  
&& sed -i -e 's/u_int64_t/uint64_t/g' \  
./src/actions/transformations/html_entity_decode.cc \  
./src/actions/transformations/html_entity_decode.h \  
./src/actions/transformations/js_decode.cc \  
./src/actions/transformations/js_decode.h \  
./src/actions/transformations/parity_even_7bit.cc \  
./src/actions/transformations/parity_even_7bit.h \  
./src/actions/transformations/parity_odd_7bit.cc \  
./src/actions/transformations/parity_odd_7bit.h \  
./src/actions/transformations/parity_zero_7bit.cc \  
./src/actions/transformations/parity_zero_7bit.h \  
./src/actions/transformations/remove_comments.cc \  
./src/actions/transformations/url_decode_uni.cc \  
./src/actions/transformations/url_decode_uni.h \  
&& sh build.sh \  
&& ./configure \  
&& make \  
&& make install \  
&& install -m644 modsecurity.conf-recommended /etc/nginx/owasp-modsecurity-
crs/modsecurity.conf \  
&& sed -i -e 's/\/var\/log\/modsec_audit.log/\/var\/log\/modsec\/audit.log/g'
/etc/nginx/owasp-modsecurity-crs/modsecurity.conf \  
&& sed -i -e 's/SecRuleEngine DetectionOnly/SecRuleEngine On/g'
/etc/nginx/owasp-modsecurity-crs/modsecurity.conf \  
&& sed -i -e 's/SecRequestBodyLimit 13107200/SecRequestBodyLimit 50107200/g'
/etc/nginx/owasp-modsecurity-crs/modsecurity.conf \  
&& sed -i -e 's/SecStatusEngine On/SecStatusEngine Off/g' /etc/nginx/owasp-
modsecurity-crs/modsecurity.conf \  
&& cd /usr/src \  
&& git clone https://github.com/SpiderLabs/ModSecurity-nginx \  
&& cd /usr/src/nginx-$NGINX_VERSION \  
\  
# https://github.com/cloudflare/sslconfig/issues/83  
#&& patch -p 1 -u < ../patches/nginx_http2_hpack.patch \  
&& ./configure $CONFIG \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& rm -rf /etc/nginx/html/ \  
&& mkdir -p /usr/share/nginx/html/ \  
&& install -m644 html/index.html /usr/share/nginx/html/ \  
&& install -m644 html/50x.html /usr/share/nginx/html/ \  
&& ln -s ../../usr/lib/nginx/modules /etc/nginx/modules \  
&& strip /usr/sbin/nginx* \  
&& strip /usr/lib/nginx/modules/*.so \  
&& rm -rf /usr/src/nginx-$NGINX_VERSION \  
&& rm -rf /usr/src/ModSecurity /usr/src/ModSecurity-nginx \  
\  
# Bring in gettext so we can get `envsubst`, then throw  
# the rest away. To do this, we need to install `gettext`  
# then move `envsubst` out of the way so `gettext` can  
# be deleted completely, then move `envsubst` back.  
&& apk add --no-cache --virtual .gettext gettext \  
&& mv /usr/bin/envsubst /tmp/ \  
&& runDeps="$( \  
scanelf --needed --nobanner /usr/sbin/nginx /usr/lib/nginx/modules/*.so
/tmp/envsubst \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --no-cache --virtual .nginx-rundeps $runDeps \  
&& apk del .build-deps \  
&& apk del .libmodsecurity-deps \  
&& apk del .gettext \  
&& mv /tmp/envsubst /usr/local/bin/ \  
\  
# forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log \  
&& ln -sf /dev/stderr /var/log/modsec/audit.log \  
\  
# nginx cache folder  
&& mkdir -p /cache/nginx/proxy  
  
EXPOSE 80 443  
  
STOPSIGNAL SIGTERM  
  
HEALTHCHECK --interval=5s --timeout=3s --retries=2 \  
CMD \  
wget -q -O - localhost/health-check || exit 1  
  
CMD ["nginx", "-g", "daemon off;"]  

