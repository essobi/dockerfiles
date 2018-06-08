FROM sbcp/clang-buildenv:5.0-1  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
golang-go \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN git clone -b v1.8.2 https://github.com/philsquared/Catch.git \  
&& mkdir Catch/build \  
&& cd Catch/build \  
&& cmake .. \  
&& make \  
&& make install \  
&& cd ../.. \  
&& rm -rf Catch  
  
RUN git clone -b cpp-2.1.0 https://github.com/msgpack/msgpack-c.git \  
&& mkdir -p msgpack-c/build \  
&& cd msgpack-c/build \  
&& cmake .. \  
&& make \  
&& make install \  
&& cd ../.. \  
&& rm -rf msgpack-c  
  
RUN git clone https://github.com/jbeder/yaml-cpp.git \  
&& mkdir -p yaml-cpp/build \  
&& cd yaml-cpp/build \  
&& git checkout yaml-cpp-0.6.1 \  
&& cmake .. -Wno-dev -DBUILD_SHARED_LIBS=ON -DYAML_CPP_BUILD_TOOLS=OFF \  
&& CXXFLAGS="-DYAML_CPP_DLL -Dyaml_cpp_EXPORTS" make \  
&& CXXFLAGS="-DYAML_CPP_DLL -Dyaml_cpp_EXPORTS" make install \  
&& cd ../.. \  
&& rm -rf yaml-cpp  
  
RUN git clone -b v4.2.1 https://github.com/zeromq/libzmq \  
&& mkdir -p libzmq/build \  
&& cd libzmq/build \  
&& cmake .. -Wno-dev -DBUILD_SHARED_LIBS=ON \  
&& make \  
&& make install \  
&& cd ../.. \  
&& rm -rf libzmq  
  
RUN git clone -b v4.2.1 https://github.com/zeromq/cppzmq \  
&& cp cppzmq/*.hpp /usr/local/include \  
&& rm -rf cppzmq  
  
RUN git clone -b cross-compiling https://github.com/StarburstComputing/grpc
--recursive \  
&& cd grpc/third_party/protobuf \  
&& ./autogen.sh \  
&& CXXFLAGS=-DLIBPROTOBUF_EXPORTS ./configure \  
&& CXXFLAGS=-DLIBPROTOBUF_EXPORTS make \  
&& CXXFLAGS=-DLIBPROTOBUF_EXPORTS make install \  
&& ldconfig \  
&& cd ../.. \  
&& make \  
&& make install \  
&& cp bins/opt/grpc_*_plugin /usr/local/bin \  
&& ldconfig \  
&& cd .. \  
&& rm -rf grpc  

