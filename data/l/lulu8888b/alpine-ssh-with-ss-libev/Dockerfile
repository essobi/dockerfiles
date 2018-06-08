FROM alpine:latest  
MAINTAINER lulu8888b  
WORKDIR /  
  
ENV SS_VER=2.5.6  
ENV SS_URL=https://github.com/shadowsocks/shadowsocks-
libev/archive/v$SS_VER.tar.gz  
  
ENV SERVER_ADDR 0.0.0.0  
ENV SERVER_PORT 8888  
ENV PASSWORD password  
ENV METHOD chacha20  
ENV TIMEOUT 300  
ENV DNS_ADDR 8.8.8.8  
ENV DNS_ADDR_2 8.8.4.4  
#install ssh  
# make sure the package repository is up to date  
RUN apk update && apk upgrade  
# install dropbear as the sshd  
RUN apk add openssh openssh-sftp-server byobu tmux && \  
/bin/sed -i -e 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config && \  
/bin/sed -i -e 's/#PermitUserEnvironment no/PermitUserEnvironment yes/'
/etc/ssh/sshd_config && \  
mkdir -p /root/.ssh && \  
chmod 700 /root/.ssh && \  
/usr/bin/ssh-keygen -A && \  
echo "source /etc/profile.d/color_prompt" > /root/.bashrc && \  
echo "root:root" | chpasswd && \  
su - root -c "byobu-launcher-install"  
ADD sshd.sh /  
# expose ports for ssh  
EXPOSE 22  
CMD ["/sshd.sh"]  
  
#install shadowsocks  
RUN set -ex && \  
apk add --no-cache --virtual .build-deps \  
asciidoc \  
autoconf \  
build-base \  
curl \  
libtool \  
linux-headers \  
openssl-dev \  
pcre-dev \  
tar \  
xmlto && \  
cd /tmp && \  
curl -sSL $SS_URL | tar xz --strip 1 && \  
./configure --prefix=/usr --disable-documentation && \  
make install && \  
cd .. && \  
  
runDeps="$( \  
scanelf --needed --nobanner /usr/bin/ss-* \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| xargs -r apk info --installed \  
| sort -u \  
)" && \  
apk add \--no-cache --virtual .run-deps $runDeps && \  
apk del .build-deps && \  
rm -rf /tmp/* && \  
mv /usr/bin/ss-server /usr/bin/ssserver  
  
USER nobody  
  
EXPOSE $SERVER_PORT/tcp $SERVER_PORT/udp  
  
CMD ssserver -s $SERVER_ADDR \  
-p $SERVER_PORT \  
-k ${PASSWORD:-$(hostname)} \  
-m $METHOD \  
-t $TIMEOUT \  
\--fast-open \  
-d $DNS_ADDR \  
-d $DNS_ADDR_2 \  
-u  

