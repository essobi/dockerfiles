FROM ubuntu:latest  
  
ENV BINUTILS_VERSION binutils-2.27  
ENV GCC_VERSION gcc-6.3.0  
ENV ISL_VERSION isl-0.16.1  
ENV CLOOG_VERSION cloog-0.18.1  
ENV NEWLIB_VERSION newlib-2.4.0  
ENV PREFIX /opt/m68k/$GCC_VERSION  
ENV TARGET m68k-elf  
ENV ENABLE_LANGUAGES c,c++  
  
RUN apt-get update && apt-get install -y wget unzip build-essential gcc-5
libgmp-dev libmpfr-dev libmpc-dev  
  
RUN mkdir /tmp/downloads && cd /tmp/downloads \  
&& wget http://ftp.gnu.org/pub/gnu/binutils/$BINUTILS_VERSION.tar.bz2 \  
&& wget http://ftp.gnu.org/pub/gnu/gcc/$GCC_VERSION/$GCC_VERSION.tar.bz2 \  
&& wget ftp://gcc.gnu.org/pub/gcc/infrastructure/$ISL_VERSION.tar.bz2 \  
&& wget ftp://gcc.gnu.org/pub/gcc/infrastructure/$CLOOG_VERSION.tar.gz \  
&& wget ftp://sourceware.org/pub/newlib/$NEWLIB_VERSION.tar.gz \  
&& mkdir /tmp/build && cd /tmp/build \  
&& tar jxvf ../downloads/$BINUTILS_VERSION.tar.bz2 \  
&& tar jxvf ../downloads/$GCC_VERSION.tar.bz2 \  
&& tar jxvf ../downloads/$ISL_VERSION.tar.bz2 \  
&& tar zxvf ../downloads/$CLOOG_VERSION.tar.gz \  
&& tar zvxf ../downloads/$NEWLIB_VERSION.tar.gz \  
&& rm -v /tmp/downloads/* \  
&& mv $ISL_VERSION ./$GCC_VERSION/isl \  
&& mv $CLOOG_VERSION ./$GCC_VERSION/cloog \  
&& mv $NEWLIB_VERSION/libgloss/m68k/io-read.c
$NEWLIB_VERSION/libgloss/m68k/io-read.bak \  
&& sed -e 's/ssize_t/_READ_WRITE_RETURN_TYPE/g'
$NEWLIB_VERSION/libgloss/m68k/io-read.bak > $NEWLIB_VERSION/libgloss/m68k/io-
read.c \  
&& rm $NEWLIB_VERSION/libgloss/m68k/io-read.bak \  
&& mv $NEWLIB_VERSION/libgloss/m68k/io-write.c
$NEWLIB_VERSION/libgloss/m68k/io-write.bak \  
&& sed -e 's/ssize_t/_READ_WRITE_RETURN_TYPE/g'
$NEWLIB_VERSION/libgloss/m68k/io-write.bak > $NEWLIB_VERSION/libgloss/m68k/io-
write.c \  
&& rm $NEWLIB_VERSION/libgloss/m68k/io-write.bak  
  
RUN mkdir /tmp/build/binutils-obj && cd /tmp/build/binutils-obj \  
&& ../$BINUTILS_VERSION/configure --prefix=$PREFIX \--target=$TARGET \  
&& make \  
&& make install  
  
RUN mkdir /tmp/build/gcc-obj && cd /tmp/build/gcc-obj \  
&& ../$GCC_VERSION/configure --prefix=$PREFIX \--target=$TARGET \--enable-
languages=$ENABLE_LANGUAGES \--with-newlib --disable-libmudflap --disable-
libssp --disable-libgomp --disable-libstdcxx-pch --disable-threads --disable-
nls --disable-libquadmath --with-gnu-as --with-gnu-ld --without-headers \  
&& make all-gcc \  
&& make install-gcc  
  
ENV PATH=$PATH:$PREFIX/bin  
  
RUN mkdir /tmp/build/newlib-obj && cd /tmp/build/newlib-obj \  
&& ../$NEWLIB_VERSION/configure --prefix=$PREFIX \--target=$TARGET \--disable-
newlib-multithread --disable-newlib-io-float --enable-lite-exit --disable-
newlib-supplied-syscalls \  
&& make \  
&& make install  
  
RUN cd /tmp/build/gcc-obj \  
&& make all-target-libgcc all-target-libstdc++-v3 \  
&& make install-target-libgcc install-target-libstdc++-v3  

