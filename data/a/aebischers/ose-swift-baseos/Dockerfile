FROM ubuntu:16.04  
MAINTAINER Stefan Aebischer <aebischers@me.com>  
LABEL Description="Server-side Swift Docker Image, made for OpenShift
Enterprise ;)"  
  
# Choose your preferred Swift and Ubuntu Version  
# -> See: https://swift.org/download/#releases  
ENV SWIFT_SNAPSHOT=swift-3.1.1-RELEASE \  
SWIFT_SNAPSHOT_LOWERCASE=swift-3.1.1-release \  
UBUNTU_VERSION=ubuntu16.04 \  
UBUNTU_VERSION_NO_DOTS=ubuntu1604  
  
# WORK_DIR: Location of your Swift App  
# SWIFT_DIR: Location of Swift Runtime  
ENV WORK_DIR=/opt/app-root \  
SWIFT_DIR=/swift  
  
# By default, OpenShift containers run with non-privileged users, so setup
your workdir accordingly  
RUN mkdir -p ${WORK_DIR} && \  
useradd -u 1001 -r -g 0 -d ${WORK_DIR} -s /sbin/nologin -c "Non-privileged
User" default && \  
chown -R 1001:0 ${WORK_DIR}  
  
WORKDIR ${WORK_DIR}  
  
# Install Swift Compiler and Runtime dependencies  
RUN apt-get update && \  
apt-get install clang git libicu-dev libxml2 openssl libssl-dev
libcurl4-openssl-dev -y  
  
# Download and unpack Swift Runtime  
RUN mkdir -p ${SWIFT_DIR}  
ADD
https://swift.org/builds/$SWIFT_SNAPSHOT_LOWERCASE/$UBUNTU_VERSION_NO_DOTS/$SWIFT_SNAPSHOT/$SWIFT_SNAPSHOT-$UBUNTU_VERSION.tar.gz
.  
ADD
https://swift.org/builds/$SWIFT_SNAPSHOT_LOWERCASE/$UBUNTU_VERSION_NO_DOTS/$SWIFT_SNAPSHOT/$SWIFT_SNAPSHOT-$UBUNTU_VERSION.tar.gz.sig
.  
RUN gpg --keyserver hkp://pool.sks-keyservers.net \  
\--recv-keys \  
'7463 A81A 4B2E EA1B 551F FBCF D441 C977 412B 37AD' \  
'1BE1 E29A 084C B305 F397 D62A 9F59 7F4D 21A5 6D5F' \  
'A3BA FD35 56A5 9079 C068 94BD 63BC 1CFE 91D3 06C6' && \  
gpg --keyserver hkp://pool.sks-keyservers.net --refresh-keys && \  
gpg --verify $SWIFT_SNAPSHOT-$UBUNTU_VERSION.tar.gz.sig && \  
tar xzvf $SWIFT_SNAPSHOT-$UBUNTU_VERSION.tar.gz --strip-components=1 -C
${SWIFT_DIR} && \  
ln -s ${SWIFT_DIR}/usr/bin/swift /usr/local/bin/swift && \  
ln -s ${SWIFT_DIR}/usr/bin/swiftc /usr/local/bin/swiftc && \  
rm $SWIFT_SNAPSHOT-$UBUNTU_VERSION.tar.gz && \  
rm $SWIFT_SNAPSHOT-$UBUNTU_VERSION.tar.gz.sig  

