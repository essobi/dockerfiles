FROM debian:jessie-slim  
LABEL Maintainer="Rob Egan<RSEgan@lbl.gov"  
  
WORKDIR /tmp/build  
  
# This is necessary because the upgrade sometimes prompts for input  
ENV DEBIAN_FRONTEND=noninteractive  
  
ARG CUPCVER=3.8.1-0  
ENV CUPCTAR=clang-upc-all-$CUPCVER.tar.gz  
ENV CUPCURL=https://github.com/Intrepid/clang-upc/releases/download/clang-
upc-$CUPCVER/$CUPCTAR  
ENV CUPCDIR=clang-upc-$CUPCVER  
  
ARG BUPCVER=2.24.2  
ENV BUPCDIR=berkeley_upc-$BUPCVER  
ENV BUPCTAR=$BUPCDIR.tar.gz  
ENV BUPCURL=http://upc.lbl.gov/download/release/$BUPCTAR  
  
RUN apt-get update && \  
apt-get install -y wget openmpi-bin libopenmpi-dev openssh-server build-
essential perl cmake python && \  
wget -O $CUPCTAR $CUPCURL && \  
wget -O $BUPCTAR $BUPCURL && \  
tar -xzf $CUPCTAR && \  
mkdir -p build_clangupc && \  
cd build_clangupc && \  
cmake ../$CUPCDIR -DCMAKE_INSTALL_PREFIX:PATH=/usr/local
-DLLVM_TARGETS_TO_BUILD:=host -DCMAKE_BUILD_TYPE:=Release && \  
make -j 32 && \  
make install && \  
cd \- && \  
tar -xvzf $BUPCTAR && \  
mkdir build-bupc && \  
cd build-bupc && \  
../$BUPCDIR/configure MPI_CC=mpicc CUPC2C_TRANS=/usr/local/bin/clang-upc2c
--prefix=/usr/local \  
\--disable-dependency-tracking --disable-ibv \  
\--with-multiconf=+opt_cupc2c --enable-pshm --enable-pthreads --enable-udp
--enable-mpi --enable-smp --disable-ibv --with-default-network=mpi \  
\--enable-sptr-struct --disable-sptr-struct --with-sptr-packed-bits=10,18,36
&& \  
make -j 31 && \  
make install && \  
cd \- && \  
apt-get purge -y wget && \  
apt-get autoremove -y && \  
apt-get clean && \  
apt-get autoclean && \  
rm -rf /tmp/build/* \  
/var/lib/apt/lists/* && \  
find / -name '*.pyc' -exec rm {} \;  
  
CMD ["/bin/bash"]  
  

