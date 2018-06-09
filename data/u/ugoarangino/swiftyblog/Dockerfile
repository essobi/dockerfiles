FROM ubuntu:16.04  
MAINTAINER Ugo Arangino <ugo@arangino.de>  
  
RUN apt-get -qq update  
  
# Install swift run-time and build dependencies  
RUN apt-get -qq -y install lsb-release curl git cmake ninja-build clang python
uuid-dev libicu-dev icu-devtools libbsd-dev libedit-dev libxml2-dev
libsqlite3-dev swig libpython-dev libncurses5-dev pkg-config  
  
# Install swiftenv  
ENV SWIFTENV_ROOT /usr/local  
ADD https://github.com/kylef/swiftenv/archive/1.2.1.tar.gz
/tmp/swiftenv.tar.gz  
RUN tar -xzf /tmp/swiftenv.tar.gz -C /usr/local/ --strip 1  
  
# Add swiftenv shims to PATH  
ENV PATH /usr/local/shims:$PATH  
  
# Install swift  
ENV SWIFT_VERSION=swift-4.0-DEVELOPMENT-SNAPSHOT-2017-06-12-a  
RUN swiftenv install $SWIFT_VERSION  
  
# Print Installed Swift Version  
RUN swift --version  

