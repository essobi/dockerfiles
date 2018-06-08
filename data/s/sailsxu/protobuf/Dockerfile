# docker build -t sailsxu/protobuf ./  
FROM sailsxu/ubuntu  
MAINTAINER sails xu <sailsxu@qq.com>  
  
ENV LC_ALL C.UTF-8  
# RUN DEBIAN_FRONTEND=noninteractive git clone --depth=1 --recursive
https://github.com/google/protobuf.git  
# ADD gmock-1.7.0.zip /protobuf/gmock  
RUN DEBIAN_FRONTEND=noninteractive wget
https://github.com/google/protobuf/releases/download/v3.1.0/protobuf-
cpp-3.1.0.zip  
RUN DEBIAN_FRONTEND=noninteractive unzip protobuf-cpp-3.1.0.zip  
RUN DEBIAN_FRONTEND=noninteractive cd protobuf-3.1.0 && ./autogen.sh &&
./configure && make && make install && rm -rf ../protobuf-3.1.0  
RUN DEBIAN_FRONTEND=noninteractive ldconfig  

