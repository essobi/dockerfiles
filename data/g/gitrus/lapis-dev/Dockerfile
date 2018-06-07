FROM ubuntu:16.04  
  
ENV TZ='Etc/GMT'  
  
# install build dependencies  
RUN apt-get -qq update \  
&& apt-get -qq -y install \  
libreadline-dev \  
libncurses5-dev \  
libpcre3-dev \  
libssl-dev \  
libpq-dev \  
libgd-dev \  
libgeoip-dev \  
libncurses5-dev \  
libperl-dev \  
libxslt1-dev \  
ca-certificates \  
build-essential \  
perl \  
make \  
curl \  
git-core \  
luarocks \  
lua-sec \  
tzdata \  
&& echo $TZ > /etc/timezone \  
&& rm /etc/localtime \  
&& ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \  
&& dpkg-reconfigure -f noninteractive tzdata \  
&& apt-get clean  
  
# build/install OpenResty  
ENV OPENRESTY_VERSION=1.11.2.4  
ENV OPENRESTY_PREFIX=/opt/openresty  
ENV LAPIS_VERSION=1.6.0  
ENV BIN_DIR=/tmp  
  
RUN cd $BIN_DIR && curl -LOs
https://openresty.org/download/openresty-$OPENRESTY_VERSION.tar.gz \  
&& tar xzf openresty-$OPENRESTY_VERSION.tar.gz && cd
openresty-$OPENRESTY_VERSION \  
&& ./configure --prefix=$OPENRESTY_PREFIX \  
\--with-file-aio \  
\--with-http_addition_module \  
\--with-http_auth_request_module \  
\--with-http_dav_module \  
\--with-http_flv_module \  
\--with-http_geoip_module=dynamic \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_image_filter_module=dynamic \  
\--with-http_mp4_module \  
\--with-http_postgres_module \  
\--with-http_random_index_module \  
\--with-http_realip_module \  
\--with-http_secure_link_module \  
\--with-http_slice_module \  
\--with-http_ssl_module \  
\--with-http_stub_status_module \  
\--with-http_sub_module \  
\--with-http_v2_module \  
\--with-http_xslt_module=dynamic \  
\--with-ipv6 \  
\--with-luajit \  
\--with-mail \  
\--with-mail_ssl_module \  
\--with-md5-asm \  
\--with-pcre-jit \  
\--with-sha1-asm \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-threads \  
&& make && make install && rm -rf openresty-$OPENRESTY_VERSION* \  
&& luarocks install --server=http://rocks.moonscript.org/manifests/leafo lapis
$LAPIS_VERSION \  
&& luarocks install moonscript \  
&& luarocks install lapis-console \  
&& luarocks install lua-resty-http \  
&& luarocks install luatz \  
&& luarocks install stringy \  
&& mkdir /app  
  
ENV LAPIS_OPENRESTY $OPENRESTY_PREFIX/nginx/sbin/nginx  
  
EXPOSE 443  
EXPOSE 80  
  
WORKDIR /app  
VOLUME /app  
  
# LAPIS_OPENRESTY=/opt/openresty/nginx/sbin/nginx lapis server production  
ENTRYPOINT ["lapis"]  
CMD ["server", "production"]

