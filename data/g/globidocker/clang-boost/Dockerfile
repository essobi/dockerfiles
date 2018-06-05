FROM debian:jessie  
  
RUN apt-get update -y && apt-get install -y curl xz-utils build-essential &&\  
mkdir /tmp/clang-binaries &&\  
curl -L "http://releases.llvm.org/5.0.0/clang+llvm-5.0.0-x86_64-linux-gnu-
debian8.tar.xz" | tar xJ \  
\--strip-components=1 \  
-C /tmp/clang-binaries &&\  
cd /tmp/clang-binaries && cp -r * /usr/local/ && rm -rf /tmp/clang-binaries
&&\  
mkdir /tmp/boost-build &&\  
curl -L
"http://dl.bintray.com/boostorg/release/1.65.0/source/boost_1_65_0.tar.bz2" |
tar xj \  
\--strip-components=1 \  
-C /tmp/boost-build &&\  
cd /tmp/boost-build &&\  
./bootstrap.sh \  
\--with-toolset=clang \  
\--without-libraries=python &&\  
./b2 \  
-j$(nproc) \  
toolset=clang \  
cxxflags="-std=c++17 -stdlib=libc++ -D _LIBCPP_ENABLE_CXX17_REMOVED_FEATURES"
\  
linkflags="-stdlib=libc++ -lc++" \  
install > boost.build &&\  
rm -rf /tmp/boost-build  

