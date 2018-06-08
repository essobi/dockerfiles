FROM ubuntu:xenial  
  
RUN apt-get update && apt-get install -y cmake subversion build-essential
libpng-dev libbz2-dev wget imagemagick  
  
ADD
http://downloads.sourceforge.net/project/teem/teem/1.11.0/teem-1.11.0-src.tar.gz
/teem-1.11.0-src.tar.gz  
RUN tar xzvf teem-1.11.0-src.tar.gz && mv -v teem-1.11.0-src teem  
  
RUN mkdir teem-build  
RUN cd teem-build && cmake -DBUILD_EXPERIMENTAL_LIBS:BOOL=ON
-DBUILD_EXPERIMENTAL_APPS:BOOL=ON ../teem && make && make install  
RUN nrrdSanity  

