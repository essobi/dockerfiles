# Uses the Debian cross compiler to build a native mingw-w64 gcc for:  
#  
# - Host: win32  
# - Target: multilib (win32 and win64)  
# - Threading model: win32  
# - Exception model: sjlj  
#  
# Based on:
http://sourceforge.net/p/mingw-w64/wiki2/Native%20Win64%20compiler/  
#  
# Cross compiling notes:  
# - The minor version of gcc must match that of our cross compiler (4.9 in
this case)  
# - Important parameters: http://gcc.gnu.org/onlinedocs/gccint/Configure-
Terms.html  
FROM debian:jessie  
  
RUN \  
useradd -ms /bin/bash builder && \  
apt-get update && \  
apt-get -y dist-upgrade && \  
apt-get install -y wget make bzip2 gcc g++ texinfo m4 zip \  
mingw-w64  
  
RUN \  
chmod 777 /usr/local/include  
  
USER builder  
  
ENV HOST i686-w64-mingw32  
ENV BUILD x86_64-w64-mingw32  
ENV TARGET i686-w64-mingw32  
ENV THREADS win32  
ENV BUILDROOT /home/builder/mingw  
ENV SRC $BUILDROOT/sources  
ENV DEST $BUILDROOT/dest  
ENV PREFIX $DEST/$TARGET  
  
RUN \  
mkdir -p $SRC && \  
mkdir -p $DEST  
  
RUN \  
cd $SRC && \  
wget -nv ftp://gcc.gnu.org/pub/gcc/infrastructure/mpc-0.8.1.tar.gz && \  
tar xzf mpc-0.8.1.tar.gz && \  
wget -nv ftp://gcc.gnu.org/pub/gcc/infrastructure/mpfr-2.4.2.tar.bz2 && \  
tar xjf mpfr-2.4.2.tar.bz2 && \  
wget -nv http://isl.gforge.inria.fr/isl-0.12.2.tar.bz2 && \  
tar xjf isl-0.12.2.tar.bz2 && \  
wget -nv http://gmplib.org/download/gmp/gmp-4.3.2.tar.bz2 && \  
tar xjf gmp-4.3.2.tar.bz2 && \  
wget -nv http://ftp.gnu.org/gnu/binutils/binutils-2.25.tar.bz2 && \  
tar xjf binutils-2.25.tar.bz2 && \  
wget -nv
http://downloads.sourceforge.net/project/mingw-w64/mingw-w64/mingw-w64-release/mingw-w64-v4.0.2.tar.bz2
&& \  
tar xjf mingw-w64-v4.0.2.tar.bz2 && \  
wget -nv http://ftp.gnu.org/gnu/gcc/gcc-4.9.2/gcc-4.9.2.tar.bz2 && \  
tar xjf gcc-4.9.2.tar.bz2 && \  
wget -nv ftp://gcc.gnu.org/pub/gcc/infrastructure/cloog-0.18.1.tar.gz &&\  
tar xzf cloog-0.18.1.tar.gz  
  
RUN \  
mkdir -p $BUILDROOT/binutils && \  
cd $BUILDROOT/binutils && \  
$SRC/binutils-2.25/configure --prefix=$DEST \--with-sysroot=$DEST
\--host=$HOST \--target=$TARGET \--enable-
targets=i686-w64-mingw32,x86_64-w64-mingw32 && \  
make && \  
make install  
  
RUN \  
mkdir -p $SRC/gcc-4.9.2/gcc/winsup/mingw && \  
ln -s /usr/i686-w64-mingw32/include $SRC/gcc-4.9.2/gcc/winsup/mingw/include  
  
RUN \  
mkdir -p $BUILDROOT/headers && \  
cd $BUILDROOT/headers && \  
$SRC/mingw-w64-v4.0.2/mingw-w64-headers/configure --prefix=$PREFIX
\--host=$HOST \--build=$BUILD && \  
make && \  
make install  
  
RUN \  
ln -s $PREFIX $DEST/mingw && \  
ln -s $PREFIX/lib $PREFIX/lib32  
  
RUN \  
mkdir -p $BUILDROOT/gmp && \  
cd $BUILDROOT/gmp && \  
$SRC/gmp-4.3.2/configure --host=$HOST \--build=$BUILD \--prefix=$PREFIX
\--disable-shared --enable-static --enable-cxx && \  
make && \  
make install  
  
RUN \  
mkdir -p $BUILDROOT/isl && \  
cd $BUILDROOT/isl && \  
CPPFLAGS=-I$PREFIX/include LDFLAGS=-L$PREFIX/lib $SRC/isl-0.12.2/configure
--host=$HOST \--build=$BUILD \--prefix=$PREFIX \--disable-shared --enable-
static --with-gmp-prefix=$BUILDROOT && \  
make && \  
make install  
  
RUN \  
mkdir -p $BUILDROOT/mpfr && \  
cd $BUILDROOT/mpfr && \  
CPPFLAGS="-I$SRC/gcc-4.9.2/gcc/ginclude -I$PREFIX/include"
LDFLAGS="-L$PREFIX/lib" $SRC/mpfr-2.4.2/configure --host=$HOST \--build=$BUILD
\--prefix=$PREFIX \--disable-shared --enable-static --with-gmp=$BUILDROOT && \  
make && \  
make install  
  
RUN \  
mkdir -p $BUILDROOT/mpc && \  
cd $BUILDROOT/mpc && \  
CPPFLAGS="-I$PREFIX/include" LDFLAGS="-L$PREFIX/lib" $SRC/mpc-0.8.1/configure
--host=$HOST \--build=$BUILD \--prefix=$PREFIX \--disable-shared --enable-
static --with-gmp=$BUILDROOT \--with-mpfr=$BUILDROOT && \  
make && \  
make install  
  
RUN \  
mkdir -p $BUILDROOT/cloog && \  
cd $BUILDROOT/cloog && \  
CPPFLAGS="-I$PREFIX/include" LDFLAGS="-L$PREFIX/lib"
$SRC/cloog-0.18.1/configure --host=$HOST \--build=$BUILD \--prefix=$PREFIX
\--with-gmp=$BUILDROOT \--with-isl=$BUILDROOT \--disable-shared --enable-
static --prefix=$PREFIX \--enable-targets=i686-w64-mingw32,x86_64-w64-mingw32
&& \  
make && \  
make install  
  
RUN \  
mkdir -p $BUILDROOT/gcc && \  
cd $BUILDROOT/gcc && \  
mkdir -p gcc && ln -sf auto-host.h gcc/auto-build.h && \  
$SRC/gcc-4.9.2/configure --build=$BUILD \--host=$HOST \--target=$TARGET \  
\--prefix=$PREFIX \--with-sysroot=$DEST \--enable-
targets=i686-w64-mingw32,x86_64-w64-mingw32 --enable-languages=c,c++,fortran \  
\--with-gmp=$PREFIX \--with-mpfr=$PREFIX \--with-mpc=$PREFIX \--with-
cloog=$PREFIX \  
\--disable-shared --enable-static --enable-plugins --enable-cloog-backend=isl
\  
\--enable-sjlj-exceptions --disable-dw2-exceptions --disable-seh-exceptions
--enable-threads=$THREADS \  
\--enable-libgomp --disable-libstdcxx-pch --enable-fully-dynamic-string
--enable-libstdcxx-time \  
\--disable-nls --disable-werror --enable-checking=release \  
\--with-gnu-as --with-gnu-ld && \  
make maybe-all-libiberty && \  
mkdir -p build-$BUILD/libiberty && cp libiberty/pex-win32.o
build-$BUILD/libiberty && touch -t 12312359 build-$BUILD/libiberty/pex-win32.o
&& \  
make && \  
make install  
  
RUN \  
mkdir -p $BUILDROOT/mingw32 && \  
cd $BUILDROOT/mingw32 && \  
CPPFLAGS="-I$PREFIX/include" LDFLAGS="-L$PREFIX/lib"
$SRC/mingw-w64-v4.0.2/configure --host=i686-w64-mingw32 --prefix=$PREFIX
\--enable-lib32 && \  
make && \  
make install  
  
RUN \  
mkdir -p $BUILDROOT/mingw64 && \  
cd $BUILDROOT/mingw64 && \  
CPPFLAGS="-I$PREFIX/include" LDFLAGS="-L$PREFIX/lib"
$SRC/mingw-w64-v4.0.2/configure --host=x86_64-w64-mingw32 --prefix=$PREFIX
\--enable-lib64 && \  
make && \  
make install  
  
RUN \  
cd $DEST && \  
zip --symlinks -r $TARGET-multi.zip . && \  
mv $TARGET-multi.zip ~  

