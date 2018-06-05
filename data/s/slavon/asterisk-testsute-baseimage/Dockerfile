FROM gcc  
  
MAINTAINER Badalyan Vyacheslav <v.badalyan@open-bs.ru>  
  
ENV libsrtp_tag=v1.5.4  
ENV pjproject_branch=trunk  
ENV sipp_tag=v3.5.1  
  
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update -y --force-yes &&
apt-get dist-upgrade -y --force-yes && \  
apt-get install -qq -y -o Dpkg::Options::="--force-confdef" -o
Dpkg::Options::="--force-confold" \  
autoconf \  
binutils-dev \  
build-essential \  
doxygen \  
freetds-dev \  
git \  
libasound2-dev \  
libbluetooth-dev \  
libc-client-dev \  
libcorosync-dev \  
libcurl4-openssl-dev \  
libedit-dev \  
libfreeradius-client-dev \  
libfreeradius-dev \  
libgmime-2.6-dev \  
libgsl0-dev \  
libgsm1-dev \  
libical-dev \  
libiksemel-dev \  
libjack-dev \  
libjansson-dev \  
libldap-dev \  
liblua5.1-dev \  
liblua5.2-dev \  
libmysqlclient-dev \  
libncurses-dev \  
libneon27-dev \  
libnewt-dev \  
libogg-dev \  
libpcap-dev \  
libpopt-dev \  
libpq-dev \  
libresample-dev \  
libsctp-dev \  
libsnmp-dev \  
libspandsp-dev \  
libspeex-dev \  
libspeexdsp-dev \  
libsqlite3-dev \  
libssl-dev \  
libusb-dev \  
libvorbis-dev \  
libvpb-dev \  
libxml2-dev \  
libxslt1-dev \  
libz-dev \  
lua5.2 \  
lua5.1 \  
python-autobahn \  
python-requests \  
python-dev \  
python-setuptools \  
python-twisted \  
python-yaml \  
subversion \  
unixodbc-dev \  
uuid \  
xmlstarlet \  
subversion \  
psmisc \  
uuid-dev && \  
apt-get clean all && \  
rm -rf /var/lib/apt/lists/*  
  
### SIP-P  
  
RUN git clone -b ${sipp_tag} --depth 1 https://github.com/SIPp/sipp.git
/usr/src/sipp && \  
cd /usr/src/sipp && \  
./build.sh --full && make install && \  
rm -rf /usr/src/sipp  
  
### LIBSRTP  
  
RUN git clone -b ${libsrtp_tag} --depth 1 https://github.com/cisco/libsrtp.git
/usr/src/libsrtp && \  
cd /usr/src/libsrtp && \  
./configure --enable-openssl --prefix=/usr && \  
make && make libsrtp.so.1 && make install && ldconfig && \  
rm -rf /usr/src/libsrtp  
  
### PJPROJECT  
  
RUN svn co http://svn.pjsip.org/repos/pjproject/${pjproject_branch}
/usr/src/pjproject && \  
cd /usr/src/pjproject && \  
./configure --enable-shared --with-external-srtp --disable-sound --disable-
resample --disable-video --disable-opencore-amr --prefix=/usr
CFLAGS='-DPJ_HAS_IPV6=1 -O2 -g -DTLSEXT_nid_unknown=0x1000000' && \  
make dep && make && make install && \  
cp pjsip-apps/bin/pjsua-x86_64-unknown-linux-gnu /usr/sbin/pjsua && \  
make -C pjsip-apps/src/python install && ldconfig && \  
rm -rf /usr/src/pjproject  
  
  

