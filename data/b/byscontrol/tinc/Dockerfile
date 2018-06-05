FROM ubuntu:16.04  
MAINTAINER ByS Control "info@bys-control.com.ar"  
# Remove SUID programs  
RUN for i in `find / -perm +6000 -type f 2>/dev/null`; do chmod a-s $i; done  
  
# Based on https://nwgat.ninja/quick-easy-tinc-1-1-2/  
# Install dev packages  
# Build tinc  
# Install tinc 1.1pre14 dependencies as stated in debian:experimental  
# libc6 (>= 2.15), liblzo2-2, libncurses5 (>= 6), libreadline6 (>= 6.0),
libssl1.1 (>= 1.1.0~pre5), libtinfo5 (>= 6), zlib1g (>= 1:1.1.4), init-system-
helpers (>= 1.18~)  
RUN apt-get update && \  
apt-get install -y build-essential libncurses5-dev libreadline6-dev libzlcore-
dev zlib1g-dev liblzo2-dev libssl-dev && \  
apt-get install -y --no-install-recommends iproute2 supervisor curl && \  
curl http://tinc-vpn.org/packages/tinc-1.1pre15.tar.gz | tar xzC /tmp && \  
cd /tmp/tinc-1.1pre15 && ./configure --prefix=/usr --sysconfdir=/etc
--localstatedir=/var && make && make install && \  
apt-get purge --auto-remove -y build-essential libncurses5-dev
libreadline6-dev libzlcore-dev zlib1g-dev liblzo2-dev libssl-dev && \  
apt-get install -y libc6 liblzo2-2 libncurses5 libreadline6 libssl1.0.0
libtinfo5 zlib1g init-system-helpers && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD scripts/ /root/scripts  
  
EXPOSE 655/tcp 655/udp  
VOLUME /etc/tinc  
  
ENTRYPOINT [ "/usr/bin/supervisord" ]  

