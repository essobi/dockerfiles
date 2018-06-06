FROM docker:dind  
ENV GLIBC_VERSION 2.25-r0  
ENV DOCKER_COMPOSE_VERSION 1.14.0  
ENV DROPBEAR_VERSION 2017.75  
  
RUN apk add \--update \--no-cache tzdata && cp
/usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" >
/etc/timezone && apk del tzdata  
  
RUN apk add \--update \--no-cache curl bash && curl -fsSL
https://bin.equinox.io/c/ekMN3bCZFUn/forego-stable-linux-amd64.tgz | tar xzv
-C /usr/local/bin && chmod +x /usr/local/bin/forego  
  
RUN apk add \--update \--no-cache \--virtual .build-deps linux-pam-dev build-
base zlib-dev linux-headers && \  
curl -fsSL
https://matt.ucc.asn.au/dropbear/releases/dropbear-${DROPBEAR_VERSION}.tar.bz2
-o /tmp/dropbear-${DROPBEAR_VERSION}.tar.bz2 && \  
tar xf /tmp/dropbear-${DROPBEAR_VERSION}.tar.bz2 -C /tmp && \  
cd /tmp/dropbear-${DROPBEAR_VERSION} && \  
./configure \--prefix=/usr \--sysconfdir=/etc \--mandir=/usr/share/man
\--infodir=/usr/share/info \--localstatedir=/var \--enable-pam \--disable-wtmp
&& \  
make dropbear dropbearkey dbclient dropbearconvert scp && \  
strip dropbear dropbearkey dbclient dropbearconvert scp && \  
cp dropbear /usr/sbin && cp dbclient dropbearkey scp /usr/bin && ln -s
/usr/bin/dbclient /usr/bin/ssh && \  
mkdir /etc/dropbear && touch /var/log/lastlog && mkdir -m 700 -p /root/.ssh &&
\  
apk del .build-deps && \  
rm -rf /tmp/dropbear-${DROPBEAR_VERSION}
/tmp/dropbear-${DROPBEAR_VERSION}.tar.bz2  
  
RUN apk add \--update \--no-cache vim nmap lftp netcat-openbsd tmux htop iftop
git sed gawk wget iperf iproute2 && rm /usr/bin/vi && ln -s /usr/bin/vim
/usr/bin/vi  
  
RUN curl -LOsS https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk && \  
curl -LsS -o /etc/apk/keys/sgerrand.rsa.pub
https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/sgerrand.rsa.pub && \  
apk add glibc-${GLIBC_VERSION}.apk && \  
rm /etc/apk/keys/sgerrand.rsa.pub glibc-${GLIBC_VERSION}.apk && \  
ln -s /lib/libz.so.1 /usr/glibc-compat/lib/ && \  
ln -s /lib/libc.musl-x86_64.so.1 /usr/glibc-compat/lib  
  
RUN curl -L
https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-
compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose && chmod +x
/usr/local/bin/docker-compose  
  
ADD Procfile docker-compose.yml docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["forego", "start", "-r"]  

