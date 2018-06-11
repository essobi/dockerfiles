FROM wiggins/alpine:latest  
MAINTAINER wiggins  
  
ARG VERSION=${VERSION:-1.10.3}  
ARG AUTOINDEX_NAME_LEN=${AUTOINDEX_NAME_LEN:-100}  
  
ENV INSTALL_DIR=/usr/local/nginx \  
DATA_DIR=/data/wwwroot \  
TEMP_DIR=/tmp/nginx  
  
RUN set -x && \  
mkdir -p $(dirname ${DATA_DIR}) ${TEMP_DIR} && cd ${TEMP_DIR} && \  
DOWN_URL="http://nginx.org/download" && \  
DOWN_URL="${DOWN_URL}/nginx-${VERSION}.tar.gz" && \  
FILE_NAME=${DOWN_URL##*/} && mkdir -p ${TEMP_DIR}/${FILE_NAME%%\\.tar*} && \  
apk \--update \--no-cache upgrade && \  
apk add \--no-cache \--virtual .build-deps geoip geoip-dev pcre libxslt gd
openssl-dev pcre-dev zlib-dev \  
build-base linux-headers libxslt-dev gd-dev openssl-dev libstdc++ libgcc patch
git tar curl && \  
curl -Lk ${DOWN_URL} | tar xz -C ${TEMP_DIR} \--strip-components=1 && \  
curl -Lk https://github.com/maowiggins/nginx-add-module/raw/master/nginx-
mode.tar.gz|tar xz -C ${TEMP_DIR} && \  
git clone https://github.com/arut/nginx-rtmp-module.git -b v1.1.7 && \  
git clone https://github.com/xiaokai-wang/nginx_upstream_check_module.git && \  
git clone https://github.com/xiaokai-wang/nginx-stream-upsync-module.git && \  
git clone https://github.com/yaoweibin/nginx_limit_speed_module.git && \  
#git clone https://github.com/leev/ngx_http_geoip2_module.git && \  
addgroup -g 400 -S www && \  
adduser -u 400 -S -h ${DATA_DIR} -s /sbin/nologin -g 'WEB Server' -G www www
&& \  
find ${TEMP_DIR} -type f -exec sed -i 's/\r$//g' {} \; && \  
#cd ${FILE_NAME%%\\.tar*} && \  
sed -ri "s/^(#define NGX_HTTP_AUTOINDEX_NAME_LEN).*/\1 ${AUTOINDEX_NAME_LEN}/"
src/http/modules/ngx_http_autoindex_module.c && \  
sed -ri "s/^(#define NGX_HTTP_AUTOINDEX_PREALLOCATE).*/\1
${AUTOINDEX_NAME_LEN}/" src/http/modules/ngx_http_autoindex_module.c && \  
patch -p0 < ./nginx_upstream_check_module/check_1.9.2+.patch && \  
CFLAGS=-Wno-unused-but-set-variable ./configure \--prefix=${INSTALL_DIR} \  
\--user=www \--group=www \  
\--error-log-path=/data/wwwlogs/error.log \  
\--http-log-path=/data/wwwlogs/access.log \  
\--pid-path=/usr/local/nginx/nginx.pid \  
\--lock-path=/var/lock/nginx.lock \  
\--with-pcre \  
\--with-ipv6 \  
\--with-mail \  
\--with-mail_ssl_module \  
\--with-pcre-jit \  
\--with-file-aio \  
\--with-threads \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-http_ssl_module \  
\--with-http_flv_module \  
\--with-http_v2_module \  
\--with-http_realip_module \  
\--with-http_gzip_static_module \  
\--with-http_stub_status_module \  
\--with-http_sub_module \  
\--with-http_mp4_module \  
\--with-http_image_filter_module \  
\--with-http_addition_module \  
\--with-http_auth_request_module \  
\--with-http_dav_module \  
\--with-http_degradation_module \  
\--with-http_geoip_module \  
#--with-http_geo_module \  
\--with-http_xslt_module \  
\--with-http_gunzip_module \  
\--with-http_secure_link_module \  
\--with-http_slice_module \  
\--add-module=./ngx_http_substitutions_filter_module \  
\--add-module=./ngx_fancyindex \  
\--add-module=./echo_nginx_module \  
\--add-module=./nginx-rtmp-module \  
\--add-module=./nginx_upstream_check_module \  
\--add-module=./nginx_limit_speed_module && \  
#--add-module=./nginx-stream-upsync-module && \  
#--add-module=./ngx_http_geoip2_module && \  
#--http-client-body-temp-path=${INSTALL_DIR}/client/ \  
#--http-proxy-temp-path=${INSTALL_DIR}/proxy/ \  
#--http-fastcgi-temp-path=${INSTALL_DIR}/fcgi/ \  
#--http-uwsgi-temp-path=${INSTALL_DIR}/uwsgi \  
#--http-scgi-temp-path=${INSTALL_DIR}/scgi \  
make -j$(getconf _NPROCESSORS_ONLN) && \  
make install && \  
curl -Lks https://raw.githubusercontent.com/xiaoyawl/docker-
nginx/master/Block_Injections.conf > ${INSTALL_DIR}/conf/Block_Injections.conf
&& \  
runDeps="$( scanelf --needed --nobanner --recursive /usr/local/ | awk '{
gsub(/,/, "\nso:", $2); print "so:" $2 }' | sort -u | xargs -r apk info
--installed | sort -u )" && \  
runDeps="${runDeps} inotify-tools supervisor logrotate python" && \  
apk add \--no-cache \--virtual .ngx-rundeps $runDeps && \  
apk del .build-deps && \  
#apk del build-base git patch && \  
rm -rf /var/cache/apk/* /tmp/* ${INSTALL_DIR}/conf/nginx.conf && \  
mkdir -p /usr/local/geoip && \  
curl -Lk
http://www.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz >
/usr/local/geoip/GeoIP.dat.gz && \  
curl -Lk http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
> /usr/local/geoip/GeoLiteCity.dat.gz && \  
cd /usr/local/geoip && \  
gunzip GeoIP.dat.gz && \  
gunzip GeoLiteCity.dat.gz  
  
ENV PATH=${INSTALL_DIR}/sbin:$PATH \  
TERM=linux  
  
ADD etc /etc  
ADD entrypoint.sh /entrypoint.sh  
  
VOLUME ["${DATA_DIR}"]  
EXPOSE 80 443  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
#CMD ["/usr/sbin/supervisord"]  
#CMD ["/bin/bash", "/entrypoint.sh"]  

