FROM ubuntu:16.04  
  
MAINTAINER Simon Spoorendonk  
  
# install dependencies  
RUN \  
apt-get update && \  
apt-get install -y \  
wget gfortran subversion mingw-w64 make patch g++ && \  
# install cbc  
wget https://github.com/coin-or/Cbc/archive/releases/2.9.8.tar.gz && \  
tar -xzf 2.9.8.tar.gz && \  
rm 2.9.8.tar.gz && \  
cd Cbc-releases-2.9.8 && \  
wget https://github.com/coin-or-tools/BuildTools/archive/releases/0.8.6.tar.gz
&& \  
tar -xzf 0.8.6.tar.gz && \  
rm 0.8.6.tar.gz && \  
chmod +x BuildTools-releases-0.8.6/get.dependencies.sh && \  
BuildTools-releases-0.8.6/get.dependencies.sh fetch && \  
./configure && \  
make && \  
make install && \  
# remove dependencies  
apt-get remove -y \  
wget subversion mingw-w64 make patch g++ \  
binutils gfortran binutils-mingw-w64-i686 binutils-mingw-w64-x86-64 ca-
certificates \  
cpp cpp-5 g++ g++-5 g++-mingw-w64 g++-mingw-w64-i686 g++-mingw-w64-x86-64 \  
gcc gcc-5 gcc-mingw-w64 gcc-mingw-w64-base gcc-mingw-w64-i686 \  
gcc-mingw-w64-x86-64 gfortran gfortran-5 gfortran-mingw-w64 \  
gfortran-mingw-w64-i686 gfortran-mingw-w64-x86-64 gnat-mingw-w64 \  
gnat-mingw-w64-base gnat-mingw-w64-i686 gnat-mingw-w64-x86-64 krb5-locales \  
libapr1 libaprutil1 libasan2 libatomic1 libc-dev-bin libc6-dev libcc1-0 \  
libcilkrts5 libexpat1 libgcc-5-dev libgfortran-5-dev libgmp10 \  
libgomp1 libgssapi-krb5-2 libidn11 libisl15 libitm1 libk5crypto3 \  
libkeyutils1 libkrb5-3 libkrb5support0 liblsan0 libmpc3 libmpfr4 libmpx0 \  
libsasl2-2 libsasl2-modules libsasl2-modules-db libserf-1-1 \  
libsqlite3-0 libssl1.0.0 libstdc++-5-dev libsvn1 libtsan0 libubsan0 \  
linux-libc-dev make manpages manpages-dev mingw-w64 mingw-w64-common \  
mingw-w64-i686-dev mingw-w64-x86-64-dev openssl patch subversion wget && \  
apt-get install -y libgfortran3 && \  
apt autoremove -y && \  
rm -rf /var/lib/apt/lists/* && \  
# copy executable  
cp /Cbc-releases-2.9.8/bin/* /usr/local/bin && \  
# remove source code  
find /Cbc-releases-2.9.8/* -type d -not -name lib -exec rm -rf {} + && \  
find /Cbc-releases-2.9.8/* -type f -maxdepth 0 -exec rm -rf {} +  
  
# copy example problem  
COPY hello.mps hello.mps

