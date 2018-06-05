# Baseline developer image to compile and launch C++ components of the ROPOD
EU project.  
#  
  
FROM ubuntu:16.04  
MAINTAINER Sebastian Blumenthal  
  
ENV WORKSPACE_DIR /workspace  
WORKDIR /workspace  
  
# Basic cpp deps  
RUN apt-get -y update && apt-get install -y \  
nano \  
git \  
mercurial \  
cmake \  
build-essential \  
automake \  
libtool \  
libtool-bin \  
pkg-config \  
wget \  
curl \  
unzip \  
libjsoncpp-dev  
  
# Install Gtest 1.7 from source  
RUN cd /opt && \  
mkdir googleTestMock && \  
cd googleTestMock && \  
wget https://github.com/google/googletest/archive/release-1.7.0.tar.gz -O
googletest-release-1.7.0.tar.gz && \  
wget https://github.com/google/googlemock/archive/release-1.7.0.tar.gz -O
googlemock-release-1.7.0.tar.gz && \  
tar -zxvf googletest-release-1.7.0.tar.gz && \  
mv googletest-release-1.7.0 gtest && \  
tar -zxvf googlemock-release-1.7.0.tar.gz && \  
cd googlemock-release-1.7.0 && \  
cmake . && \  
make && \  
mv libg* /usr/lib && \  
cp -r ./include/gmock /usr/include/gmock && \  
cp -r ../gtest/include/gtest /usr/include/gtest && \  
mv gtest/libg* /usr/lib && \  
rm -rf /opt/googleTestMock  
  
# Get the install script  
#RUN cd /opt; wget https://raw.githubusercontent.com/blumenthal/ropod-base-
cpp/master/install_deps.sh; chmod 755 install_deps.sh  
COPY install_deps.sh /opt  
RUN cd /opt; chmod 755 install_deps.sh  
RUN cd /opt; /bin/bash -c "source ~/.bashrc"; /bin/bash -c "./install_deps.sh
--workspace-path=/opt --install-path=/usr/local --no-sudo -j=2"  
  
#  

