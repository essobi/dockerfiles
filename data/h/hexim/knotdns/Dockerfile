FROM debian:stretch  
MAINTAINER admin@best-net.cz  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
WORKDIR /root  
  
ENTRYPOINT /etc/init.d/knot start && bash  
  
EXPOSE 53/tcp 53/udp  
  
# Environment  
ENV THREADS 4  
ENV BUILD_PKGS wget git-core make gcc libtool autoconf pkg-config \  
liburcu-dev liblmdb-dev libgnutls28-dev libjansson-dev libedit-dev
libidn11-dev  
ENV RUNTIME_PKGS liburcu4 liblmdb0 libgnutls30 libjansson4 libedit2 libidn11  
ENV ADD_PKGS nano mc ntpdate openssh-server ssh vim php7.0-cli php7.0-mysql
php7.0-curl phpunit net-tools  
ENV TERM xterm  
  
# Install dependencies and sources  
RUN apt-get -qqy update \  
&& apt-get install -qqy ${BUILD_PKGS} ${RUNTIME_PKGS} ${ADD_PKGS} \  
&& git clone -b v2.6.7 https://gitlab.labs.nic.cz/knot/knot-dns.git /knot-src
\  
&& cd /knot-src \  
&& autoreconf -if \  
&& ./configure --disable-static --enable-fastparser --disable-documentation
--prefix=/usr \  
\--bindir=/usr/sbin/ \--libexecdir=/usr/sbin/ --sbindir=/usr/sbin/
\--sysconfdir=/etc/ \  
\--with-rundir=/var/run/knot/ \  
&& make -j${THREADS} \  
&& make install \  
&& cp /etc/knot/knot.sample.conf /etc/knot/knot.conf \  
&& adduser --quiet --system --group --no-create-home --home /var/lib/knot knot
\  
&& mkdir -p /var/lib/knot/ \  
&& mkdir -p /var/run/knot/ \  
&& chown knot: /etc/knot/ -R \  
&& chown knot: /var/lib/knot/ -R \  
&& chown knot: /var/run/knot/ -R \  
&& touch /etc/default/knot \  
&& echo KNOTD_ARGS=\"\" > /etc/default/knot \  
&& wget https://raw.githubusercontent.com/heximcz/docker-
knotdns/master/examples/etc/init.d/knot -O /etc/init.d/knot \  
&& chmod 777 /etc/init.d/knot \  
&& update-rc.d knot defaults \  
&& ldconfig \  
&& cd \  
&& rm -rf /knot-src \  
&& apt-get purge -q -y ${BUILD_PKGS} \  
&& apt-get autoremove -q -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV DEBIAN_FRONTEND=teletype  
  

