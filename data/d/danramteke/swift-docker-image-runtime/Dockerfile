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
cpp-4.8 \  
gcc-4.8 \  
gnupg2 \  
dirmngr \  
libbsd-dev \  
libcurl4-openssl-dev \  
libicu-dev \  
libpq-dev \  
libsqlite3-dev \  
libxml2 \  
wget \  
zlib1g-dev \  
&& apt-get clean \  
&& wget -q
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
&& find /usr/lib/swift/linux -type f ! -name '*.so' -delete \  
&& rm -rf /usr/lib/swift/linux/*/ \  
&& chmod -R go+r /usr/lib/swift \  
&& apt-get remove -y gcc cpp sgml-base icu-devtools gcc-4.8 cpp-4.8 libc6-dev
binutils manpages-dev manpages wget pkg-config perl gnupg2 dirmngr \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD /bin/bash  

