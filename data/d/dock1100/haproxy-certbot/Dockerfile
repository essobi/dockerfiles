FROM alpine:3.7  
  
ENV HAPROXY_MAJOR 1.8  
ENV HAPROXY_VERSION 1.8.8  
ENV HAPROXY_MD5 8633b6e661169d2fc6a44d82a3aceae5  
  
RUN set -x \  
\  
&& apk add --no-cache --virtual .build-deps \  
ca-certificates \  
gcc \  
libc-dev \  
linux-headers \  
make \  
openssl-dev \  
pcre-dev \  
readline-dev \  
tar \  
zlib-dev \  
# install HAProxy  
&& wget -O haproxy.tar.gz
"http://www.haproxy.org/download/${HAPROXY_MAJOR}/src/haproxy-${HAPROXY_VERSION}.tar.gz"
\  
&& echo "$HAPROXY_MD5 *haproxy.tar.gz" | md5sum -c \  
&& mkdir -p /usr/src/haproxy \  
&& tar -xzf haproxy.tar.gz -C /usr/src/haproxy --strip-components=1 \  
&& rm haproxy.tar.gz \  
\  
&& makeOpts=' \  
TARGET=linux2628 \  
USE_OPENSSL=1 \  
USE_PCRE=1 PCREDIR= \  
USE_ZLIB=1 \  
' \  
&& make -C /usr/src/haproxy -j "$(getconf _NPROCESSORS_ONLN)" all $makeOpts \  
&& make -C /usr/src/haproxy install-bin $makeOpts \  
\  
&& mkdir -p /usr/local/etc/haproxy \  
&& cp -R /usr/src/haproxy/examples/errorfiles /usr/local/etc/haproxy/errors \  
&& rm -rf /usr/src/haproxy \  
\  
&& runDeps="$( \  
scanelf --needed --nobanner --format '%n#p' --recursive /usr/local \  
| tr ',' '\n' \  
| sort -u \  
| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1
}' \  
)" \  
&& apk add --virtual .haproxy-rundeps $runDeps \  
&& apk del .build-deps  
  
# Install certbot, supervisor, cron, libnl-utils, net-tools, iptables  
# "certbot>=0.22" \- minimum version of certbot with ACME v2 support  
RUN echo http://nl.alpinelinux.org/alpine/edge/community >>
/etc/apk/repositories  
RUN apk add --no-cache --update \  
supervisor \  
dcron \  
libnl3-cli \  
net-tools \  
iproute2 \  
"certbot>=0.22" \  
openssl \  
&& rm -rf /var/cache/apk/*  
  
# Setup Supervisor  
RUN mkdir -p /var/log/supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Setup Certbot  
RUN mkdir -p /usr/local/etc/haproxy/certs.d  
RUN mkdir -p /usr/local/etc/letsencrypt  
COPY certbot.cron /etc/cron.d/certbot  
COPY cli.ini /usr/local/etc/letsencrypt/cli.ini  
COPY haproxy-refresh.sh /usr/bin/haproxy-refresh  
COPY haproxy-restart.sh /usr/bin/haproxy-restart  
COPY haproxy-check.sh /usr/bin/haproxy-check  
COPY certbot-certonly.sh /usr/bin/certbot-certonly  
COPY certbot-renew.sh /usr/bin/certbot-renew  
RUN chmod +x /usr/bin/haproxy-refresh /usr/bin/haproxy-restart
/usr/bin/haproxy-check /usr/bin/certbot-certonly /usr/bin/certbot-renew  
  
# Add startup script  
COPY start.sh /start.sh  
RUN chmod +x /start.sh  
  
EXPOSE 80 443  
VOLUME ["/config/", "/etc/letsencrypt/", "/usr/local/etc/haproxy/certs.d/",
"/var/log/supervisord/"]  
  
# Start  
CMD ["/start.sh"]  

