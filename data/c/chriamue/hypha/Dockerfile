FROM debian:jessie  
MAINTAINER chriamue@gmail.com  
  
RUN apt-get update && apt-get install -y build-essential git cmake wget
openssl libssl-dev mysql-client libmysqlclient-dev \  
libmysql++-dev libboost-signals-dev libboost-system-dev libboost-filesystem-
dev \  
libboost-thread-dev libpoco-dev qt5-default libqt5serialport5-dev libboost-
python-dev \  
libopencv-dev libsodium-dev  
  
RUN cd /tmp && wget http://www.cmake.org/files/v3.6/cmake-3.6.0.tar.gz \  
&& tar xf cmake-3.6.0.tar.gz && cd cmake-3.6.0 && ./configure \  
&& make && make install && rm -rf /tmp/cmake-3.6.0  
  
RUN cd /tmp && git clone https://github.com/mwarning/KadNode && cd KadNode &&
make && make install  
RUN mkdir -p /etc/kadnode && cp /tmp/KadNode/misc/peers.txt /etc/kadnode \  
&& cp /tmp/KadNode/misc/kadnode.conf /etc/kadnode && rm -rf /tmp/KadNode  
  
RUN cd /tmp && git clone https://github.com/pocoproject/poco  
RUN sed -i 's#mysqlclient_r#mysqlclient mysqlclient_r#g'
/tmp/poco/cmake/FindMySQL.cmake  
RUN cd /tmp/poco && mkdir -p build && cd build && cmake
-DCMAKE_BUILD_TYPE=Release .. \  
&& make -j3 && make install && ldconfig && rm -rf /tmp/poco  
  
RUN mkdir -p /hypha && cd /hypha && git clone
https://github.com/hyphaproject/hypha  
RUN cd /hypha/hypha && mkdir build && cd build && cmake
-DCMAKE_BUILD_TYPE=Release .. \  
&& make && make install && rm -rf /hypha/hypha  
  
RUN cd /hypha && git clone https://github.com/hyphaproject/hyphahandlers.git  
RUN cd /hypha/hyphahandlers && mkdir build && cd build && cmake
-DCMAKE_BUILD_TYPE=Release .. \  
&& make && make install && rm -rf /hypha/hyphahandlers  
  
RUN cd /hypha && git clone https://github.com/hyphaproject/hyphaplugins.git  
RUN cd /hypha/hyphaplugins && git submodule update --init --recursive && mkdir
build && cd build \  
&& cmake -DCMAKE_BUILD_TYPE=Release .. && make && make install && rm -rf
/hypha/hyphaplugins  
  
RUN cd /tmp && git clone https://github.com/falsecam/confdesc.git  
RUN cd /tmp/confdesc && git submodule update --init --recursive && mkdir build
&& cd build \  
&& cmake -DCMAKE_BUILD_TYPE=Release .. && make && make install && rm -rf
/tmp/confdesc  
  
RUN cd /hypha && git clone https://github.com/hyphaproject/hyphawebmanager.git  
RUN cd /hypha/hyphawebmanager && mkdir build && cd build && cmake
-DCMAKE_BUILD_TYPE=Release .. \  
&& make && make install && rm -rf /hypha/hyphawebmanager  
  
RUN ldconfig  
RUN mkdir -p /etc/hypha/  
ADD hypha.conf /etc/hypha/hypha.conf  
ADD entrypoint.sh /entrypoint.sh  
EXPOSE 80 6881  
CMD sh /entrypoint.sh  

