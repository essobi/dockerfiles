#  
# Dockerfile for ShadowsocksR  
#  
FROM alpine:3.4  
ENV SSR_URL https://github.com/shadowsocksr/shadowsocksr/archive/manyuser.zip  
ARG KCP_VER=20170329  
ARG
KCP_URL=https://github.com/xtaci/kcptun/releases/download/v$KCP_VER/kcptun-
linux-amd64-$KCP_VER.tar.gz  
  
RUN set -ex \  
&& apk --update add --no-cache libsodium py-pip curl tar \  
&& pip --no-cache-dir install $SSR_URL \  
&& rm -rf /var/cache/apk \  
&& cd /tmp \  
&& curl -sSL $KCP_URL | tar xz server_linux_amd64 \  
&& mv server_linux_amd64 /usr/bin/  
  
ENV SERVER_ADDR 0.0.0.0  
ENV SERVER_PORT 8388  
ENV PASSWORD sakura  
ENV METHOD chacha20  
ENV PROTOCOL auth_sha1_v4_compatible  
ENV OBFS tls1.2_ticket_auth_compatible  
ENV TIMEOUT 300  
ENV KCP_LISTEN 1024  
ENV KCP_PASS kcptun  
ENV KCP_ENCRYPT aes  
ENV KCP_MODE fast  
ENV KCP_MUT 1350  
EXPOSE $SERVER_PORT/tcp  
EXPOSE $SERVER_PORT/udp  
EXPOSE $KCP_LISTEN/udp  
  
WORKDIR /usr/bin/  
  
CMD ssserver -s $SERVER_ADDR \  
-p $SERVER_PORT \  
-k $PASSWORD \  
-m $METHOD \  
-O $PROTOCOL \  
-o $OBFS \  
-t $TIMEOUT \  
&& server_linux_amd64 -t "127.0.0.1:$SERVER_PORT" \  
-l ":$KCP_LISTEN" \  
-key $KCP_PASS \  
\--mode $KCP_MODE \  
\--crypt $KCP_ENCRYPT \  
\--mtu $KCP_MUT

