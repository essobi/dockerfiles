#  
# Docker AppShield  
#  
  
# Pick Our Base Image  
FROM phusion/baseimage:0.9.22  
  
# ################################################################  
# Install OpenResty & Configure  
# ################################################################  
  
# Docker Build Arguments  
ARG RESTY_VERSION="1.13.6.1"  
ARG RESTY_LUAROCKS_VERSION="2.4.3"  
ARG RESTY_OPENSSL_VERSION="1.0.2k"  
ARG RESTY_PCRE_VERSION="8.41"  
ARG RESTY_NAXSI_VERSION="0.55.3"  
ARG RESTY_J="1"  
ARG RESTY_CONFIG_OPTIONS="\  
\--with-file-aio \  
\--with-http_geoip_module=dynamic \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_realip_module \  
\--with-http_secure_link_module \  
\--with-http_ssl_module \  
\--with-http_stub_status_module \  
\--with-http_v2_module \  
\--with-http_auth_request_module \  
\--with-ipv6 \  
\--with-md5-asm \  
\--with-pcre-jit \  
\--with-sha1-asm \  
\--with-threads \  
"  
  
# Append More Config Arguments  
ARG RESTY_CONFIG_OPTIONS_MORE=""  
  
# These are not intended to be user-specified  
ARG _RESTY_CONFIG_DEPS="--add-
module=/tmp/naxsi-${RESTY_NAXSI_VERSION}/naxsi_src/ --with-
openssl=/tmp/openssl-${RESTY_OPENSSL_VERSION} --with-
pcre=/tmp/pcre-${RESTY_PCRE_VERSION}"  
  
# Install Deps , Download , Build , Cleanup  
RUN DEBIAN_FRONTEND=noninteractive apt-get update &&
DEBIAN_FRONTEND=noninteractive apt-get -y upgrade \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
build-essential \  
ca-certificates \  
curl \  
gettext-base \  
libgeoip-dev \  
libncurses5-dev \  
libperl-dev \  
libreadline-dev \  
make \  
perl \  
unzip \  
zlib1g-dev \  
wget \  
&& cd /tmp \  
&& curl -fSL
https://www.openssl.org/source/openssl-${RESTY_OPENSSL_VERSION}.tar.gz -o
openssl-${RESTY_OPENSSL_VERSION}.tar.gz \  
&& tar xzf openssl-${RESTY_OPENSSL_VERSION}.tar.gz \  
&& curl -fSL https://ftp.pcre.org/pub/pcre/pcre-${RESTY_PCRE_VERSION}.tar.gz
-o pcre-${RESTY_PCRE_VERSION}.tar.gz \  
&& tar xzf pcre-${RESTY_PCRE_VERSION}.tar.gz \  
&& curl -fSL https://github.com/nbs-
system/naxsi/archive/${RESTY_NAXSI_VERSION}.tar.gz -o
naxsi-${RESTY_NAXSI_VERSION}.tar.gz \  
&& tar xzf naxsi-${RESTY_NAXSI_VERSION}.tar.gz \  
&& curl -fSL https://openresty.org/download/openresty-${RESTY_VERSION}.tar.gz
-o openresty-${RESTY_VERSION}.tar.gz \  
&& tar xzf openresty-${RESTY_VERSION}.tar.gz \  
&& cd /tmp/openresty-${RESTY_VERSION} \  
&& ./configure -j${RESTY_J} ${_RESTY_CONFIG_DEPS} ${RESTY_CONFIG_OPTIONS}
${RESTY_CONFIG_OPTIONS_MORE} \  
&& make -j${RESTY_J} \  
&& make -j${RESTY_J} install \  
&& cd /tmp \  
&& rm -rf \  
openssl-${RESTY_OPENSSL_VERSION} \  
openssl-${RESTY_OPENSSL_VERSION}.tar.gz \  
openresty-${RESTY_VERSION}.tar.gz openresty-${RESTY_VERSION} \  
pcre-${RESTY_PCRE_VERSION}.tar.gz pcre-${RESTY_PCRE_VERSION} \  
naxsi-${RESTY_NAXSI_VERSION}.tar.gz naxsi-${RESTY_NAXSI_VERSION} \  
&& curl -fSL
https://github.com/luarocks/luarocks/archive/${RESTY_LUAROCKS_VERSION}.tar.gz
-o luarocks-${RESTY_LUAROCKS_VERSION}.tar.gz \  
&& tar xzf luarocks-${RESTY_LUAROCKS_VERSION}.tar.gz \  
&& cd luarocks-${RESTY_LUAROCKS_VERSION} \  
&& ./configure \  
\--prefix=/usr/local/openresty/luajit \  
\--with-lua=/usr/local/openresty/luajit \  
\--lua-suffix=jit-2.1.0-beta3 \  
\--with-lua-include=/usr/local/openresty/luajit/include/luajit-2.1 \  
&& make build \  
&& make install \  
&& cd /tmp \  
&& rm -rf luarocks-${RESTY_LUAROCKS_VERSION}
luarocks-${RESTY_LUAROCKS_VERSION}.tar.gz  
  
# Add Binaries To PATH  
ENV
PATH=$PATH:/usr/local/openresty/luajit/bin/:/usr/local/openresty/nginx/sbin/:/usr/local/openresty/bin/  
  
# ################################################################  
# Install OS Config & Scripts  
# ################################################################  
  
ADD cron.d /etc/cron.d/  
ADD my_init.d /etc/my_init.d/  
ADD service /etc/service/  
ADD scripts /opt/scripts/  
RUN chmod 755 /etc/my_init.d/* && \  
chmod -R 755 /etc/service/* && \  
chmod 755 -R /opt/scripts/*  
  
# ################################################################  
# Install NGINX Config & Setup OPM && Nginx LogRotate  
# ################################################################  
  
ADD config/nginx /etc/nginx/  
RUN mkdir -p /var/log/nginx/ && chown www-data:www-data /var/log/nginx/ && \  
opm get hamishforbes/lua-resty-iputils && \  
opm get openresty/lua-resty-limit-traffic && \  
mv /opt/scripts/logrotate_nginx /etc/logrotate.d/nginx  
  
# ################################################################  
# Install BotBlocker  
# ################################################################  
  
RUN curl -fSL https://raw.githubusercontent.com/mitchellkrogza/nginx-ultimate-
bad-bot-blocker/master/install-ngxblocker -o install-ngxblocker && \  
chmod +x install-ngxblocker && ./install-ngxblocker -x && rm install-
ngxblocker && /usr/local/sbin/setup-ngxblocker -x && \  
cp /etc/nginx/bots.d/blacklist-ips.conf /etc/nginx/bots.d/blacklist-
ips.conf.orig  
  
# ################################################################  
# Clean Image  
# ################################################################  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get autoremove -y && apt-get clean &&
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

