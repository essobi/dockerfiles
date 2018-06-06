FROM column/base:v1  
  
MAINTAINER Column Fang <column.fang@gmail.com>  
  
COPY files /  
  
RUN \  
# Install build tools & openresty dependencies  
apt-get update && \  
apt-get install -y gnupg build-essential libpcre3 libpcre3-dev openssl libssl-
dev ca-certificates && \  
  
# Compile openresty bundle  
curl -L https://openresty.org/download/openresty-1.11.2.3.tar.gz >
/tmp/openresty.tar.gz && \  
tar xzvf /tmp/openresty.tar.gz -C /tmp && \  
cd /tmp/openresty-*/ && \  
./configure && \  
make && \  
make install && \  
  
# Config nginx  
useradd -r -U -s /bin/false -c nginx -d /nonexistent nginx && \  
mv /nginx.conf /usr/local/openresty/nginx/conf && \  
  
# Compile luarocks  
curl -L http://luarocks.github.io/luarocks/releases/luarocks-2.4.2.tar.gz >
/tmp/luarocks.tar.gz && \  
tar xzvf /tmp/luarocks.tar.gz -C /tmp && \  
cd /tmp/luarocks-*/ && \  
./configure \--with-lua="/usr/local/openresty/luajit" \--lua-suffix="jit" \  
\--with-lua-include=/usr/local/openresty/luajit/include/$(ls
/usr/local/openresty/luajit/include)/ && \  
make bootstrap && \  
  
# Cleanup  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME /usr/local/openresty/nginx/conf/conf.d  
EXPOSE 80 443  

