FROM ubuntu:16.04  
  
MAINTAINER Marc Reichelt <mcreichelt@gmail.com>  
  
RUN apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get install cmake wget build-essential libuv1-dev zlib1g-dev libssl-dev
git cppad gfortran -y && \  
apt-get clean autoclean && \  
apt-get autoremove -y  
  
RUN git clone https://github.com/uWebSockets/uWebSockets && \  
cd uWebSockets && \  
git checkout e94b6e1 && \  
mkdir build && \  
cd build && \  
cmake .. && \  
make -j4 && \  
make install && \  
cd ../.. && \  
ln -s /usr/lib64/libuWS.so /usr/lib/libuWS.so && \  
rm -r uWebSockets  
  
RUN wget https://www.coin-or.org/download/source/Ipopt/Ipopt-3.12.7.tgz && \  
tar xvfz Ipopt-3.12.7.tgz && \  
rm Ipopt-3.12.7.tgz && \  
cd Ipopt-3.12.7 && \  
  
# BLAS  
cd ThirdParty/Blas && \  
./get.Blas && \  
mkdir -p build && cd build && \  
../configure \--prefix=/usr/local \--disable-shared \--with-pic && \  
make install && \  
  
# Lapack  
cd ../../../ThirdParty/Lapack && \  
./get.Lapack && \  
mkdir -p build && cd build && \  
../configure \--prefix=/usr/local \--disable-shared \--with-pic \--with-
blas="/usr/local/lib/libcoinblas.a -lgfortran" && \  
make install && \  
  
# ASL  
cd ../../../ThirdParty/ASL && \  
./get.ASL && \  
  
# MUMPS  
cd ../../ThirdParty/Mumps && \  
./get.Mumps && \  
  
# build everything  
cd ../../ && \  
./configure \--prefix=/usr/local coin_skip_warn_cxxflags=yes \--with-
blas="/usr/local/lib/libcoinblas.a -lgfortran" \--with-
lapack=/usr/local/lib/libcoinlapack.a && \  
make && \  
make test && \  
make -j1 install && \  
  
cd .. && \  
rm -r Ipopt-3.12.7  
  
VOLUME "/project"  
WORKDIR "/project"  

