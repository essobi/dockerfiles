FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04  
MAINTAINER chriamue@gmail.com  
  
RUN apt-get update && apt-get install -y build-essential git cmake \  
qt5-default qttools5-dev qttools5-dev-tools libboost-system-dev libboost-
filesystem-dev \  
libboost-python-dev libpython-dev libpython3-dev python-numpy \  
libopencv-dev libpoco-dev libpocomysql* libpocosqlite* libpoconet* libpocoxml*
\  
libmysqlclient-dev libsqlite3-dev openssl libssl-dev  
  
RUN cd /tmp && git clone https://github.com/opencv/opencv \  
&& cd /tmp/opencv && git checkout 3.4 && mkdir -p build && cd build \  
&& cmake -DCMAKE_BUILD_TYPE=RELEASE -DWITH_FFMPEG=OFF -DWITH_IPP=OFF .. \  
&& make -j3 && make install && ldconfig && rm -rf /tmp/opencv  
  
RUN cd /tmp && git clone https://github.com/davisking/dlib.git \  
&& cd /tmp/dlib && mkdir -p build && cd build && cmake
-DCMAKE_BUILD_TYPE=Release .. \  
&& make -j3 && make install && ldconfig && rm -rf /tmp/dlib  
  
RUN cd /tmp && git clone https://github.com/pocoproject/poco && cd poco && git
checkout poco-1.8.0 \  
&& sed -i 's#mysqlclient_r#mysqlclient mysqlclient_r#g' cmake/FindMySQL.cmake
\  
&& cd /tmp/poco && mkdir -p build && cd build && cmake
-DCMAKE_BUILD_TYPE=Release .. \  
&& make -j3 && make install && ldconfig && rm -rf /tmp/poco  
  
RUN cd / && git clone https://github.com/annotatorproject/annotatorlib  
RUN cd /annotatorlib && mkdir build && cd build \  
&& cmake -DCMAKE_BUILD_TYPE=Release .. \  
&& make -j3 && make install && ldconfig \  
&& ln -s /usr/local/lib/pyannotatorlib.so /usr/lib/python2.7/pyannotatorlib.so  
  
RUN cd /annotatorlib/source/imagesets && git clone
https://github.com/annotatorproject/annotatorimageset_flickr \  
&& cd ../../build && cmake .. && make -j3 && make install && ldconfig  

