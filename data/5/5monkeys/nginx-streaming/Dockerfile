FROM buildpack-deps:jessie  
  
RUN curl -L -o /tmp/nginx_signing.key http://nginx.org/keys/nginx_signing.key
&& \  
apt-key add /tmp/nginx_signing.key && \  
echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list && \  
echo "deb-src http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list  
  
# lua-nginx-module only supports nginx <=1.11.2  
ENV NGINX_VERSION 1.11.2  
ENV NGINX_FULL_VERSION ${NGINX_VERSION}-1~jessie  
ENV RTMP_VERSION 1.2.0  
ENV VOD_VERSION 1.19  
ENV LUA_VERSION 0.10.10  
RUN mkdir -p /usr/src/nginx  
WORKDIR /usr/src/nginx  
  
# Download nginx source  
RUN apt-get update && \  
apt-get install -y libluajit-5.1-dev && \  
apt-get source nginx=${NGINX_FULL_VERSION} && \  
apt-get build-dep -y nginx=${NGINX_FULL_VERSION} && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /usr/src/nginx/nginx-${NGINX_VERSION}/debian/modules/  
  
# Download RTMP module  
RUN curl -L https://github.com/arut/nginx-rtmp-
module/archive/v${RTMP_VERSION}.tar.gz | tar xz && \  
ln -s nginx-rtmp-module-${RTMP_VERSION} nginx-rtmp-module  
  
# Download VOD module  
RUN curl -L https://github.com/kaltura/nginx-vod-
module/archive/${VOD_VERSION}.tar.gz | tar xz && \  
ln -s nginx-vod-module-${VOD_VERSION} nginx-vod-module  
  
# Download LUA module  
RUN curl -L https://github.com/openresty/lua-nginx-
module/archive/v${LUA_VERSION}.tar.gz | tar xz && \  
ln -s lua-nginx-module-${LUA_VERSION} lua-nginx-module  
  
# Add modules to build nginx debian rules  
ENV RTMP_MODULE_SOURCE
"\\\\\/usr\\\\\/src\\\\\/nginx\\\\\/nginx-${NGINX_VERSION}\\\\\/debian\\\\\/modules\\\\\/nginx-
rtmp-module"  
ENV VOD_MODULE_SOURCE
"\\\\\/usr\\\\\/src\\\\\/nginx\\\\\/nginx-${NGINX_VERSION}\\\\\/debian\\\\\/modules\\\\\/nginx-
vod-module"  
ENV LUA_MODULE_SOURCE
"\\\\\/usr\\\\\/src\\\\\/nginx\\\\\/nginx-${NGINX_VERSION}\\\\\/debian\\\\\/modules\\\\\/lua-
nginx-module"  
RUN sed -i "s#--with-ipv6#--with-ipv6 --add-module=${RTMP_MODULE_SOURCE}
\--add-module=${VOD_MODULE_SOURCE} \--add-module=${LUA_MODULE_SOURCE}#g"
/usr/src/nginx/nginx-${NGINX_VERSION}/debian/rules  
  
# Build nginx debian package  
WORKDIR /usr/src/nginx/nginx-${NGINX_VERSION}  
RUN dpkg-buildpackage -b  
  
# Install nginx  
WORKDIR /usr/src/nginx  
RUN dpkg -i nginx_${NGINX_FULL_VERSION}_amd64.deb  
  
# Add rtmp config wildcard inclusion  
RUN mkdir -p /etc/nginx/rtmp.d && \  
printf "\nrtmp {\n\tinclude /etc/nginx/rtmp.d/*.conf;\n}\n" >>
/etc/nginx/nginx.conf  
  
# Install ffmpeg / aac / envsubst  
RUN echo 'deb http://www.deb-multimedia.org jessie main non-free' >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y --force-yes \  
deb-multimedia-keyring \  
ffmpeg \  
gettext-base && \  
apt-get autoremove -yqq && \  
apt-get clean -yqq && \  
rm -rf /usr/src/nginx  
  
# Forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
COPY envconf.sh /  
  
VOLUME ["/var/cache/nginx"]  
  
EXPOSE 80 443  
ENTRYPOINT ["/envconf.sh"]  
CMD ["nginx", "-g", "daemon off;"]  

