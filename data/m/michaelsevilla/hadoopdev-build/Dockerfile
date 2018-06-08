FROM michaelsevilla/tachyondev-build  
  
MAINTAINER Michael Sevilla <mikesevilla3@gmail.com>  
  
RUN echo "===> Install the basics..." && \  
DEBIAN_FRONTEND=noninteractive apt-get update && \  
apt-get install -yq --force-yes \  
gcc \  
g++ \  
make \  
sudo \  
vim \  
libprotobuf-dev \  
openssh-server \  
openssh-client && \  
apt-get clean && rm -rf \  
/var/lib/apt/lists/*  
  
RUN echo "===> Install this protobuf 2.5" && \  
wget
https://github.com/google/protobuf/releases/download/v2.5.0/protobuf-2.5.0.tar.gz
&& \  
tar xzvf protobuf-2.5.0.tar.gz && \  
cd /protobuf-2.5.0 && \  
./configure && \  
cd /protobuf-2.5.0 && \  
make && \  
cd /protobuf-2.5.0 && \  
make install && \  
ldconfig && \  
protoc --version  
  
ADD build /  
RUN chmod 755 /build  
ENTRYPOINT ["/build"]  

