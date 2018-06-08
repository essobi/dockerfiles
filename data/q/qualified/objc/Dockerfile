FROM buildpack-deps:xenial  
# libobjc2 1.8.1  
# http://wiki.gnustep.org/index.php/GNUstep_under_Ubuntu_Linux  
  
RUN set -ex; \  
useradd --create-home codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
RUN set -ex; \  
apt-get update; \  
apt-get install -y --no-install-recommends \  
autoconf \  
clang \  
git \  
cmake \  
libtool \  
libffi-dev \  
libxml2-dev \  
libgnutls28-dev \  
libicu-dev \  
libffi-dev \  
# libdispatch deps  
libblocksruntime-dev \  
libpthread-workqueue-dev \  
libkqueue-dev \  
; \  
rm -rf /var/lib/apt/lists/*;  
  
RUN set -ex; \  
mkdir /tmp/GNUstep-build; \  
cd /tmp/GNUstep-build; \  
# Set clang as compiler  
export CC=clang; \  
export CXX=clang++; \  
# Checkout sources  
# The makefile package is a simple, powerful and extensible way to write
makefiles for a GNUstep-based project.  
mkdir tools-make; \  
wget -qO- https://github.com/gnustep/tools-make/archive/make-2_6_8.tar.gz |
tar xz -C tools-make --strip-components=1; \  
cd tools-make; \  
# Build GNUstep make first time  
./configure \  
\--enable-debug-by-default \  
\--with-layout=gnustep \  
\--enable-objc-nonfragile-abi \  
\--enable-objc-arc \  
; \  
make -j8; \  
make install; \  
. /usr/GNUstep/System/Library/Makefiles/GNUstep.sh; \  
\  
# Build libdispatch  
# Linux port of Apple's open-source concurrency library  
cd ../; \  
git clone https://github.com/nickhutchinson/libdispatch.git; \  
cd libdispatch; \  
git checkout bd1808980b04830cbbd79c959b8bc554085e38a1; \  
git clean -dfx; \  
mkdir build; \  
cd build; \  
../configure --prefix=/usr; \  
make; \  
make install; \  
ldconfig; \  
\  
# Build libobjc2  
cd ../../; \  
# Objective-C runtime library intended for use with Clang.  
mkdir libobjc2; \  
wget -qO- https://github.com/gnustep/libobjc2/archive/v1.8.1.tar.gz | tar xz
-C libobjc2 --strip-components=1; \  
cd libobjc2; \  
mkdir build; \  
cd build; \  
cmake ../ \  
-DCMAKE_C_COMPILER=clang \  
-DCMAKE_CXX_COMPILER=clang \  
-DCMAKE_ASM_COMPILER=clang \  
-DTESTS=OFF \  
; \  
cmake --build .; \  
make install; \  
ldconfig; \  
export LDFLAGS=-ldispatch; \  
OBJCFLAGS="-fblocks -fobjc-runtime=gnustep-1.8.1"; \  
\  
# Build GNUstep make second time  
cd ../..; \  
cd tools-make; \  
./configure \  
\--enable-debug-by-default \  
\--with-layout=gnustep \  
\--enable-objc-nonfragile-abi \  
\--enable-objc-arc \  
; \  
make -j8; \  
make install; \  
. /usr/GNUstep/System/Library/Makefiles/GNUstep.sh; \  
\  
# Build GNUstep base  
cd ..; \  
# The GNUstep Base Library is a library of general-purpose, non-graphical
Objective C objects.  
git clone https://github.com/gnustep/libs-base.git; \  
cd libs-base; \  
./configure; \  
make -j8; \  
make install; \  
. /usr/GNUstep/System/Library/Makefiles/GNUstep.sh; \  
\  
cd ..; \  
git clone https://github.com/etoile/UnitKit; \  
cd UnitKit; \  
git checkout b2133f3ef6e396de49e58bb01fa5c8380de30ca8; \  
git clean -dfx; \  
wget -q https://raw.githubusercontent.com/etoile/Etoile/master/etoile.make; \  
. /usr/GNUstep/System/Library/Makefiles/GNUstep.sh; \  
make; \  
make install; \  
make test=yes; \  
ukrun -q TestSource/TestUnitKit/TestUnitKit.bundle; \  
rm -rf /tmp/GNUstep-build;  
  
ENV CC=clang \  
CXX=clang++ \  
LDFLAGS=-ldispatch \  
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/GNUstep/Local/Library/Libraries:/usr/GNUstep/System/Library/Libraries
\  
OBJCFLAGS="-fblocks -fobjc-runtime=gnustep-1.8.1"  
  
WORKDIR /workspace  
  
COPY rootfs/usr /usr  
COPY rootfs/workspace /workspace  
RUN chown -R codewarrior:codewarrior /workspace/objc  
  
USER codewarrior  
ENV USER=codewarrior \  
HOME=/home/codewarrior  

