FROM ubuntu:16.04 AS build  
EXPOSE 4567  
CMD bash  
  
VOLUME /repo  
VOLUME /build  
WORKDIR /build  
  
RUN apt-get update && apt-get install --no-install-recommends -y \  
ca-certificates \  
cmake \  
cmake-data \  
cppad \  
curl \  
g++ \  
gcc \  
gdb \  
git \  
gfortran \  
libssl-dev \  
libtool-bin \  
libuv1-dev \  
m4 \  
make \  
ninja-build \  
patch \  
pkg-config \  
wget \  
zlib1g-dev && \  
apt-get clean  
  
ENV UWS_URL="https://github.com/uWebSockets/uWebSockets.git"  
ENV UWS_TAG="v0.13.0"  
RUN ln -s /usr/lib /usr/lib64 && \  
git clone ${UWS_URL} && \  
cd uWebSockets && \  
git checkout ${UWS_TAG} && \  
cmake . -DCMAKE_BUILD_TYPE=Release && \  
make -j && \  
make install && \  
cd .. && \  
rm -rf uWebSockets && \  
chmod 755 /usr/lib/libuWS.so  
  
ENV IPOPT_VERSION="3.12.8"  
ENV IPOPT_URL="https://www.coin-
or.org/download/source/Ipopt/Ipopt-${IPOPT_VERSION}.tgz"  
RUN wget ${IPOPT_URL} && \  
mkdir ipopt && \  
mkdir -p /usr/local/opt/ipopt && \  
tar -zxf $(basename ${IPOPT_URL}) -C ipopt --strip-components=1 && \  
rm $(basename ${IPOPT_URL}) && \  
cd ipopt && \  
find ThirdParty -name "get.*" -printf "cd $(pwd)/%h && ./%f && cd ..\n" | sh
&& \  
./configure --with-pic --prefix=/usr/local/opt/ipopt && \  
make -j && \  
make -j test && \  
make install && \  
cd .. && \  
rm -rf ipopt  
  
ENV PKG_CONFIG_PATH="/usr/local/opt/ipopt/lib/pkgconfig:${PKG_CONFIG_PATH}"  
ENV LD_LIBRARY_PATH="/usr/local/opt/ipopt/lib:${LD_LIBRARY_PATH}"  
### Custom CppAd build  
#ENV CPPAD_VERSION="20170000.8"  
#ENV CPPAD_URL="https://www.coin-
or.org/download/source/CppAD/cppad-${CPPAD_VERSION}.epl.tgz"  
#RUN wget ${CPPAD_URL} && \  
# mkdir cppad && \  
# mkdir -p /usr/local/opt/cppad && \  
# tar -zxf $(basename ${CPPAD_URL}) -C cppad --strip-components=1 && \  
# rm $(basename ${CPPAD_URL}) && \  
# cd cppad && \  
# CPPFLAGS="${CPPFLAGS} $(pkg-config ipopt --cflags-only-I) -I$(pkg-config
ipopt --variable=prefix)/include" \  
# LDFLAGS="${LDFLAGS} $(pkg-config ipopt --libs-only-L)" \  
# ./configure --prefix=/usr/local/opt/cppad && \  
# make -j && \  
# make install && \  
# cd .. && \  
# rm -rf cppad  
#ENV PKG_CONFIG_PATH="${PKG_CONFIG_PATH}:/usr/local/opt/cppad/share/pkgconfig"  
#ENV CPPFLAGS="${CPPFLAGS} -I/usr/local/opt/cppad/include"  
ENV BENCHMARK_URL="https://github.com/google/benchmark.git"  
RUN git clone ${BENCHMARK_URL} && \  
cd benchmark && \  
cmake . -DCMAKE_BUILD_TYPE=Release -DBENCHMARK_DOWNLOAD_DEPENDENCIES=ON && \  
make -j && \  
make install && \  
cd .. && \  
rm -rf benchmark  

