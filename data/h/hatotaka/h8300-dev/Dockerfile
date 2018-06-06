FROM ubuntu:xenial  
  
RUN mkdir -p /usr/local/src  
WORKDIR /usr/local/src  
  
RUN apt-get update \  
&& apt-get install -y make curl bzip2 gcc g++ m4 mpc  
  
ENV \  
BINUTILS_VERSION=2.26 \  
GMP_VERSION=6.1.0 \  
MPFR_VERSION=3.1.4 \  
MPC_VERSION=1.0.3 \  
GCC_VERSION=4.9.3  
RUN curl -O
http://ftp.gnu.org/gnu/binutils/binutils-${BINUTILS_VERSION}.tar.bz2 \  
&& curl -O http://ftp.gnu.org/gnu/gmp/gmp-${GMP_VERSION}.tar.bz2 \  
&& curl -O
http://www.multiprecision.org/mpc/download/mpc-${MPC_VERSION}.tar.gz \  
&& curl -O http://ftp.gnu.org/gnu/mpfr/mpfr-${MPFR_VERSION}.tar.gz \  
&& curl -O
http://ftp.gnu.org/gnu/gcc/gcc-${GCC_VERSION}/gcc-${GCC_VERSION}.tar.gz \  
&& cd /usr/local/src \  
&& tar jxvf binutils-${BINUTILS_VERSION}.tar.bz2 \  
&& cd binutils-${BINUTILS_VERSION} \  
&& ./configure --target=h8300-elf --disable-nls --disable-werror
prefix=/usr/local \  
&& make \  
&& make install \  
&& cd /usr/local/src \  
&& tar jxvf gmp-${GMP_VERSION}.tar.bz2 \  
&& cd gmp-${GMP_VERSION} \  
&& ./configure prefix=/usr/local \  
&& make \  
&& make install \  
&& cd /usr/local/src \  
&& tar zxvf mpfr-${MPFR_VERSION}.tar.gz \  
&& cd mpfr-${MPFR_VERSION} \  
&& ./configure prefix=/usr/local \--with-gmp=/usr/local \  
&& make \  
&& make install \  
&& cd /usr/local/src \  
&& tar zxvf mpc-${MPC_VERSION}.tar.gz \  
&& cd mpc-${MPC_VERSION} \  
&& ./configure --prefix=/usr/local \--with-gmp=/usr/local \--with-
mpfr=/usr/local \  
&& make \  
&& make install \  
&& cd /usr/local/src \  
&& tar zxvf gcc-${GCC_VERSION}.tar.gz \  
&& cd gcc-${GCC_VERSION} \  
&& mkdir h8300-elf \  
&& cd h8300-elf \  
&& ../configure --target=h8300-elf --disable-nls --disable-threads --disable-
shared --disable-werror --enable-languages=c --disable-libssp
--prefix=/usr/local \--with-gmp=/usr/local \--with-mpfr=/usr/local \--with-
mpc=/usr/local \  
&& make LANGUAGES=c \  
&& make install \  
&& rm -rf /usr/local/src/*  
  

