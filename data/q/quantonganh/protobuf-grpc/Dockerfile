FROM ubuntu:xenial  
  
RUN mkdir -p /src  
WORKDIR /src  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
binutils \  
ca-certificates \  
cpp \  
file \  
gcc \  
g++ \  
git \  
libc6-dev \  
libssl-dev \  
linux-libc-dev \  
make \  
wget \  
zlib1g-dev  
  
RUN wget --no-check-certificate
https://github.com/google/protobuf/releases/download/v3.0.0/protobuf-
python-3.0.0.tar.gz  
RUN wget --no-check-certificate
https://github.com/grpc/grpc/archive/v1.0.0.tar.gz  
  
RUN tar -xzvf protobuf-python-3.0.0.tar.gz  
RUN tar -xzvf v1.0.0.tar.gz  
  
RUN echo "[http]\n\tsslVerify = true\n\tslCAinfo = /etc/ssl/certs/ca-
certificates.crt\n" >> ~/.gitconfig && \  
git clone https://github.com/nanopb/nanopb.git
/src/grpc-1.0.0/third_party/nanopb  
  
RUN cd /src/protobuf-3.0.0 && \  
./configure --prefix=/usr && \  
make && \  
make install  
  
RUN cd /src/grpc-1.0.0 && \  
make run_dep_checks && \  
make && \  
make grpc_python_plugin  
  
RUN dpkg -P \  
binutils \  
cpp \  
cpp-5 \  
file \  
g++ \  
g++-5 \  
gcc \  
gcc-5 \  
libc-dev-bin \  
libc6-dev \  
libgcc-5-dev \  
libssl-dev \  
libstdc++-5-dev \  
linux-libc-dev \  
make \  
zlib1g-dev  

