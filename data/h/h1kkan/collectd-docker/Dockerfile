FROM ubuntu:xenial  
MAINTAINER Ivan Golubnichiy <h1kkan@itsyndicate.org>  
  
  
RUN apt-get update && apt-get install -y \  
autoconf \  
automake \  
autotools-dev \  
bison \  
build-essential \  
curl \  
flex \  
nano \  
mc \  
git \  
iptables-dev \  
libcurl4-gnutls-dev \  
libdbi0-dev \  
libesmtp-dev \  
libganglia1-dev \  
libgcrypt11-dev \  
libglib2.0-dev \  
libhiredis-dev \  
libltdl-dev \  
liblvm2-dev \  
libmemcached-dev \  
libmnl-dev \  
libmodbus-dev \  
libmysqlclient-dev \  
libopenipmi-dev \  
liboping-dev \  
libow-dev \  
libpcap-dev \  
libperl-dev \  
libpq-dev \  
libprotobuf-c-dev \  
librabbitmq-dev \  
librrd-dev \  
libsensors4-dev \  
libsnmp-dev \  
libtokyocabinet-dev \  
libtokyotyrant-dev \  
libtool \  
libupsclient-dev \  
libvirt-dev \  
libxml2-dev \  
libyajl-dev \  
linux-libc-dev \  
pkg-config \  
protobuf-c-compiler \  
python-dev && \  
rm -rf /usr/share/doc/* && \  
rm -rf /usr/share/info/* && \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/* \  
&& apt-get autoclean \  
&& apt-get clean \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /usr/share/man/* \  
&& rm -rf /usr/share/info/* \  
&& rm -rf /var/cache/man/*  
  
ENV COLLECTD_VERSION collectd-5.7  
  
WORKDIR /usr/src  
RUN git clone https://github.com/collectd/collectd.git  
WORKDIR /usr/src/collectd  
RUN git checkout $COLLECTD_VERSION  
RUN ./build.sh  
RUN ./configure \  
\--prefix=/usr \  
\--sysconfdir=/etc/collectd \  
\--without-libstatgrab \  
\--without-included-ltdl \  
\--disable-static  
RUN make all  
RUN make install  
RUN make clean  
ADD conf/collectd.conf /etc/collectd/  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

