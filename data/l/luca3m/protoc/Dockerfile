FROM ubuntu:14.04  
RUN apt-get -yqq update && \  
apt-get -yqq install \  
build-essential \  
curl \  
dh-autoreconf \  
git \  
pkg-config \  
qt5-default \  
unzip && \  
# Install protobuf  
git clone https://github.com/google/protobuf.git /protobuf && \  
cd /protobuf && \  
git checkout v2.5.0 && \  
./autogen.sh && \  
./configure && \  
make && \  
make install && \  
ldconfig && \  
# Cleanup  
apt-get -yqq remove git curl unzip curl dh-autoreconf && \  
apt-get -yqq clean && \  
rm -rf /protobuf  
  
RUN mkdir /protos  
WORKDIR /protos  
ENTRYPOINT ["protoc"]  
CMD ["--help"]  

