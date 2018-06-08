#  
# NuttX development environment  
#  
  
FROM ubuntu:xenial  
MAINTAINER David Sidrane <david_s5@nscdg.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN dpkg --add-architecture i386 \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -y --quiet --no-install-recommends
install \  
bison \  
bzip2 \  
ca-certificates \  
ccache \  
cmake \  
file \  
flex \  
g++ \  
gcc \  
genromfs \  
git \  
gosu \  
gperf \  
libc6:i386 \  
libgcc1:i386 \  
libncurses-dev \  
libstdc++5:i386 \  
libstdc++6:i386 \  
make \  
ninja-build \  
patch \  
python \  
sudo \  
unzip \  
wget \  
&& apt-get -y autoremove \  
&& apt-get clean autoclean \  
# astyle v2.06  
&& wget
https://downloads.sourceforge.net/project/astyle/astyle/astyle%202.06/astyle_2.06_linux.tar.gz
-O /tmp/astyle.tar.gz \  
&& tar -xvf /tmp/astyle.tar.gz && cd astyle/src && make -f
../build/gcc/Makefile && cp bin/astyle /usr/local/bin && cd .. && rm -rf
astyle \  
# manual ccache setup  
&& ln -s /usr/bin/ccache /usr/lib/ccache/cc \  
&& ln -s /usr/bin/ccache /usr/lib/ccache/c++ \  
# cleanup  
&& rm -rf /var/lib/apt/lists/{apt,dpkg,cache,log} /tmp/* /var/tmp/*  
  
RUN git clone --depth 1 https://bitbucket.org/nuttx/tools.git /tmp/tools; \  
cd /tmp/tools/kconfig-frontends; \  
./configure --enable-mconf -prefix=/usr; \  
make; \  
make install; \  
rm -rf /tmp/*  
  
# GCC 5.4  
RUN mkdir -p /opt/gcc && cd /opt/gcc && \  
wget -qO- https://launchpad.net/gcc-arm-
embedded/5.0/5-2016-q3-update/+download/gcc-arm-none-
eabi-5_4-2016q3-20160926-linux.tar.bz2 | tar jx --strip 1 && \  
rm -rf /opt/gcc/share/doc; \  
ln -s /usr/bin/ccache /usr/lib/ccache/arm-none-eabi-g++; \  
ln -s /usr/bin/ccache /usr/lib/ccache/arm-none-eabi-gcc  
  
ENV CCACHE_CPP2=1  
ENV CCACHE_MAXSIZE=1G  
ENV DISPLAY :0  
ENV PATH "/usr/lib/ccache:/opt/gcc/bin:$PATH"  
ENV TERM=xterm  
  
# create and start as LOCAL_USER_ID  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
  
CMD ["/bin/bash"]  
  

