FROM wearelifetrading/cpp:1.0  
MAINTAINER Life Trading <technology@lifetrading.com.au>  
  
# Build and install boost  
RUN cd /tmp/boost_1_61_0 && \  
echo "using gcc : 5.4 : /usr/bin/g++-5 ;" > tools/build/src/user-config.jam &&
\  
sudo ./b2 link=static --layout=versioned toolset=gcc-5.4 --without-python
install  
  
# Build and install protobuf  
RUN cd /tmp/protobuf && \  
./configure --disable-shared && \  
make && \  
make check && \  
sudo make install && \  
sudo cp -p src/google/protobuf/compiler/csharp/csharp_helpers.h
/usr/local/include/google/protobuf/compiler/csharp && \  
sudo ldconfig  
  
# Clean up after ourselves to make the image smaller  
RUN sudo apt-get clean && \  
sudo rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

