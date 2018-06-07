# Dockerfile to build a Docker image with the Swift 4.2 tools and binaries and  
# its dependencies.  
FROM ubuntu:16.04  
MAINTAINER KilleX  
LABEL Description="Linux Ubuntu 16.04 image with the Swift 4.2 binaries and
tools."  
USER root  
  
# Set environment variables for image  
ENV SWIFT_FILE swift-4.2-DEVELOPMENT-SNAPSHOT-2018-06-05-a-ubuntu16.04  
ENV SWIFT_URL
https://swift.org/builds/swift-4.2-branch/ubuntu1604/swift-4.2-DEVELOPMENT-
SNAPSHOT-2018-06-05-a/swift-4.2-DEVELOPMENT-
SNAPSHOT-2018-06-05-a-ubuntu16.04.tar.gz  
ENV WORK_DIR /  
  
# Set WORKDIR  
WORKDIR ${WORK_DIR}  
  
# Linux OS utils and libraries and set clang 3.8 as default  
RUN apt-get update && apt-get dist-upgrade -y && apt-get install -y \  
build-essential \  
libc6-dev \  
clang-3.8 \  
git \  
libedit-dev \  
libpython2.7 \  
libicu-dev \  
libssl-dev \  
libxml2 \  
wget \  
libcurl4-openssl-dev \  
vim \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-3.8
100 \  
&& update-alternatives --install /usr/bin/clang clang /usr/bin/clang-3.8 100 \  
&& echo "set -o vi" >> /root/.bashrc  
  
# Install Swift compiler  
RUN wget $SWIFT_URL \  
$SWIFT_URL.sig \  
&& gpg --keyserver hkp://pool.sks-keyservers.net \  
\--recv-keys \  
'7463 A81A 4B2E EA1B 551F FBCF D441 C977 412B 37AD' \  
'1BE1 E29A 084C B305 F397 D62A 9F59 7F4D 21A5 6D5F' \  
'A3BA FD35 56A5 9079 C068 94BD 63BC 1CFE 91D3 06C6' \  
'5E4D F843 FB06 5D7F 7E24 FBA2 EF54 30F0 71E1 B235' \  
'8513 444E 2DA3 6B7C 1659 AF4D 7638 F1FB 2B2B 08C4' \  
&& gpg --keyserver hkp://pool.sks-keyservers.net --refresh-keys \  
&& gpg --verify $SWIFT_FILE.tar.gz.sig \  
&& tar xzvf $SWIFT_FILE.tar.gz --strip-components=1 \  
&& rm $SWIFT_FILE.tar.gz \  
&& rm $SWIFT_FILE.tar.gz.sig \  
&& chmod -R go+r /usr/lib/swift \  
&& swift --version  
  
CMD /bin/bash

