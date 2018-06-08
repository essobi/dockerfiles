# Quagga from Git source  
  
FROM ubuntu:16.04  
  
MAINTAINER IWASE Yusuke <iwase.yusuke0@gmail.com>  
ARG user=iwaseyusuke  
  
USER root  
WORKDIR /root  
  
ARG branch_name=master  
  
RUN apt-get update && apt-get install -y \--no-install-recommends \  
autoconf \  
automake \  
fakeroot \  
gawk \  
gcc \  
git \  
iproute2 \  
iputils-ping \  
libc-ares-dev \  
libreadline-dev \  
libtool \  
pkg-config \  
tcpdump \  
telnet \  
vim \  
&& rm -rf /var/lib/apt/lists/* \  
&& mv /bin/ping /sbin/ping \  
&& mv /bin/ping6 /sbin/ping6 \  
&& mv /usr/sbin/tcpdump /usr/bin/tcpdump \  
&& git clone -b $branch_name \--single-branch
git://git.savannah.nongnu.org/quagga.git \  
&& cd quagga \  
&& ./bootstrap.sh \  
&& ./configure \  
\--disable-doc \--enable-fpm \  
\--localstatedir=/var/run/quagga \--sysconfdir=/etc/quagga \  
\--enable-user=`whoami` \--enable-group=`whoami` \  
&& mkdir /var/run/quagga \  
&& make \  
&& make install \  
&& ldconfig \  
&& cp -p /etc/quagga/zebra.conf.sample /etc/quagga/zebra.conf \  
&& cp -p /etc/quagga/ripd.conf.sample /etc/quagga/ripd.conf \  
&& cp -p /etc/quagga/ripngd.conf.sample /etc/quagga/ripngd.conf \  
&& cp -p /etc/quagga/ospfd.conf.sample /etc/quagga/ospfd.conf \  
&& cp -p /etc/quagga/ospf6d.conf.sample /etc/quagga/ospf6d.conf \  
&& cp -p /etc/quagga/bgpd.conf.sample /etc/quagga/bgpd.conf \  
&& cp -p /etc/quagga/isisd.conf.sample /etc/quagga/isisd.conf \  
&& cp -p /etc/quagga/pimd.conf.sample /etc/quagga/pimd.conf \  
&& cp -p /etc/quagga/vtysh.conf.sample /etc/quagga/vtysh.conf  

