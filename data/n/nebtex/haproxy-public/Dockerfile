# Much of this stolen from haproxy:1.6 dockerfile, with Lua support  
FROM debian:jessie  
  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >
/etc/apt/sources.list.d/jessie.backports.list  
  
ENV SUPERVISOR_VERSION 3.3.0  
RUN buildDeps='curl gcc libc6-dev libpcre3-dev libssl-dev make libreadline-
dev' \  
&& set -x \  
&& apt-get update && apt-get install --no-install-recommends -yqq $buildDeps \  
cron \  
wget \  
ca-certificates \  
curl \  
patch \  
unzip \  
iptables \  
python-setuptools \  
libssl1.0.0 libpcre3 \  
&& apt-get install --no-install-recommends -yqq certbot -t jessie-backports \  
&& wget
https://github.com/Supervisor/supervisor/archive/${SUPERVISOR_VERSION}.tar.gz
\  
&& tar -xvf ${SUPERVISOR_VERSION}.tar.gz \  
&& cd supervisor-${SUPERVISOR_VERSION} && python setup.py install \  
&& apt-get clean autoclean && apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV CONSUL_TEMPLATE_VERSION=0.14.0  
ENV CONSUL_TEMPLATE=/usr/local/bin/consul-template  
ENV CONSUL_CONFIG=/consul-template/config.d  
ENV CONSUL_CONNECT=consul.service.consul:8500  
ENV CONSUL_MINWAIT=2s  
ENV CONSUL_MAXWAIT=10s  
ENV CONSUL_LOGLEVEL=info  
ADD https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip /  
  
RUN unzip /consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \  
mv /consul-template /usr/local/bin/consul-template && \  
rm -rf /consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip  
  
RUN mkdir -p /consul-template/config.d /consul-template/template.d  
ADD config/ /consul-template/config.d/  
ADD template/ /consul-template/template.d/  
  
ENV LUA_VERSION 5.3.0  
ENV LUA_VERSION_SHORT 53  
RUN cd /usr/src \  
&& curl -R -O http://www.lua.org/ftp/lua-${LUA_VERSION}.tar.gz \  
&& tar zxf lua-${LUA_VERSION}.tar.gz \  
&& rm lua-${LUA_VERSION}.tar.gz \  
&& cd lua-${LUA_VERSION} \  
&& make linux \  
&& make INSTALL_TOP=/opt/lua${LUA_VERSION_SHORT} install  
  
ENV HAPROXY_MAJOR 1.6  
ENV HAPROXY_VERSION 1.6.5  
ENV HAPROXY_MD5 5290f278c04e682e42ab71fed26fc082  
  
RUN cd / && curl -SL
"http://www.haproxy.org/download/${HAPROXY_MAJOR}/src/haproxy-${HAPROXY_VERSION}.tar.gz"
-o haproxy.tar.gz \  
&& echo "${HAPROXY_MD5} haproxy.tar.gz" | md5sum -c \  
&& mkdir -p /usr/src/haproxy \  
&& tar -xzf haproxy.tar.gz -C /usr/src/haproxy --strip-components=1 \  
&& rm haproxy.tar.gz \  
&& make -C /usr/src/haproxy \  
TARGET=linux2628 \  
USE_PCRE=1 PCREDIR= \  
USE_OPENSSL=1 \  
USE_ZLIB=1 \  
USE_LUA=yes LUA_LIB=/opt/lua53/lib/ \  
LUA_INC=/opt/lua53/include/ LDFLAGS=-ldl \  
all \  
install-bin \  
&& mkdir -p /usr/local/etc/haproxy \  
&& cp -R /usr/src/haproxy/examples/errorfiles /usr/local/etc/haproxy/errors \  
&& rm -rf /usr/src/haproxy  
  
COPY run_consul_template.sh /  
COPY docker-entrypoint.sh /  
  
ADD reload.sh /  
RUN chmod +x reload.sh  
RUN chmod +x run_consul_template.sh  
  
# See https://github.com/janeczku/haproxy-acme-validation-plugin  
COPY haproxy-acme-validation-plugin/acme-http01-webroot.lua
/usr/local/etc/haproxy/  
COPY haproxy-acme-validation-plugin/cert-renewal-haproxy.sh /  
  
COPY crontab.txt /var/crontab.txt  
RUN crontab /var/crontab.txt && chmod 600 /etc/crontab  
  
COPY supervisord.conf /etc/  
COPY certs.sh /  
COPY bootstrap.sh /  
  
RUN mkdir /jail  
  
EXPOSE 80 443 1936  
VOLUME /etc/letsencrypt  
  
ENTRYPOINT ["/bootstrap.sh"]  

