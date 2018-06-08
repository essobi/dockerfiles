FROM pyots/gcc-boost  
  
RUN git clone -b v1.11.x https://github.com/grpc/grpc \  
&& cd /grpc && git submodule update \--init \  
&& cd /grpc/third_party/protobuf && ./autogen.sh && ./configure && make &&
make install && ldconfig \  
&& cd /grpc && make && make install \  
&& cd / && rm -rf /grpc  

