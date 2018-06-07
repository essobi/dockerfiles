FROM debian:jessie  
  
RUN dpkg --add-architecture i386 \  
&& apt-get -qq update \  
&& apt-get -qq upgrade -y \  
&& apt-get -qq install -y --no-install-recommends \  
ca-certificates \  
wget \  
g++-multilib \  
make \  
git \  
unzip \  
vim \  
less \  
man \  
libssl-dev:i386 \  
libmysqlclient-dev:i386  
  
# CMake  
RUN \  
CMAKE_VERSION=3.10.1 && \  
mkdir -p /tmp/cmake && \  
wget -q -O /tmp/cmake/cmake.sh https://cmake.org/files/v`expr "$CMAKE_VERSION"
: '\\([0-9][0-9]*\\.[0-9][0-9]*\\)'`/cmake-${CMAKE_VERSION}-Linux-x86_64.sh &&
\  
chmod +x /tmp/cmake/cmake.sh && \  
./tmp/cmake/cmake.sh --prefix=/usr/local --exclude-subdir && \  
rm -rf /tmp/cmake  
  
# Boost  
RUN \  
BOOST_VERSION=1.65.1 && \  
mkdir -p /tmp/boost && \  
wget -q -O /tmp/boost/boost.tar.gz
https://dl.bintray.com/boostorg/release/${BOOST_VERSION}/source/boost_`echo
$BOOST_VERSION | sed 's|\\.|_|g'`.tar.gz && \  
tar xfz /tmp/boost/boost.tar.gz -C /tmp/boost/ \--strip-components=1 && \  
cd /tmp/boost && \  
./bootstrap.sh --prefix=/usr/local --with-
libraries=system,chrono,thread,regex,date_time,atomic && \  
./b2 variant=release link=static threading=multi address-model=32 runtime-
link=shared -j2 -d0 install && \  
cd - && \  
rm -rf /tmp/boost  
  
# SA-MP server + includes  
RUN \  
mkdir -p /tmp/samp && \  
wget -q -O /tmp/samp/sampsvr-linux.tar.gz http://files.sa-
mp.com/samp037svr_R2-2-1.tar.gz && \  
tar xfz /tmp/samp/sampsvr-linux.tar.gz -C /root/ && \  
wget -q -O /tmp/samp/sampsvr-win32.zip http://files.sa-
mp.com/samp037_svr_R2-2-1_win32.zip && \  
unzip /tmp/samp/sampsvr-win32.zip pawno/include/* -d /root/samp03 && \  
rm -rf /tmp/samp  
  
# PAWN compiler  
RUN \  
PAWN_COMPILER_VERSION=3.10.6 && \  
mkdir -p /tmp/pawncc && \  
wget -q -O /tmp/pawncc/pawncc.tar.gz
https://github.com/Southclaws/pawn/releases/download/v${PAWN_COMPILER_VERSION}/pawnc-${PAWN_COMPILER_VERSION}-linux.tar.gz
&& \  
tar xfz /tmp/pawncc/pawncc.tar.gz -C /usr/local/ \--strip-components=1 && \  
ldconfig && \  
rm -rf /tmp/pawncc  
  
COPY .bashrc /root  
  
WORKDIR /root  
CMD ["/bin/bash"]  

