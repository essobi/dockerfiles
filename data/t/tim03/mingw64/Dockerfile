FROM tim03/gcc:6.3  
LABEL MAINTAINER Chen, Wenli <chenwenli@chenwenli.com>  
  
ENV PRJROOT=/opt/cross/w64 \  
TARGET=x86_64-w64-mingw32  
ENV PREFIX=${PRJROOT}/tools \  
BUILD=${PRJROOT}/build-tools  
ENV TARGET_PREFIX=${PREFIX}/${TARGET}  
ENV MAKEOPTS="-j4 -s"  
ENV PATH=${PATH}:${PREFIX}/bin  
  
COPY createdir.sh .  
  
RUN \  
/bin/bash createdir.sh && rm createdir.sh  
  
ENV BUILD_TOOLS="lzip"  
  
RUN apt-get -qq update && apt-get -qqy install --no-install-recommends \  
$BUILD_TOOLS \  
&& apt-get -y autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& cd $BUILD \  
&& curl -L http://ftp.gnu.org/gnu/binutils/binutils-2.27.tar.gz | tar zxf - \  
&& cd build-binutils \  
&& ../binutils-2.27/configure --disable-multilib --target=$TARGET
--prefix=$PREFIX --with-sysroot=${PREFIX} \  
&& make \  
&& make install \  
&& cd $BUILD \  
&& rm -rf build-binutils binutils-2.27 \  
# mingw headers  
&& curl -L
http://downloads.sourceforge.net/project/mingw-w64/mingw-w64/mingw-w64-release/mingw-w64-v5.0.2.tar.bz2
| tar jxf - \  
&& mkdir -p $BUILD/build-mingw-w64-header/ \  
&& cd $BUILD/build-mingw-w64-header/ \  
&& ../mingw-w64-v5.0.2/configure --host=${TARGET} --prefix=${TARGET_PREFIX}
--with-sysroot=${TARGET_PREFIX} --without-crt \  
&& make \  
&& make install \  
&& cd $BUILD \  
&& rm -rf build-mingw-w64-header \  
# gcc phase 1  
&& curl -L
http://ftp.tsukuba.wide.ad.jp/software/gcc/releases/gcc-6.3.0/gcc-6.3.0.tar.bz2
| tar jxf - \  
&& ln -s $TARGET_PREFIX $PREFIX/mingw \  
&& mkdir -p $TARGET_PREFIX/lib \  
&& ln -s $TARGET_PREFIX/lib $TARGET_PREFIX/lib64 \  
# gmp  
&& curl -L https://gmplib.org/download/gmp/gmp-6.1.2.tar.lz | tar --lzip -xf -
\  
&& mv gmp-6.1.2 gcc-6.3.0/gmp \  
# mpc  
&& curl -L ftp://ftp.gnu.org/gnu/mpc/mpc-1.0.3.tar.gz | tar zxf - \  
&& mv mpc-1.0.3 gcc-6.3.0/mpc \  
# mpfr  
&& curl -L http://www.mpfr.org/mpfr-current/mpfr-3.1.5.tar.bz2 | tar jxf - \  
&& mv mpfr-3.1.5 gcc-6.3.0/mpfr \  
&& cd $BUILD/build-gcc \  
&& ../gcc-6.3.0/configure --disable-multilib --disable-bootstrap
--target=$TARGET --prefix=$PREFIX --with-sysroot=${PREFIX} --enable-
languages=c,c++ \  
&& make all-gcc \  
&& make install-gcc \  
# mingw CRT  
&& mkdir -p $BUILD/build-mingw-w64-crt/ \  
&& cd $BUILD/build-mingw-w64-crt/ \  
&& ../mingw-w64-v5.0.2/configure --host=$TARGET --prefix=$TARGET_PREFIX
--without-header --with-sysroot=${TARGET_PREFIX} \  
&& make \  
&& make install \  
&& cd $BUILD \  
&& rm -rf build-mingw-w64-crt mingw-w64-v5.0.2 \  
# gcc phase 2  
&& cd $BUILD/build-gcc \  
&& make all \  
&& make install \  
&& cd $BUILD \  
&& rm -rf build-gcc gcc-6.3.0  
  
RUN adduser -q docker  
USER docker  
  
CMD ["/bin/bash"]  

