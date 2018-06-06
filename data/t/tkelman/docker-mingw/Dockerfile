FROM debian:stretch  
# LLVM has an undefined reference to SHGetKnownFolderPath when using  
# pre-4.0 mingw-w64-x86_64-dev, so jessie is too old  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
ca-certificates git build-essential mingw-w64 && \  
git clone https://github.com/flame/blis /home/blis  
WORKDIR /home/blis  
RUN git log -1 && \  
mkdir -p build32reference && \  
cd build32reference && \  
../configure reference && \  
make -j4 CC=i686-w64-mingw32-gcc AR=i686-w64-mingw32-ar \  
RANLIB=i686-w64-mingw32-ranlib CPICFLAGS="" BLIS_ENABLE_DYNAMIC_BUILD=yes && \  
for i in reference dunnington sandybridge haswell bulldozer piledriver
carrizo; do \  
mkdir -p ../build64$i && \  
cd ../build64$i && \  
../configure $i && \  
make -j4 CC=x86_64-w64-mingw32-gcc AR=x86_64-w64-mingw32-ar \  
RANLIB=x86_64-w64-mingw32-ranlib CPICFLAGS="" BLIS_ENABLE_DYNAMIC_BUILD=yes; \  
done  

