FROM debian:jessie  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y apt-utils \  
&& DEBIAN_FRONTEND=noninteractive dpkg-reconfigure apt-utils \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
automake \  
cmake \  
curl \  
fakeroot \  
g++ \  
git \  
make \  
runit \  
sudo \  
xz-utils \  
pkg-config \  
libasound2-dev \  
libfreetype6-dev \  
libcurl3-dev \  
libxinerama1 \  
libxinerama-dev  
  
# Here is where we hardcode the toolchain decision.  
ENV HOST=arm-linux-gnueabihf \  
TOOLCHAIN=gcc-linaro-arm-linux-gnueabihf-raspbian-x64 \  
RPXC_ROOT=/rpxc  
  
# TOOLCHAIN=arm-rpi-4.9.3-linux-gnueabihf \  
# TOOLCHAIN=gcc-linaro-arm-linux-gnueabihf-raspbian-x64 \  
WORKDIR $RPXC_ROOT  
RUN curl -L https://github.com/raspberrypi/tools/tarball/master \  
| tar --wildcards --strip-components 3 -xzf - "*/arm-bcm2708/$TOOLCHAIN/"  
  
ENV ARCH=arm \  
CROSS_COMPILE=$RPXC_ROOT/bin/$HOST- \  
PATH=$RPXC_ROOT/bin:$PATH \  
QEMU_PATH=/usr/bin/qemu-arm-static \  
QEMU_EXECVE=1 \  
SYSROOT=$RPXC_ROOT/sysroot  
  
WORKDIR $SYSROOT  
RUN curl -Ls https://github.com/sdhibit/docker-rpi-
raspbian/raw/master/raspbian.2015.05.05.tar.xz \  
| tar -xJf - \  
&& curl -Ls https://github.com/resin-io-projects/armv7hf-debian-
qemu/raw/master/qemu-arm-static \  
> $SYSROOT/$QEMU_PATH \  
&& chmod +x $SYSROOT/$QEMU_PATH \  
&& mkdir -p $SYSROOT/build \  
&& chroot $SYSROOT $QEMU_PATH /bin/sh -c '\  
apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y apt-utils \  
&& DEBIAN_FRONTEND=noninteractive dpkg-reconfigure apt-utils \  
&& DEBIAN_FRONTEND=noninteractive apt-get upgrade -y \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
libc6-dev \  
symlinks \  
&& symlinks -cors /'  
  
COPY image/ /  
  
#/rpxc/bin/../lib/gcc/arm-linux-gnueabihf/4.8.3/../../../../arm-linux-
gnueabihf/bin/ld: cannot find -lasound  
#/rpxc/bin/../lib/gcc/arm-linux-gnueabihf/4.8.3/../../../../arm-linux-
gnueabihf/bin/ld: cannot find -lfreetype  
#/rpxc/bin/../lib/gcc/arm-linux-gnueabihf/4.8.3/../../../../arm-linux-
gnueabihf/bin/ld: cannot find -lcurl  
#/rpxc/bin/../lib/gcc/arm-linux-gnueabihf/4.8.3/../../../../arm-linux-
gnueabihf/bin/ld: cannot find -lX11  
#/rpxc/bin/../lib/gcc/arm-linux-gnueabihf/4.8.3/../../../../arm-linux-
gnueabihf/bin/ld: cannot find -lXext  
#/rpxc/bin/../lib/gcc/arm-linux-gnueabihf/4.8.3/../../../../arm-linux-
gnueabihf/bin/ld: cannot find -lXinerama  
#/rpxc/bin/../lib/gcc/arm-linux-gnueabihf/4.8.3/../../../../arm-linux-
gnueabihf/bin/ld: cannot find -lGL  
RUN rpdo DEBIAN_FRONTEND=noninteractive apt-get install -y \  
libfreetype6-dev \  
libxinerama-dev \  
libxrandr-dev \  
libxcursor-dev \  
libasound2-dev \  
freeglut3-dev \  
libcurl3-dev  
# libx11-dev \  
# mesa-common-dev \  
# libxcomposite-dev \  
# libxcursor-dev \  
COPY local/ /rpxc/local/  
RUN sudo ln -s /rpxc/local/lib/libwiringPi.so.2.36 /rpxc/lib/libwiringPi.so  
RUN sudo ln -s /rpxc/local/lib/libwiringPiDev.so.2.36
/rpxc/lib/libwiringPiDev.so  
  
WORKDIR /build  
ENTRYPOINT [ "/rpxc/entrypoint.sh" ]  

