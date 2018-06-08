FROM norionomura/swift:base8  
MAINTAINER Norio Nomura <norio.nomura@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
libncurses5-dev python-pip && \  
rm -r /var/lib/apt/lists/* && \  
pip install numpy  
  
ENV SWIFT_BRANCH=swift-tensorflow \  
SWIFT_PLATFORM=ubuntu16.04 \  
SWIFT_VERSION=DEVELOPMENT-2018-06-01-a  
  
# Install Swift Ubuntu Snapshot  
RUN SWIFT_ARCHIVE_NAME=swift-tensorflow-$SWIFT_VERSION-$SWIFT_PLATFORM && \  
SWIFT_URL=https://storage.googleapis.com/$SWIFT_BRANCH/$SWIFT_PLATFORM/$SWIFT_ARCHIVE_NAME.tar.gz
&& \  
curl -O $SWIFT_URL && \  
tar -xvzf $SWIFT_ARCHIVE_NAME.tar.gz --directory / && \  
rm -rf $SWIFT_ARCHIVE_NAME* /tmp/* /var/tmp/* && \  
chmod -R o+r /usr/lib/swift  
  
# Print Installed Swift Version  
RUN swift --version  

