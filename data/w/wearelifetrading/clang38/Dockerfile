FROM wearelifetrading/cpp:1.0  
  
MAINTAINER Life Trading <technology@lifetrading.com.au>  
  
# Install only the essential build tools  
RUN sudo apt-get update && \  
sudo apt-get install -y clang++-3.8  
# Build and install boost  
RUN cd /tmp/boost_1_61_0 && \  
echo "using clang : 3.8 : /usr/bin/clang++-3.8 ;" > tools/build/src/user-
config.jam && \  
sudo ./b2 link=static --layout=versioned toolset=clang-3.8
define=_GLIBCXX_USE_CXX11_ABI=0 \--without-python install  
  
# Build and install protobuf  
RUN cd /tmp/protobuf && \  
CXX=clang++-3.8 CC=clang-3.8 CXXFLAGS=-D_GLIBCXX_USE_CXX11_ABI=0 ./configure
--disable-shared && \  
make && \  
make check && \  
sudo make install && \  
sudo cp -p src/google/protobuf/compiler/csharp/csharp_helpers.h
/usr/local/include/google/protobuf/compiler/csharp && \  
sudo ln -s /usr/local/lib/libprotobuf.a /usr/local/lib/libprotobuf-clang38.a
&& \  
sudo ln -s /usr/local/lib/libprotoc.a /usr/local/lib/libprotoc-clang38.a  
# Clean up after ourselves to make the image smaller  
RUN sudo apt-get clean && \  
sudo rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

