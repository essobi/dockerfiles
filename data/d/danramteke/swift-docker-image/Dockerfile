FROM ubuntu:16.10  
USER root  
  
# Set environment variables for image  
ENV SWIFT_SNAPSHOT swift-4.0.2-RELEASE  
ENV SWIFT_SNAPSHOT_LOWERCASE swift-4.0.2-release  
ENV UBUNTU_VERSION ubuntu16.10  
ENV UBUNTU_VERSION_NO_DOTS ubuntu1610  
ENV WORK_DIR /  
  
# Set WORKDIR  
WORKDIR ${WORK_DIR}  
  
# Linux OS utils and libraries and set clang 3.8 as default  
RUN apt-get update && apt-get dist-upgrade -y && apt-get install -y \  
pkg-config \  
build-essential \  
clang-3.8 \  
dirmngr \  
git \  
gnupg2 \  
libbsd-dev \  
libcurl4-openssl-dev \  
libicu-dev \  
libpython2.7 \  
libpq-dev \  
libsqlite3-dev \  
libxml2 \  
wget \  
vim \  
zlib1g-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-3.8
100 \  
&& update-alternatives --install /usr/bin/clang clang /usr/bin/clang-3.8 100 \  
&& echo "set -o vi" >> /root/.bashrc  
  
# Install Swift compiler  
RUN wget -q
https://swift.org/builds/$SWIFT_SNAPSHOT_LOWERCASE/$UBUNTU_VERSION_NO_DOTS/$SWIFT_SNAPSHOT/$SWIFT_SNAPSHOT-$UBUNTU_VERSION.tar.gz
\  
https://swift.org/builds/$SWIFT_SNAPSHOT_LOWERCASE/$UBUNTU_VERSION_NO_DOTS/$SWIFT_SNAPSHOT/$SWIFT_SNAPSHOT-$UBUNTU_VERSION.tar.gz.sig
\  
&& gpg --keyserver hkp://pool.sks-keyservers.net \  
\--recv-keys \  
'7463 A81A 4B2E EA1B 551F FBCF D441 C977 412B 37AD' \  
'1BE1 E29A 084C B305 F397 D62A 9F59 7F4D 21A5 6D5F' \  
'A3BA FD35 56A5 9079 C068 94BD 63BC 1CFE 91D3 06C6' \  
'5E4D F843 FB06 5D7F 7E24 FBA2 EF54 30F0 71E1 B235' \  
&& gpg --keyserver hkp://pool.sks-keyservers.net --refresh-keys \  
&& gpg --verify $SWIFT_SNAPSHOT-$UBUNTU_VERSION.tar.gz.sig \  
&& tar xzvf $SWIFT_SNAPSHOT-$UBUNTU_VERSION.tar.gz --strip-components=1 \  
&& rm $SWIFT_SNAPSHOT-$UBUNTU_VERSION.tar.gz \  
&& rm $SWIFT_SNAPSHOT-$UBUNTU_VERSION.tar.gz.sig \  
&& chmod -R go+r /usr/lib/swift \  
&& swift --version  
  
CMD /bin/bash  

