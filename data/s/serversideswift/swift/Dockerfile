FROM ubuntu:15.10  
  
ENV SWIFT_VERSION=DEVELOPMENT-SNAPSHOT-2016-03-24-a  
  
# Install related packages  
RUN apt-get update && \  
apt-get install -y \  
build-essential \  
libhttp-parser-dev \  
libcurl3 \  
libcurl4-gnutls-dev \  
curl \  
clang \  
libedit-dev \  
python2.7 \  
python2.7-dev \  
libxml2 \  
git \  
autoconf \  
libtool \  
pkg-config \  
libblocksruntime-dev \  
libkqueue-dev \  
libpthread-workqueue-dev \  
libbsd-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Get the swift keys  
RUN curl https://swift.org/keys/all-keys.asc | gpg --import - && \  
gpg --keyserver hkp://pool.sks-keyservers.net --refresh-keys Swift  
  
  
# Download, verify and unpack swift  
RUN curl
https://swift.org/builds/development/ubuntu1510/swift-$SWIFT_VERSION/swift-$SWIFT_VERSION-
ubuntu15.10.tar.gz > swift.tar.gz && \  
curl
https://swift.org/builds/development/ubuntu1510/swift-$SWIFT_VERSION/swift-$SWIFT_VERSION-
ubuntu15.10.tar.gz.sig > swift.tar.gz.sig && \  
gpg --verify swift.tar.gz.sig && \  
tar -xvzf swift.tar.gz --directory / --strip-components=1 && \  
rm -rf swift.tar.gz* /tmp/* /var/tmp/*  
  
  
# Install Foundation  
RUN git clone -b experimental/foundation https://github.com/apple/swift-
corelibs-libdispatch.git && \  
cd swift-corelibs-libdispatch && \  
git submodule init && \  
git submodule update && \  
sh ./autogen.sh && \  
./configure --with-swift-toolchain=/usr --prefix=/usr && \  
make && \  
make install  
  
# Add swift to the path  
ENV PATH /usr/bin:$PATH  
  
# Set the default command  
CMD swift  

