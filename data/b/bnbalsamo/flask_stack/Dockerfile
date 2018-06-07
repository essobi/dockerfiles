FROM python:3.5-alpine  
# Slot in the stuff we'll need for making the nginx conf  
COPY ./nginx_conf_build.sh /nginx_conf_build.sh  
COPY ./nginx.template /etc/nginx/nginx.template  
# And the runit service definitions  
COPY gunicorn_run /etc/sv/gunicorn/run  
COPY nginx_run /etc/sv/nginx/run  
# Set up nginx  
# This is copy-pasted from the nginx Dockerfile  
ENV NGINX_VERSION 1.12.1  
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
&& export GNUPGHOME="$(mktemp -d)" \  
&& found=''; \  
for server in \  
ha.pool.sks-keyservers.net \  
hkp://keyserver.ubuntu.com:80 \  
hkp://p80.pool.sks-keyservers.net:80 \  
pgp.mit.edu \  
; do \  
echo "Fetching GPG key $GPG_KEYS from $server"; \  
gpg --keyserver "$server" \--keyserver-options timeout=10 \--recv-keys
"$GPG_KEYS" && found=yes && break; \  
done; \  
test -z "$found" && echo >&2 "error: failed to fetch GPG key $GPG_KEYS" &&
exit 1; \  
gpg --batch --verify nginx.tar.gz.asc nginx.tar.gz \  
&& rm -r "$GNUPGHOME" nginx.tar.gz.asc \  
&& mkdir -p /usr/src \  
&& tar -zxC /usr/src -f nginx.tar.gz \  
&& rm nginx.tar.gz \  
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
&& rm -rf /usr/src/nginx-$NGINX_VERSION \  
\  
# Bring in gettext so we can get `envsubst`, then throw  
# the rest away. To do this, we need to install `gettext`  
# then move `envsubst` out of the way so `gettext` can  
# be deleted completely, then move `envsubst` back.  
&& apk add --no-cache --virtual .gettext gettext \  
&& mv /usr/bin/envsubst /tmp/ \  
\  
&& runDeps="$( \  
scanelf --needed --nobanner /usr/sbin/nginx /usr/lib/nginx/modules/*.so
/tmp/envsubst \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --no-cache --virtual .nginx-rundeps $runDeps \  
&& apk del .gettext \  
&& mv /tmp/envsubst /usr/local/bin/ \  
\  
# forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log \  
# End nginx Dockerfile copy-paste  
# Install runit  
&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& apk --update upgrade && apk add runit \  
# Install the flask/gunicorn basics via pip  
# Pip complains about the dir it's being run in disappearing,  
# so plop in back in the root before running it.  
&& cd / && pip install flask greenlet eventlet gevent gunicorn \  
# Make our own stuff executable and link it where it needs to go  
&& chmod +x /etc/sv/gunicorn/run \  
&& chmod +x /etc/sv/nginx/run \  
&& ln -s /etc/sv/gunicorn /etc/service/gunicorn \  
&& ln -s /etc/sv/nginx /etc/service/nginx \  
&& chmod +x /nginx_conf_build.sh \  
&& apk del .build-deps  
  
# Grab all the args, toss them in the environment  
# NOTE: All of these pertaining to nginx.conf need to  
# ALSO appear in the nginx_conf_build.sh envsubst command  
ARG NGINX_WORKER_PROCESSES=4  
ARG NGINX_USER=nobody  
ARG NGINX_GROUP=nogroup  
ARG NGINX_WORKER_CONNECTIONS=1024  
ARG NGINX_PORT=80  
ARG NGINX_TIMEOUT=300  
ARG NGINX_ROOT_DIR=/dev/null  
ARG NGINX_ACCEPT_MUTEX=on  
ARG NGINX_SENDFILE=on  
ARG NGINX_CLIENT_MAX_BODY_SIZE=4G  
ARG NGINX_SERVER_EXTEND  
ARG NGINX_HTTP_EXTEND  
ARG NGINX_EVENTS_EXTEND  
ARG NGINX_ROOT_EXTEND  
ARG NGINX_UPSTREAM_EXTEND  
ARG NGINX_PROXY_EXTEND  
ARG NGINX_CLI_EXTEND  
ARG GUNICORN_WORKER_TYPE=eventlet  
ARG GUNICORN_WORKERS=4  
ARG GUNICORN_TIMEOUT=300  
ARG GUNICORN_CLI_EXTEND  
ARG APP_CALLABLE=app  
ENV \  
NGINX_WORKER_PROCESSES=$NGINX_WORKER_PROCESSES \  
NGINX_USER=$NGINX_USER \  
NGINX_GROUP=$NGINX_GROUP \  
NGINX_WORKER_CONNECTIONS=$NGINX_WORKER_CONNECTIONS \  
NGINX_PORT=$NGINX_PORT \  
NGINX_TIMEOUT=$NGINX_TIMEOUT \  
NGINX_ROOT_DIR=$NGINX_ROOT_DIR \  
NGINX_ACCEPT_MUTEX=$NGINX_ACCEPT_MUTEX \  
NGINX_SENDFILE=$NGINX_SENDFILE \  
NGINX_CLIENT_MAX_BODY_SIZE=$NGINX_CLIENT_MAX_BODY_SIZE \  
NGINX_SERVER_EXTEND=$NGINX_SERVER_EXTEND \  
NGINX_HTTP_EXTEND=$NGINX_HTTP_EXTEND \  
NGINX_EVENTS_EXTEND=$NGINX_EVENTS_EXTEND \  
NGINX_ROOT_EXTEND=$NGINX_ROOT_EXTEND \  
NGINX_UPSTREAM_EXTEND=$NGINX_UPSTREAM_EXTEND \  
NGINX_PROXY_EXTEND=$NGINX_PROXY_EXTEND \  
NGINX_CLI_EXTEND=$NGINX_CLI_EXTEND \  
GUNICORN_WORKER_TYPE=$GUNICORN_WORKER_TYPE \  
GUNICORN_WORKERS=$GUNICORN_WORKERS \  
GUNICORN_TIMEOUT=$GUNICORN_TIMEOUT \  
GUNICORN_CLI_EXTEND=$GUNICORN_CLI_EXTEND \  
APP_CALLABLE=$APP_CALLABLE  
# Copy in the code from project specific builds  
# and install it  
ONBUILD COPY . /code/  
ONBUILD WORKDIR /code  
ONBUILD RUN \  
apk add --no-cache --virtual .build-deps \  
# Pull alpine-sdk in so most stuff _probably_ builds  
# if it requires external libs  
alpine-sdk \  
  
&& if [ -e /code/apk_packages.txt ]; then while IFS='' read line; do apk add
--no-cache $line; done < /code/apk_packages.txt; fi \  
&& if [ -e /code/requirements.txt ]; then pip install -r
/code/requirements.txt; fi \  
&& python /code/setup.py install \  
&& rm -rf /var/cache/apk/* \  
&& apk del .build-deps  
# We should be good to go, fire it up.  
CMD /nginx_conf_build.sh && \  
test -n $APP_NAME && \  
runsvdir -P /etc/service  

