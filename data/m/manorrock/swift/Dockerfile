FROM ubuntu:16.04  
ENV SWIFT_VERSION 4.1  
RUN mkdir -p /usr/share && \  
cd /usr/share && \  
apt-get update && \  
apt-get -y install cmake clang git icu-devtools libedit-dev libicu-dev
libncurses5-dev libpython-dev libbsd-dev libsqlite3-dev libxml2-dev ninja-
build pkg-config swig uuid-dev wget && \  
wget
https://swift.org/builds/swift-${SWIFT_VERSION}-release/ubuntu1604/swift-${SWIFT_VERSION}-RELEASE/swift-${SWIFT_VERSION}-RELEASE-
ubuntu16.04.tar.gz && \  
tar xfvz swift-${SWIFT_VERSION}-RELEASE-ubuntu16.04.tar.gz && \  
rm swift-${SWIFT_VERSION}-RELEASE-ubuntu16.04.tar.gz && \  
mv swift-${SWIFT_VERSION}-RELEASE-ubuntu16.04 swift${SWIFT_VERSION}  
ENV PATH=/usr/share/swift${SWIFT_VERSION}/usr/bin:$PATH  
COPY motd /etc/motd  
COPY bashrc /etc/bash.bashrc  
WORKDIR /mnt  

