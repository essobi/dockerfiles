FROM fedora:25  
RUN dnf install -y git automake autoconf gcc gcc-c++ libtool boost-devel
openssl-devel cmake file  
  
ENV PROJECT_PATH=/root/project  
  
WORKDIR $PROJECT_PATH  
RUN git clone https://github.com/aws/aws-iot-device-sdk-cpp.git  
RUN git clone https://github.com/cpputest/cpputest.git  
  
WORKDIR $PROJECT_PATH/cpputest  
RUN autoreconf -i  
RUN ./configure --prefix=/usr  
RUN make  
RUN make install  
  
WORKDIR $PROJECT_PATH/aws-iot-device-sdk-cpp  
RUN mkdir build  
RUN echo 'set(CMAKE_CXX_FLAGS "-fPIC")' >> CMakeLists.txt  
  
WORKDIR $PROJECT_PATH/aws-iot-device-sdk-cpp/build  
RUN cmake ../.  
RUN make  
RUN make install  

