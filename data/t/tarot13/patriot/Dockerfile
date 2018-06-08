FROM alpine  
  
LABEL maintainer "Ian Li <OpenSource@ianli.xyz>"  
  
ARG V2RAY_VER=3.6  
ARG OC_VERSION=0.11.10  
  
RUN apk add --no-cache bash curl nano ca-certificates bind-tools python py-pip
haproxy gnutls gnutls-utils && \  
apk add --no-cache --virtual .ocserv-runtime-dependencies iptables musl
openssl readline libnl3 lz4 lz4-libs libseccomp libev geoip && \  
apk add --no-cache --virtual .ocserv-build-dependencies build-base unzip xz
linux-headers musl-dev gnutls-dev readline-dev libnl3-dev lz4-dev libseccomp-
dev libev-dev geoip-dev && \  
pip install supervisor supervisor-stdout && \  
curl -O https://raw.githubusercontent.com/tests-always-included/mo/master/mo
&& \  
mv mo /usr/local/bin && \  
chmod +x /usr/local/bin/mo && \  
curl -L "https://github.com/v2ray/v2ray-
core/releases/download/v${V2RAY_VER}/v2ray-linux-64.zip" -o /tmp/v2ray.zip &&
\  
unzip /tmp/v2ray.zip -d /tmp/ && \  
mv /tmp/v2ray-v${V2RAY_VER}-linux-64/v2ray /usr/local/bin/v2ray && \  
mv /tmp/v2ray-v${V2RAY_VER}-linux-64/v2ctl /usr/local/bin/v2ctl && \  
chmod +x /usr/local/bin/v2ray && \  
chmod +x /usr/local/bin/v2ctl && \  
rm -rf /tmp/v2ray* && \  
mkdir /src && cd /src && \  
OC_FILE="ocserv-$OC_VERSION" && \  
wget ftp://ftp.infradead.org/pub/ocserv/$OC_FILE.tar.xz && \  
tar xJf $OC_FILE.tar.xz && \  
rm $OC_FILE.tar.xz && \  
cd $OC_FILE && \  
sed -i '/#define DEFAULT_CONFIG_ENTRIES /{s/96/200/}' src/vpn.h && \  
./configure && \  
make -j"$(nproc)" && \  
make install && \  
mkdir -p /etc/ocserv && \  
cd .. && \  
rm -rf $OC_FILE && \  
cd / && \  
rm -rf /src && \  
apk del .ocserv-build-dependencies && \  
curl -L -O
https://github.com/techotaku/patriot/raw/master/docker/entrypoint.sh && \  
curl -L -O https://github.com/techotaku/patriot/raw/master/docker/gencert.sh
&& \  
chmod +x entrypoint.sh && \  
mv entrypoint.sh /usr/local/bin/entrypoint.sh && \  
chmod +x gencert.sh && \  
mv gencert.sh /usr/local/bin/gencert.sh && \  
mkdir -p /etc/mo/template && \  
curl -L
https://github.com/techotaku/patriot/raw/master/docker/template/Caddyfile.template
-o /etc/mo/template/Caddyfile.template && \  
curl -L
https://github.com/techotaku/patriot/raw/master/docker/template/index.html.template
-o /etc/mo/template/index.html.template && \  
curl -L
https://github.com/techotaku/patriot/raw/master/docker/template/config.websocket.json.template
-o /etc/mo/template/config.websocket.json.template && \  
curl -L
https://github.com/techotaku/patriot/raw/master/docker/template/haproxy.cfg.template
-o /etc/mo/template/haproxy.cfg.template && \  
curl -L
https://github.com/techotaku/patriot/raw/master/docker/template/ocserv.conf.template
-o /etc/mo/template/ocserv.conf.template && \  
curl -L
https://github.com/techotaku/patriot/raw/master/docker/template/supervisord.conf.template
-o /etc/mo/template/supervisord.conf.template && \  
curl https://getcaddy.com | bash -s personal http.proxyprotocol  
  
ENTRYPOINT ["entrypoint.sh"]  

