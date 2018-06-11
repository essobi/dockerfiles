FROM voidbridge/centos7  
MAINTAINER Voidbridge <developers@voidbridge.com>  
  
LABEL io.k8s.description="HAProxy load balancer" \  
io.k8s.display-name="HAProxy"  
  
RUN haproxy_version="1.6.7" && \  
build_deps="make gcc pcre-static pcre-devel openssl-devel" && \  
yum install -y --enablerepo=centosplus gettext epel-release && \  
yum install -y $build_deps && \  
mkdir /tmp/haproxy-src && \  
curl -fL
http://www.haproxy.org/download/1.6/src/haproxy-${haproxy_version}.tar.gz | \  
tar -zxf - -C /tmp/haproxy-src --strip-components 1 && \  
make -C /tmp/haproxy-src \  
TARGET=linux2628 \  
USE_PCRE=1 \  
USE_OPENSSL=1 \  
USE_ZLIB=1 \  
all install-bin && \  
rm -rf /tmp/haproxy-src && \  
yum remove -y $build_deps && \  
yum install -y rsyslog nodejs npm hostname bind-utils telnet && \  
yum clean all -y && \  
setcap 'cap_net_bind_service=+ep' /usr/local/sbin/haproxy && \  
mkdir /etc/haproxy /var/lib/haproxy && \  
chmod 777 /var/run /etc/haproxy /var/lib/haproxy  
  
# Install Tini  
ADD https://github.com/krallin/tini/releases/download/v0.9.0/tini
/usr/bin/tini  
ADD https://github.com/krallin/tini/releases/download/v0.9.0/tini.asc
/usr/bin/tini.asc  
RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys 0527A9B7 && \  
gpg --verify /usr/bin/tini.asc && \  
chmod 755 /usr/bin/tini  
  
# Prepare NodeJS modules  
ADD files/opt/haproxy-updater/package.json /tmp/node/package.json  
RUN cd /tmp/node && \  
npm install && \  
mkdir -p /opt/haproxy-updater && \  
cp -a /tmp/node/node_modules /opt/haproxy-updater/ && \  
rm -rf /tmp/node  
  
ADD files /  
RUN mkdir -p /var/spool/rsyslog && \  
chmod 755 /usr/bin/run-haproxy && \  
chmod 777 /var/spool/rsyslog  
  
ENV STATS_USERNAME = admin  
ENV STATS_PASSWORD = admin  
  
USER 1001  
EXPOSE 80 1936  
VOLUME /mnt/data  
ENTRYPOINT ["/usr/bin/tini", "--"]  
CMD ["run-haproxy"]  

