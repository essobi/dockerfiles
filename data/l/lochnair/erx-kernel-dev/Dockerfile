FROM debian:wheezy-slim  
  
LABEL Description="Kernel build environment for the EdgeRouter X"  
LABEL Maintainer="Nils Andreas Svee <me@lochnair.net>"  
  
COPY root/ /  
  
ENV PATH "/opt/cross/bin:$PATH"  
ENV TARGET "mipsel-linux-gnu"  
  
RUN \  
apt-get update && \  
apt-get install -y bison \  
build-essential \  
curl \  
dpkg-dev \  
file \  
flex \  
g++ \  
gawk \  
libmpfr-dev \  
make && \  
cd /usr/src && \  
apt-get source binutils \  
gcc-4.7-source \  
libgmp10 \  
libmpc2 \  
libmpfr4 && \  
tar -xf gcc-4.7-4.7.2/gcc-4.7.2-dfsg.tar.xz && \  
# Compile and install binutils  
mkdir binutils-build && cd binutils-build && \  
../binutils-2.22/configure --prefix=/opt/cross --target=$TARGET --disable-
multilib --disable-werror && \  
make -j$(nproc) && \  
make install && \  
cd .. && \  
# First stage GCC  
cd gcc-4.7.2 && \  
ln -s ../gmp-5.0.5+dfsg gmp && \  
ln -s ../mpclib-0.9 mpc && \  
ln -s ../mpfr4-3.1.0 mpfr && \  
cd .. && \  
mkdir gcc-build && cd gcc-build && \  
../gcc-4.7.2/configure --prefix=/opt/cross --target=$TARGET --enable-
languages=c --disable-multilib && \  
make -j$(nproc) all-gcc && \  
curl -s -L
"http://dev.debwrt.net/export/935/trunk/arch/octeon/erlite/patches/gcc-
install.patch" | patch -p0 && \  
make install-gcc && \  
cd .. && \  
# Cleanup  
rm -rf /usr/src/* /tmp/* /var/lib/apt/lists/* && \  
apt-get -y remove dpkg-dev && \  
apt-get -y autoremove  
  
# Make sure /entrypoint.sh is executable  
RUN chmod +x /entrypoint.sh  
  
# Add unprivileged user  
RUN useradd -m -U -s /bin/sh -u 1234 user  
  
# Install su-exec  
RUN \  
curl -L -o /tmp/su-exec.c "https://raw.githubusercontent.com/ncopa/su-
exec/master/su-exec.c" && \  
gcc /tmp/su-exec.c -o /sbin/su-exec && \  
rm /tmp/su-exec.c  
  
ENTRYPOINT ["/entrypoint.sh"]  

