FROM ubuntu:latest  
  
RUN apt-get update && apt-get install -y git build-essential wget autoconf
automake libtool texinfo pkg-config locales python-all-dev python3-all-dev
zlib1g-dev libglib2.0-dev libaio-dev libbluetooth-dev libbrlapi-dev libbz2-dev
libcap-dev libcap-ng-dev libcurl4-gnutls-dev libgtk-3-dev libibverbs-dev
libjpeg8-dev libncurses5-dev libnuma-dev librbd-dev librdmacm-dev libsasl2-dev
libsdl2-dev libseccomp-dev libsnappy-dev libssh2-1-dev libvde-dev libvdeplug-
dev libvte-dev libxen-dev liblzo2-dev valgrind xfslibs-dev libnfs-dev
libiscsi-dev netcat-openbsd  
  
RUN locale-gen "en_US.UTF-8"  
  
ADD download.sh /usr/bin/download.sh  
  
RUN /usr/bin/download.sh  
  

