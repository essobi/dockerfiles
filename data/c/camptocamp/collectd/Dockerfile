FROM debian:stretch-slim  
  
ARG CONFD_VERSION=0.15.0  
ARG
CONFD_SHA256=7f3aba1d803543dd1df3944d014f055112cf8dadf0a583c76dd5f46578ebe3c2  
  
ADD
https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-
amd64 /usr/local/bin/confd  
RUN echo "${CONFD_SHA256} /usr/local/bin/confd" | sha256sum -c -  
RUN chmod 0755 /usr/local/bin/confd  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo 'APT::Install-Recommends "0";' > /etc/apt/apt.conf.d/50no-install-
recommends  
RUN echo 'APT::Install-Suggests "0";' > /etc/apt/apt.conf.d/50no-install-
suggests  
COPY /50collectd /etc/apt/preferences.d/  
  
COPY rootfs_prefix/ /usr/src/rootfs_prefix/  
  
RUN apt-get update \  
&& apt-get -y upgrade \  
&& apt-get -y install \  
gnupg \  
dirmngr \  
&& for server in $(shuf -e ha.pool.sks-keyservers.net \  
hkp://p80.pool.sks-keyservers.net:80 \  
keyserver.ubuntu.com \  
hkp://keyserver.ubuntu.com:80 \  
pgp.mit.edu) ; do \  
apt-key adv --keyserver "${server}" \--recv-keys 0xF4831166EFDCBABE && break
|| : ; \  
done \  
&& echo "deb http://pkg.camptocamp.net/apt stretch/dev collectd-5" >
/etc/apt/sources.list.d/collectd-c2c.list \  
&& apt-get update \  
&& apt-get -y install \  
build-essential \  
curl \  
runit \  
procps \  
netcat-openbsd \  
collectd-core \  
collectd-utils \  
libprotobuf-c1 \  
libmicrohttpd12 \  
libyajl2 \  
&& make -C /usr/src/rootfs_prefix/ \  
&& apt-get -y --purge --autoremove remove build-essential gnupg dirmngr \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN touch /etc/inittab  
RUN mkdir -p /etc/service/collectd/env  
COPY /collectd.run /etc/service/collectd/run  
COPY /collectd.check /etc/service/collectd/check  
  
RUN mkdir -p /etc/collectd/collectd.conf.d  
COPY /collectd.conf /etc/collectd/collectd.conf  
  
ENTRYPOINT ["/etc/runit/2"]  

