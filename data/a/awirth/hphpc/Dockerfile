FROM ubuntu:12.04  
# The commands in this file are sourced from  
# https://github.com/facebook/hhvm/wiki/Building-and-installing-HHVM-on-
Ubuntu-12.04/2c4d922e8284805d05cc3917a0de2ffe22f69cfd  
RUN apt-get update && apt-get install -y git-core cmake g++ libboost-dev
libmysqlclient-dev \  
libxml2-dev libmcrypt-dev libicu-dev openssl build-essential binutils-dev \  
libcap-dev libgd2-xpm-dev zlib1g-dev libtbb-dev libonig-dev libpcre3-dev \  
autoconf libtool libcurl4-openssl-dev libboost-system-dev \  
libboost-program-options-dev libboost-filesystem-dev wget memcached \  
libreadline-dev libncurses-dev libmemcached-dev libbz2-dev \  
libc-client2007e-dev php5-mcrypt php5-imagick libgoogle-perftools-dev \  
libcloog-ppl0 libelf-dev libdwarf-dev libunwind7-dev subversion php5-cli  
  
RUN mkdir /hphpc  
WORKDIR /hphpc  
  
ENV CMAKE_PREFIX_PATH=/hphpc  
  
ADD source/hhvm/hphp/third_party/libevent-1.4.14.fb-changes.diff
/hphpc/hhvm/hphp/third_party/libevent-1.4.14.fb-changes.diff  
  
ADD source/libevent /hphpc/libevent  
RUN cd libevent && \  
patch -p1 < /hphpc/hhvm/hphp/third_party/libevent-1.4.14.fb-changes.diff && \  
./autogen.sh && \  
./configure --prefix=$CMAKE_PREFIX_PATH && \  
make && \  
make install  
  
ADD source/curl /hphpc/curl  
RUN cd curl && \  
./buildconf && \  
./configure -prefix=$CMAKE_PREFIX_PATH && \  
make && \  
make install  
  
ADD source/glog /hphpc/glog  
RUN cd glog && \  
./configure --prefix=$CMAKE_PREFIX_PATH && \  
make && \  
make install  
  
ADD source/hhvm /hphpc/hhvm  
ADD hhvm_fixes.patch /hphpc/hhvm_fixes.patch  
  
WORKDIR /hphpc/hhvm  
ENV HPHP_HOME=/hphpc/hhvm HPHP_LIB=/hphpc/hhvm/bin USE_HPHPC=1  
# See patch file for details about what is changed.  
RUN patch -p1 < /hphpc/hhvm_fixes.patch  
  
# Fix up old path via symlink of src -> hphp  
# Reconfigure ubuntu to use /bin/bash for /bin/sh  
RUN ln -s hphp src && \  
echo "no" | dpkg-reconfigure dash  
  
# Just generate the files that break the parallel build manually  
# Then build in parallel  
# use CMAKE_BUILD_TYPE=RelWithDebInfo so we have symbols  
# Which shouldn't really slow down anything  
RUN cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo . && \  
/hphpc/hhvm/hphp/tools/generate_compiler_id.sh && \  
/hphpc/hhvm/hphp/tools/generate_repo_schema.sh && \  
make -j$(nproc)  
  
# Environment for tests to run correctly.  
RUN \  
# The getgroups test expects us to be in more than one group  
adduser root mail && \  
# Some tests expect to be able to setlocale()  
locale-gen --purge en_US.UTF-8 de_DE.UTF-8 fi_FI fr_FR de_DE && \  
echo -e 'LANG="en_US.UTF-8"\nLANGUAGE="en_US:en"\n' > /etc/default/locale && \  
# Some tests in ExtDatetime expect us to be in America/Los_Angeles  
echo "America/Los_Angeles" > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata  
  
# Run our simple sanity tests, should take less than 1 min  
ADD test /hphpc/test  
RUN /hphpc/test/test.sh  
  
CMD bash  

