FROM ubuntu  
  
# Build parameters  
ARG OPENSSL_VERSION="1.0.2h"  
ARG OPENRESTY_VERSION="1.13.6.1"  
ARG LUAROCKS_VERSION="2.4.1"  
ARG NEWRELIC_SDK_VERSION="v0.16.2.0-beta"  
ARG RESTY_WAF_VERSION="0.11.1-1"  
ARG RESTY_NEWRELIC_VERSION="0.01-6"  
# Default nginx configuration  
ENV NEWRELIC_APP_NAME='core-nex-routing'  
ENV NEWRELIC_APP_LICENSE_KEY=''  
ENV NGX_REAL_IP_HEADER='X-Real-IP'  
ENV NGX_LISTEN_PROTOCOL=''  
ENV NGX_SET_REAL_IP_FROM='localhost'  
ENV RESTY_WAF_MODE='SIMULATE'  
ENV NGX_PROXY_X_FORWARDED_FOR='$proxy_add_x_forwarded_for'  
ENV NGX_PROXY_X_REAL_IP='$remote_addr'  
ENV NGX_PROXY_BACKEND_PORT=80  
# Docker runtime path  
ENV
PATH="/usr/local/bin:/usr/local/openresty/nginx/sbin:/usr/local/openresty/bin:${PATH}"  
# Install base packages  
RUN apt-get update && apt-get install -y \  
build-essential \  
gcc-5 \  
g++-5 \  
libreadline-dev \  
libncurses5-dev \  
libpcre3 \  
libpcre3-dev \  
libssl-dev \  
perl \  
make \  
build-essential \  
zlib1g-dev \  
unzip \  
lua5.1 \  
liblua5.1-0-dev \  
git \  
curl \  
python \  
&& rm -rf /var/lib/apt/lists/*  
  
# Use GCC-5 as lua-resty-waf does not like gcc > 5 currently  
# (Warnings on uninitialized variables are raised as errors during
compilation)  
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-5 60 --slave
/usr/bin/g++ g++ /usr/bin/g++-5  
  
# Install OpenSSL + OpenResty  
RUN cd /tmp \  
&& curl -O https://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz \  
&& tar -xzf openssl-${OPENSSL_VERSION}.tar.gz \  
&& rm -rf openssl-${OPENSSL_VERSION}.tar.gz \  
&& cd /tmp \  
&& rm -rf ngx_openresty-${OPENRESTY_VERSION}* openresty-${OPENRESTY_VERSION}*
\  
&& curl -OL
https://openresty.org/download/openresty-${OPENRESTY_VERSION}.tar.gz \  
&& tar -xzf openresty-${OPENRESTY_VERSION}.tar.gz \  
&& cd /tmp/openresty-${OPENRESTY_VERSION}/ \  
&& export PATH=$PATH:/sbin:/bin:/usr/sbin:/usr/bin \  
&& ./configure \  
\--with-http_ssl_module \  
\--with-luajit \  
\--with-http_realip_module \  
\--with-openssl=/tmp/openssl-${OPENSSL_VERSION}/ \  
&& make \  
&& make install \  
&& rm -rf /etc/nginx \  
&& ln -s /usr/local/openresty/nginx/conf /etc/nginx \  
&& mkdir -p /etc/nginx/lua \  
/etc/nginx/lua-lib \  
/etc/nginx/sites-available \  
/etc/nginx/sites-enabled \  
/etc/nginx/conf.d \  
/etc/nginx/default-certificates \  
/etc/nginx/certificates \  
/var/log/nginx \  
&& chmod 775 /etc/nginx/certificates \  
&& chown root:www-data /etc/nginx/certificates \  
&& chmod 775 -R /usr/local/openresty \  
&& cd /tmp \  
&& rm -rf ngx_openresty-${OPENRESTY_VERSION}* openresty-${OPENRESTY_VERSION}*
\  
&& rm -rf openssl-${OPENSSL_VERSION}  
  
# Install Luarocks  
RUN cd /tmp \  
&& curl -OL https://luarocks.org/releases/luarocks-${LUAROCKS_VERSION}.tar.gz
\  
&& tar zxpf luarocks-${LUAROCKS_VERSION}.tar.gz \  
&& cd luarocks-${LUAROCKS_VERSION} \  
&& ./configure \  
&& make bootstrap  
  
# Install resty-waf  
RUN luarocks install lua-resty-waf ${RESTY_WAF_VERSION}  
  
# Install resty-newrelic  
RUN cd /tmp \  
&& rm -rf nr_agent_sdk-* \  
&& curl -OL
http://download.newrelic.com/agent_sdk/nr_agent_sdk-${NEWRELIC_SDK_VERSION}.x86_64.tar.gz
\  
&& tar -xzf nr_agent_sdk-${NEWRELIC_SDK_VERSION}.x86_64.tar.gz \  
&& cp /tmp/nr_agent_sdk-${NEWRELIC_SDK_VERSION}.x86_64/lib/*.so /lib/ \  
&& luarocks install resty-newrelic ${RESTY_NEWRELIC_VERSION}  
  
# Copy configuration files  
COPY conf.d/ /etc/nginx/conf.d/  
COPY lua/ /etc/nginx/lua/  
COPY lua-lib/ /etc/nginx/lua-lib/  
COPY templates/ /etc/nginx/templates/  
COPY public/ /etc/nginx/public/  
  
# Copy scripts  
COPY bin/ /usr/local/bin/  
RUN chmod +x /usr/local/bin/*.sh  
  
# Healthcheck  
HEALTHCHECK \--timeout=5s CMD bash /usr/local/bin/healthcheck.sh  
  
# Expose persistent folders  
VOLUME ["/var/log/nginx", "/etc/nginx/certificates", "/etc/nginx/mapping"]  
  
# Ports  
EXPOSE 80 443  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["nginx"]  

