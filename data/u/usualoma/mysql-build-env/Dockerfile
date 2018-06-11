FROM ubuntu:17.04  
  
MAINTAINER Taku AMANO taku@taaas.jp  
  
RUN set -ex \  
\  
&& apt-get update \  
&& apt-get -y install autoconf automake autopoint autotools-dev binutils bison
\  
bsdmainutils build-essential chrpath cmake cmake-data cpp cpp-6 \  
debhelper dh-apparmor dh-autoreconf dh-python dh-strip-nondeterminism \  
dh-systemd distro-info-data dpkg-dev g++ g++-6 gcc gcc-6 gettext \  
gettext-base groff-base intltool-debian libaio-dev libaio1 \  
libarchive-zip-perl libarchive13 libasan3 libasn1-8-heimdal \  
libatomic1 libbison-dev libbsd-dev libbsd0 libc-dev-bin libc6-dev \  
libcc1-0 libcilkrts5 libcroco3 libcurl3 libdpkg-perl libedit-dev \  
libedit2 libevent-2.0-5 libevent-core-2.0-5 libevent-dev \  
libevent-extra-2.0-5 libevent-openssl-2.0-5 libevent-pthreads-2.0-5 \  
libffi6 libfile-stripnondeterminism-perl libgcc-6-dev libgdbm3 \  
libglib2.0-0 libgmp10 libgnutls30 libgomp1 libgssapi-krb5-2 \  
libgssapi3-heimdal libhcrypto4-heimdal libheimbase1-heimdal \  
libheimntlm0-heimdal libhogweed4 libhx509-5-heimdal libicu57 libidn11 \  
libidn2-0 libisl15 libitm1 libjson-perl libjsoncpp1 libk5crypto3 \  
libkeyutils1 libkrb5-26-heimdal libkrb5-3 libkrb5support0 \  
libldap-2.4-2 libldap-common liblsan0 liblz4-dev liblzo2-2 libmpc3 \  
libmpfr4 libmpx2 libncurses5-dev libnettle6 libnuma-dev libnuma1 \  
libp11-kit0 libperl5.24 libpipeline1 libpsl5 libpython3-stdlib \  
libquadmath0 libroken18-heimdal librtmp1 libsasl2-2 \  
libsasl2-modules-db libsigsegv2 libstdc++-6-dev libtasn1-6 \  
libtimedate-perl libtinfo-dev libtool libtsan0 libubsan0 \  
libunistring0 libuv1 libwind0-heimdal libwrap0 libwrap0-dev libxml2 \  
linux-libc-dev lsb-release m4 make man-db patch perl \  
perl-modules-5.24 po-debconf psmisc python3 python3-minimal python3.5 \  
python3.5-minimal zlib1g-dev \  
libboost1.63 libboost1.63-dev \  
&& apt-get clean \  
&& rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
RUN mkdir /mysql-server  
WORKDIR /mysql-server  

