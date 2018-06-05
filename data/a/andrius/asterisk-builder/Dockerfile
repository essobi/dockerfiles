# vim:set ft=dockerfile:  
FROM debian:jessie  
  
MAINTAINER Andrius Kairiukstis <andrius@kairiukstis.com>  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -yqq install \  
autoconf \  
automake \  
binutils-dev \  
bison \  
build-essential \  
ca-certificates \  
curl \  
doxygen \  
espeak \  
flex \  
freetds-dev \  
ghostscript \  
git \  
git-core \  
libasound2-dev \  
libc6-dev \  
libcorosync-dev \  
libcurl4-openssl-dev \  
libedit-dev \  
libespeak-dev \  
libffi-dev \  
libgdbm-dev \  
libgsm1-dev \  
libical-dev \  
libiksemel-dev \  
libjansson-dev \  
libmagic-dev \  
libncurses-dev \  
libncurses5-dev \  
libneon27-dev \  
libnewt-dev \  
libogg-dev \  
libpcap-dev \  
libpcre3-dev \  
libpopt-dev \  
libpq-dev \  
libreadline-dev \  
libreadline6 \  
libsamplerate0-dev \  
libsndfile1-dev \  
libsnmp-dev \  
libspandsp-dev \  
libspeexdsp1 \  
libspeex-dev \  
libspeexdsp-dev \  
libsqlite0-dev \  
libsqlite3-dev \  
libsrtp0 \  
libsrtp0-dev \  
libssl-dev \  
libtiff-dev \  
libtiff-tools \  
libtool \  
libusb-dev \  
libvorbis-dev \  
libxml2-dev \  
libxslt-dev \  
libxslt1-dev \  
libyaml-dev \  
minicom \  
mpg123 \  
openssl \  
pkg-config \  
procps \  
rsync \  
sox \  
sqlite3 \  
ssl-cert \  
subversion \  
sudo \  
usbutils \  
uuid \  
uuid-dev \  
wget \  
whois \  
zlib1g \  
zlib1g-dev \  
&& echo "deb http://packages.irontec.com/debian jessie main" >
/etc/apt/sources.list.d/sngrep.list \  
&& wget http://packages.irontec.com/public.key -q -O - | apt-key add - \  
&& apt-get update \  
&& apt-get install -yqq sngrep \  
&& apt-get clean all  
  
RUN mkdir -p /usr/src  
  
RUN cd /usr/src \  
&& git clone https://github.com/asterisk/pjproject.git \  
&& cd /usr/src/pjproject \  
&& ./configure \  
\--enable-shared \  
\--disable-sound \  
\--disable-resample \  
\--disable-video \  
\--disable-opencore-amr \  
\--with-external-speex \  
\--with-external-srtp \  
\--with-external-gsm \  
&& make dep \  
&& make \  
&& make install \  
&& /sbin/ldconfig  
  
ADD asterisk /usr/src/asterisk  
  
# compiling unmodified asterisk from git  
RUN cd /usr/src/asterisk \  
&& ./contrib/scripts/get_mp3_source.sh \  
&& ./contrib/scripts/get_swagger_ui.sh \  
&& ./contrib/scripts/install_prereq install-unpackaged \  
&& /sbin/ldconfig \  
&& ./bootstrap.sh \  
&& ./configure \--with-crypto --with-ssl --with-srtp \  
&& make all \  
&& make install \  
&& make samples \  
&& make config \  
&& make install-logrotate \  
&& /sbin/ldconfig \  
&& /usr/sbin/asterisk -vvvdddF -T -W -U root -p \  
&& sleep 3 \  
&& /usr/sbin/asterisk -rx 'core show uptime'  
  
ADD scripts/sngrep.sh /usr/local/bin/  
ADD scripts/start-ast.sh /usr/local/bin/  
ADD scripts/compile-ast.sh /usr/local/bin/  
ADD scripts/build-ast.sh /usr/local/bin/  
ADD scripts/rebuild-ast.sh /usr/local/bin/  
ADD scripts/docker-start.sh /usr/local/bin/  
  
RUN mkdir -p /var/log/asterisk \  
&& echo "Execute build-asterisk.sh in running container (docker-compose up -d
asterisk; docker-compose exec asterisk build-asterisk.sh)" >
/var/log/asterisk/build.log  
  
WORKDIR /usr/src/asterisk  
  
CMD ["/usr/local/bin/docker-start.sh"]  

