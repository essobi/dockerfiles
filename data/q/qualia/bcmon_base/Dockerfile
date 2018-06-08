# BUILD-USING: docker build -t qualia/bcmon_base .  
FROM ubuntu:12.04  
MAINTAINER Drew Carey Buglione <me@drewb.ug>  
WORKDIR root  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -y  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y subversion patch  
  
RUN svn checkout -r 13 http://bcmon.googlecode.com/svn/trunk/ bcmon  
  
ADD dhd_linux.c.patch.r13
/root/bcmon/bcm4329/driver/src/bcm4329/dhd_linux.c.patch.r13  
RUN patch bcmon/bcm4329/driver/src/bcm4329/dhd_linux.c
bcmon/bcm4329/driver/src/bcm4329/dhd_linux.c.patch.r13  
  
ADD dhd_custom_gpio.c.patch.r13
/root/bcmon/bcm4329/driver/src/bcm4329/dhd_custom_gpio.c.patch.r13  
RUN patch bcmon/bcm4329/driver/src/bcm4329/dhd_custom_gpio.c
bcmon/bcm4329/driver/src/bcm4329/dhd_custom_gpio.c.patch.r13  
  
RUN echo "EXTRA_CFLAGS += -Wno-error=array-bounds" >>
bcmon/bcm4329/driver/src/bcm4329/Makefile  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget bzip2  
  
RUN wget https://sourcery.mentor.com/GNUToolchain/package11447/public/arm-
none-linux-gnueabi/arm-2013.05-24-arm-none-linux-gnueabi-i686-pc-linux-
gnu.tar.bz2 && \  
tar xvfj arm-2013.05-24-arm-none-linux-gnueabi-i686-pc-linux-gnu.tar.bz2 && \  
mv arm-2013.05 toolchain && \  
rm arm-2013.05-24-arm-none-linux-gnueabi-i686-pc-linux-gnu.tar.bz2  
ENV PATH /root/toolchain/bin:$PATH  
  
ENV ARCH arm  
ENV CROSS_COMPILE arm-none-linux-gnueabi-  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python  
  
ADD extract-symvers.py /root/extract-symvers.py  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y bison build-essential
cpio curl flex g++-multilib gcc-multilib git git-core gnupg gperf
lib32ncurses5-dev lib32readline-gplv2-dev lib32z-dev libc6-dev libc6-dev-i386
libncurses5-dev libreadline-gplv2-dev lzma squashfs-tools unzip xz-utils zip
zlib1g-dev  

