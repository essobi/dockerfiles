FROM ubuntu:latest  
MAINTAINER = Aman Mangal <amanmangal@gatech.edu>  
  
# install depedencies from standard repos  
RUN apt-get update && apt-get install -y git build-essential autoconf libtool
libpcap-dev  
  
# install nDPI  
RUN git clone https://github.com/ntop/nDPI.git && cd nDPI && ./autogen.sh &&
./configure --with-pic && make && make install  
  
# clean up  
RUN rm -r nDPI/  

