FROM debian  
MAINTAINER thouveng  
  
ENV BUILDPATH /tmp/build  
  
RUN mkdir $BUILDPATH  
  
RUN apt-get update && \  
apt-get install -y build-essential wget git  
  
# We need to build and install CMake because version 3.5+ is required  
# for LUA Sandbox extensions  
RUN cd $BUILDPATH; \  
wget https://cmake.org/files/v3.7/cmake-3.7.1.tar.gz && \  
tar xf cmake-3.7.1.tar.gz && \  
cd cmake-3.7.1 && \  
./bootstrap && make && make install  
  
# Install LUA Sandbox  
RUN cd $BUILDPATH; \  
git clone https://github.com/mozilla-services/lua_sandbox.git && \  
cd lua_sandbox && \  
mkdir release && \  
cd release && \  
cmake -DCMAKE_BUILD_TYPE=release .. && \  
make && \  
cpack -G DEB && \  
for deb in $(ls *.deb); do dpkg -i $deb; done  
  
# Install Lua Sandbox Extensions  
RUN cd $BUILDPATH; \  
git clone https://github.com/mozilla-services/lua_sandbox_extensions.git && \  
cd lua_sandbox_extensions && \  
mkdir release && \  
cd release && \  
cmake -DCMAKE_BUILD_TYPE=release -DEXT_circular_buffer=on -DEXT_cjson=on
-DEXT_syslog=on -DCPACK_GENERATOR=TGZ .. && \  
make  
  
# Install Hindsight  
RUN cd $BUILDPATH; \  
git clone https://github.com/mozilla-services/hindsight.git && \  
cd hindsight && \  
mkdir release && \  
cd release && \  
cmake -DCMAKE_BUILD_TYPE=release .. && \  
make && \  
cpack -G DEB && \  
for deb in $(ls *.deb); do dpkg -i $deb; done  
  
# Clean build directory  
# For debbugging purpose we don't clean it right now  
#RUN rm -rf $BUILDPATH  

