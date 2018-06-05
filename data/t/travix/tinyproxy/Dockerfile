FROM travix/base-alpine:3.5  
MAINTAINER Travix  
  
ENV TINYPROXY_VERSION=1.8  
RUN adduser -D -u 2000 -h /var/run/tinyproxy -s /sbin/nologin tinyproxy
tinyproxy \  
&& apk --update add -t build-dependencies \  
make \  
libcap \  
automake \  
autoconf \  
g++ \  
asciidoc \  
git \  
&& rm -rf /var/cache/apk/* \  
&& git clone -b ${TINYPROXY_VERSION} \--depth=1
https://github.com/tinyproxy/tinyproxy.git /tmp/tinyproxy \  
&& cd /tmp/tinyproxy \  
&& ./autogen.sh \  
&& ./configure --enable-transparent --prefix="" \  
&& make \  
&& make install \  
&& mkdir -p /var/log/tinyproxy \  
&& chown tinyproxy:tinyproxy /var/log/tinyproxy \  
&& cd / \  
&& rm -rf /tmp/tinyproxy \  
&& setcap 'cap_net_bind_service=+ep' /sbin/tinyproxy \  
&& apk del build-dependencies  
  
COPY tinyproxy.conf /etc/tinyproxy/tinyproxy.conf  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
USER tinyproxy  
  
EXPOSE 8888  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["tinyproxy", "-d"]  

