# Base OS  
FROM centos:7  
MAINTAINER info@incendonet.com  
  
# Env setup  
ENV HOME /root  
ENV ASTERISK_RELEASE certified-13.13-cert4  
ENV PJSIP_RELEASE 2.5.5  
WORKDIR ~/  
  
# Build deps  
RUN \  
yum -y update && \  
yum -y install epel-release &&\  
yum -y install \  
autoconf \  
automake \  
bzip2 \  
gcc-c++ \  
jansson-devel \  
libtool \  
libuuid-devel \  
libxml2-devel \  
ncurses-devel \  
make \  
sqlite-devel \  
tar \  
uuid-devel \  
wget && \  
yum clean all  
  
# Asterisk and dependencies install  
RUN \  
wget
http://www.pjsip.org/release/${PJSIP_RELEASE}/pjproject-${PJSIP_RELEASE}.tar.bz2
&& \  
tar -xjf pjproject-${PJSIP_RELEASE}.tar.bz2 && \  
cd pjproject-${PJSIP_RELEASE} && \  
./configure --prefix=/usr --enable-shared --disable-sound --disable-resample
--disable-video --disable-opencore-amr CFLAGS='-O2 -DNDEBUG -mtune=generic' &&
\  
make dep && \  
make && \  
make install && \  
ldconfig && \  
#ldconfig -p | grep pj && \  
cd .. && \  
export PKG_CONFIG_PATH=/usr/lib/pkgconfig && \  
  
wget http://downloads.asterisk.org/pub/telephony/certified-
asterisk/asterisk-${ASTERISK_RELEASE}.tar.gz && \  
tar -xzf asterisk-${ASTERISK_RELEASE}.tar.gz && \  
cd asterisk-${ASTERISK_RELEASE} && \  
./configure && \  
  
make menuselect.makeopts && \  
menuselect/menuselect \  
\--disable-category MENUSELECT_ADDONS \  
\--disable-category MENUSELECT_MOH \  
\--disable-category MENUSELECT_EXTRA_SOUNDS \  
\--disable-category MENUSELECT_AGIS \  
\--disable-category MENUSELECT_TESTS \  
\--disable BUILD_NATIVE \  
\--enable chan_pjsip \  
menuselect.makeopts && \  
make && \  
make install && \  
ldconfig && \  
#ldconfig -p | grep libast && \  
#make samples && \  
rm -Rf /etc/asterisk && \  
cd .. && \  
  
# Cleanup  
rm -Rf pjproject* && \  
rm -Rf asterisk* && \  
rm -f *.tar.*  
  
EXPOSE \  
5060-5061 \  
10000-10999  
  
CMD ["/usr/sbin/asterisk", "-cv"]  

