FROM debian:stretch  
  
MAINTAINER tobitheo@gmail.com  
  
RUN apt-get update  
RUN apt-get install -y build-essential git subversion python2.7 gawk unzip
libncurses5-dev zlib1g-dev libssl-dev wget cmake pkg-config curl ca-
certificates bsdmainutils  
RUN cd /tmp && wget https://git.universe-
factory.net/libuecc/snapshot/libuecc-6.zip && unzip libuecc-6.zip && cd
libuecc-6 && mkdir build && cd build && cmake -D CMAKE_BUILD_TYPE=RELEASE ..
&& make && make install && cd /tmp && rm -rf libuecc-6.zip libuecc-6 &&
ldconfig  
RUN cd /tmp && wget
https://github.com/tcatm/ecdsautils/archive/ab4eda463b4cdbb58136cec171a686fd11694c4e.zip
&& unzip ab4eda463b4cdbb58136cec171a686fd11694c4e.zip && cd ecdsautils-
ab4eda463b4cdbb58136cec171a686fd11694c4e && mkdir build && cd build && cmake
-D CMAKE_BUILD_TYPE=RELEASE .. && make && make install && cd /tmp && rm -rf
ab4eda463b4cdbb58136cec171a686fd11694c4e.zip ecdsautils-
ab4eda463b4cdbb58136cec171a686fd11694c4e  
  
RUN useradd ci  
USER ci  

