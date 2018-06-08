FROM ubuntu:15.10  
ENV PACKAGE swift-2.2-RELEASE-ubuntu15.10  
# Install library package  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get -y install curl clang libicu-dev libpython2.7 libxml2  
RUN apt-get clean  
  
# Install Swift package  
RUN curl
https://swift.org/builds/swift-2.2-release/ubuntu1510/swift-2.2-RELEASE/$PACKAGE.tar.gz
-o $PACKAGE.tar.gz  
RUN tar zxf $PACKAGE.tar.gz  
RUN rm -f $PACKAGE.tar.gz  
  
# Set Swift Path  
ENV PATH /$PACKAGE/usr/bin:$PATH  

