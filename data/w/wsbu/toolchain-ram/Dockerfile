FROM ubuntu:16.04  
  
RUN dpkg --add-architecture i386 && apt-get update && apt-get install --yes \  
apt-transport-https \  
autoconf \  
automake \  
autopoint \  
bc \  
bison \  
ccache \  
cmake \  
curl \  
flex \  
g++ \  
gawk \  
gcc \  
gettext \  
git \  
gperf \  
groff \  
intltool \  
kmod \  
lib32z1 \  
libc6-i386 \  
liblzo2-dev \  
libstdc++6:i386 \  
libtool \  
libxml2-utils \  
lua5.3 \  
make \  
mtd-utils \  
net-tools \  
nodejs \  
pkg-config \  
python-m2crypto \  
scons \  
texinfo \  
u-boot-tools \  
uuid-dev \  
xutils-dev \  
zip \  
zlib1g-dev \  
&& rm --recursive --force /var/lib/apt/lists/*  
  
# lua: Scripts expect to run via "lua" command  
# nodejs: ubuntu repo version (non-latest) does not install "node" executable  
RUN ln -sf /usr/bin/lua5.3 /usr/bin/lua \  
&& ln -sf /usr/bin/nodejs /usr/bin/node  
  
RUN git clone --depth=1 --progress --verbose --branch binaries \  
https://github.com/wsbu/toolchain-ram.git /binaries \  
&& yes | /binaries/eldk/install -d /opt/eldk/4.2 arm \  
&& ln -sf 4.2/arm /opt/eldk/arm \  
&& cp -r /binaries/eldk-5.6 /opt \  
&& rm -rf /binaries  
  
ENV WSBU_C11_COMPILER /opt/eldk-5.6/armv5te/sysroots/i686-eldk-
linux/usr/bin/arm-linux-gnueabi/arm-linux-gnueabi-g++  
ENV WSBU_C11_FLAGS \  
-isystem /opt/eldk-5.6/armv5te/sysroots/armv5te-linux-gnueabi/usr/include \  
-isystem /opt/eldk-5.6/armv5te/sysroots/armv5te-linux-gnueabi/usr/include/c++ \  
-isystem /opt/eldk-5.6/armv5te/sysroots/armv5te-linux-gnueabi/usr/include/c++/arm-linux-gnueabi  
  
# Lots of things complain if we are homeless  
ENV HOME /home/captain  
RUN mkdir --parents ${HOME}/.ccache && chmod -R 777 ${HOME}  

