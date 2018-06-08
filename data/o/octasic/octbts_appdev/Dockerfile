FROM ubuntu:14.04  
RUN apt-get -y update && apt-get -y install apt-transport-https  
  
RUN echo deb http://debian.pengutronix.de/debian/ jessie main contrib non-free
> /etc/apt/sources.list.d/pengutronix.list  
  
RUN apt-get -y update && apt-get install --allow-unauthenticated -y
pengutronix-archive-keyring && apt-get -y update && \  
apt-get install -y curl wget make file libpython2.7 \  
oselas.toolchain-2011.11.3-arm-cortexa9-linux-gnueabi-
gcc-4.6.2-glibc-2.14.1-binutils-2.21.1a-kernel-2.6.39-sanitized  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME [ "/ptx_sysroot" ]  
VOLUME [ "/src" ]  
WORKDIR "/src"  
  
ENV CC="/opt/OSELAS.Toolchain-2011.11.3/arm-cortexa9-linux-
gnueabi/gcc-4.6.2-glibc-2.14.1-binutils-2.21.1a-kernel-2.6.39-sanitized/bin/arm-
cortexa9-linux-gnueabi-ar"  
ENV CC="/opt/OSELAS.Toolchain-2011.11.3/arm-cortexa9-linux-
gnueabi/gcc-4.6.2-glibc-2.14.1-binutils-2.21.1a-kernel-2.6.39-sanitized/bin/arm-
cortexa9-linux-gnueabi-gcc"  
ENV CXX="/opt/OSELAS.Toolchain-2011.11.3/arm-cortexa9-linux-
gnueabi/gcc-4.6.2-glibc-2.14.1-binutils-2.21.1a-kernel-2.6.39-sanitized/bin/arm-
cortexa9-linux-gnueabi-g++"  
ENV GDB="/opt/OSELAS.Toolchain-2011.11.3/arm-cortexa9-linux-
gnueabi/gcc-4.6.2-glibc-2.14.1-binutils-2.21.1a-kernel-2.6.39-sanitized/bin/arm-
cortexa9-linux-gnueabi-gdb"  
ENV CPPFLAGS="-Wall -isystem /ptx_sysroot/include -isystem
/ptx_sysroot/usr/include"  
ENV LDFLAGS="-L/ptx_sysroot/lib -L/ptx_sysroot/usr/lib"  
CMD ["/bin/bash", "--login"]  

