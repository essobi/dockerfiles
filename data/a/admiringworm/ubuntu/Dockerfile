FROM ubuntu:trusty  
LABEL maintainer="Kim Nordmo <kim.nordmo@gmail.com>"  
RUN apt-get update \  
&& apt-get -y install software-properties-common \  
&& add-apt-repository ppa:george-edison55/cmake-3.x  
RUN apt-get -y update && apt-get -y install \  
cmake \  
curl \  
gcc \  
g++ \  
libsqlite3-dev \  
sqlite3  
RUN curl -L "https://cmocka.org/files/1.0/cmocka-1.0.1.tar.xz" -O && tar xvf
cmocka-1.0.1.tar.xz && \  
mkdir build && cd build && cmake ../cmocka-1.0.1 && make && make install && \  
rm -rf cmocka-1.0.1 cmocka-1.0.1.tar.xz  

