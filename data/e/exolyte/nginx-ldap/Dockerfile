FROM alpine:3.7  
  
MAINTAINER Uday Kabe, <uday.kabe@exolyte.com>  
  
ENV NGINX_VERSION=1.12.2 \  
\  
LDAP_SERVER="127.0.0.1:389" \  
LDAP_SEARCH_BASE_DN="ou=users,dc=example,dc=com" \  
LDAP_USER_ATTRIBUTE_LIST="givenName,sn,cn" \  
LDAP_USER_SEARCHFILTER="objectClass=inetOrgPerson" \  
LDAP_BIND_DN="cn=admin,ou=itg,dc=example,dc=com" \  
LDAP_BIND_DN_PASSWORD="password" \  
LDAP_GROUP_ATTRIBUTE_DN="member"  
  
# Install necessary build libraries  
RUN apk --update add --no-cache --virtual .build-deps \  
curl \  
gnupg \  
gcc \  
make \  
wget \  
libc-dev \  
pcre-dev \  
zlib-dev \  
linux-headers \  
libxslt-dev \  
gd-dev \  
geoip-dev \  
musl-dev libressl-dev expat-dev apr-dev apr-util-dev curl-dev linux-pam-dev  
  
# Download NGINX source; watch for occasional errors when validating key  
RUN GPG_KEYS=B0F4253373F8F6F510D42178520A9993A1C052F8 && \  
cd ~ && \  
curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz -o
nginx.tar.gz && \  
curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz.asc -o
nginx.tar.gz.asc && \  
export GNUPGHOME="$(mktemp -d)" && \  
found=''; \  
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
&& rm -r "$GNUPGHOME" nginx.tar.gz.asc \  
&& mkdir -p /usr/src \  
&& tar -zxC /usr/src -f nginx.tar.gz \  
&& rm nginx.tar.gz  
  
# Environment variables for third-party-module versions  
ENV NGINX_HTTP_AUTH_PAM_MODULE_VERSION=1.5.1 \  
NGINX_RTMP_MODULE_VERSION=1.2.1 \  
NGINX_DAV_EXT_MODULE_VERSION=0.1.0 \  
NGINX_HTTP_SHIBBOLETH_VERSION=2.0.1 \  
NGINX_UPSTREAM_FAIR_VERSION=0.1.2 \  
NGINX_STICKY_MODULE_NG_VERSION=master \  
NGINX_AUTH_LDAP_VERSION=master  
  
# Download the third-party modules for NGINX  
RUN cd /usr/src && \  
echo 'if [ "_master" != _$3 ]; then export pref="v"; else export pref=""; fi;
wget --no-check-certificate $1/$2/archive/$pref$3.zip && unzip $pref$3 && mv
$2-$3 $2' > getgh && chmod +x getgh && \  
./getgh https://github.com/kvspb nginx-auth-ldap master && \  
./getgh https://github.com/arut nginx-dav-ext-module
${NGINX_DAV_EXT_MODULE_VERSION} && \  
./getgh https://github.com/nginx-shib nginx-http-shibboleth
${NGINX_HTTP_SHIBBOLETH_VERSION} && \  
./getgh https://github.com/itoffshore nginx-upstream-fair
${NGINX_UPSTREAM_FAIR_VERSION} && \  
./getgh https://github.com/sto ngx_http_auth_pam_module
${NGINX_HTTP_AUTH_PAM_MODULE_VERSION} && \  
./getgh https://github.com/arut nginx-rtmp-module ${NGINX_RTMP_MODULE_VERSION}  
  
# Download nginx-sticky-module from bitbucket.org; download appears to have
intermittent connectivity issues  
RUN cd /usr/src && \  
wget --no-check-certificate -O master.zip https://bitbucket.org/nginx-
goodies/nginx-sticky-module-ng/get/${NGINX_STICKY_MODULE_NG_VERSION}.zip && \  
mkdir temp && unzip ${NGINX_STICKY_MODULE_NG_VERSION} -d temp && \  
mkdir nginx-sticky-module && mv temp/*/* nginx-sticky-module/ && \  
rm -rf temp ${NGINX_STICKY_MODULE_NG_VERSION}.zip  
  
# Add nginx user and group  
RUN addgroup -g 1000 -S nginx && \  
adduser -u 1000 -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx  
  
# Build NGINX from source, along with third-party modules  
RUN CONFIG="\  
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
\--add-dynamic-module=../nginx-auth-ldap \  
\--add-dynamic-module=../nginx-dav-ext-module \  
\--add-dynamic-module=../nginx-http-shibboleth \  
\--add-dynamic-module=../nginx-upstream-fair \  
\--add-dynamic-module=../nginx-sticky-module \  
\--add-dynamic-module=../ngx_http_auth_pam_module \  
\--add-dynamic-module=../nginx-rtmp-module \  
" \  
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
&& rm -rf /usr/src/ \  
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
# forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
COPY templates/configuration/nginx.ldap.conf
/templates/configuration/nginx.conf  
  
EXPOSE 80 443  
  
WORKDIR /etc/nginx  
  
COPY resources/scripts/entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod u+x /usr/local/bin/entrypoint.sh  
  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
  
CMD ["nginx", "-g", "daemon off;"]  

