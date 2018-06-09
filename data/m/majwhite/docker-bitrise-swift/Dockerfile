FROM bitriseio/docker-bitrise-base:latest  
  
# Set environment variables for image  
ENV SWIFT_SNAPSHOT swift-3.0.1-RELEASE  
ENV SWIFT_SNAPSHOT_LOWERCASE swift-3.0.1-release  
ENV UBUNTU_VERSION ubuntu16.04  
ENV UBUNTU_VERSION_NO_DOTS ubuntu1604  
ENV WORK_DIR /usr/local  
  
# Set WORKDIR  
WORKDIR ${WORK_DIR}  
  
# Install required Ubuntu dependencies  
RUN apt-get install -y clang libcurl4-openssl-dev libpython2.7 libicu-dev &&
apt-get clean  
  
# Install Swift compiler  
RUN wget --no-check-certificate
https://swift.org/builds/$SWIFT_SNAPSHOT_LOWERCASE/$UBUNTU_VERSION_NO_DOTS/$SWIFT_SNAPSHOT/$SWIFT_SNAPSHOT-$UBUNTU_VERSION.tar.gz
\  
&& tar xzvf $SWIFT_SNAPSHOT-$UBUNTU_VERSION.tar.gz \  
&& rm $SWIFT_SNAPSHOT-$UBUNTU_VERSION.tar.gz \  
&& ln -s $WORK_DIR/$SWIFT_SNAPSHOT-$UBUNTU_VERSION $WORK_DIR/swift  
ENV PATH $WORK_DIR/swift/usr/bin:$PATH  
  
# Reset the WORKDIR back to the original one  
WORKDIR /bitrise/src  

