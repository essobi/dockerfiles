FROM ubuntu:16.04  
LABEL maintainer "Xin Zhang <xin.l.zhang@noaa.gov>"  
  
ARG FC=gfortran  
ARG CC=gcc  
ARG CXX=g++  
  
# install basic tools and openmpi  
RUN buildDeps='git libcurl4-openssl-dev autoconf automake gcc g++ make
gfortran libexpat1-dev wget vim file texinfo cmake csh ksh mlocate openssh-
server net-tools libmpc-dev gcc-multilib zip ca-certificates libncurses-dev
python-dev libssl-dev libxml2-dev flex bison pkg-config' \  
&& echo 'deb http://ppa.launchpad.net/george-edison55/cmake-3.x/ubuntu trusty
main' | tee -a /etc/apt/sources.list.d/cmake.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& rm -rf /var/lib/apt/lists/* \  
&& updatedb \  
&& cd /usr/local/src/ \  
&& wget --no-check-certificate
http://www.netgull.com/gcc/releases/gcc-6.3.0/gcc-6.3.0.tar.gz \  
&& tar xf gcc-6.3.0.tar.gz \  
&& rm gcc-6.3.0.tar.gz \  
&& cd gcc-6.3.0 \  
&& ./configure --prefix=/usr \  
&& make -j `nproc` \  
&& make install \  
&& cd /usr/local/src \  
&& rm -rf gcc-6.3.0  
ENV PATH=/usr/bin:/usr/local/bin:/bin:${PATH}  
ENV LD_LIBRARY_PATH=/usr/local/lib  
ENV NETCDF=/usr/local  
ENV PNETCDF=/usr/local  
ENV PIO=/usr/local  
ENV BOOST_ROOT=/usr/local  
ENV EIGEN3_INCLUDE_DIR=/usr/local  
ENV LAPACK_PATH=/usr/local  
ENV LAPACK_DIR=$LAPACK_PATH  
ENV LAPACK_LIBRARIES="$LAPACK_PATH/lib/liblapack.a;$LAPACK_PATH/lib/libblas.a"  
# build the common libraries for numerical weather prediction models  
WORKDIR /usr/local  
COPY CMake /usr/local/CMake  
COPY CMakeLists.txt /usr/local  
COPY nceplibs /usr/local/nceplibs  
RUN mkdir -p build \  
&& cd build \  
&& rm -fr * \  
&& cmake .. \  
&& make -j`nproc` \  
&& cd /usr/local \  
&& rm -fr CMake* build downloads \  
&& cd /usr/local/nceplibs \  
&& ./nceplibs.bash \  
&& cd /usr/local \  
&& rm -fr nceplibs  
  
CMD ["/bin/bash" , "-l"]  

