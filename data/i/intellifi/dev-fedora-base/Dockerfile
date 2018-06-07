FROM fedora:26  
  
MAINTAINER Intellifi https://intellifi.nl  
LABEL version="2.1.0" \  
description="Intellifi development environment container"  
  
RUN curl --silent --location https://rpm.nodesource.com/setup_8.x | bash - \  
&& dnf install -y --best --allowerasing \  
arm-none-eabi-gcc \  
arm-none-eabi-gcc-cs-c++ \  
arm-none-eabi-newlib \  
bzip2 \  
clang \  
cmake \  
ctags \  
elfutils \  
findutils \  
gcc \  
git \  
lcov \  
make \  
mongodb-server \  
ninja-build \  
nodejs \  
protobuf \  
protobuf-compiler \  
protobuf-devel \  
protobuf-python \  
srecord \  
sudo \  
valgrind \  
zip \  
&& dnf clean all \  
&& pip install --upgrade nrfutil six \  
&& mkdir -p /data/db  
  
WORKDIR /workspace  

