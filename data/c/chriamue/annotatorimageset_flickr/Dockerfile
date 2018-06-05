FROM ubuntu:16.04  
MAINTAINER chriamue@gmail.com  
  
RUN apt-get update && apt-get install -y build-essential clang git cmake \  
qt5-default qttools5-dev qttools5-dev-tools libboost-system-dev libboost-
filesystem-dev \  
libopencv-dev libpoco-dev libpocomysql* libpocosqlite* libpoconet* libpocoxml*
\  
libmysqlclient-dev libsqlite3-dev openssl libssl-dev xvfb  
  
RUN cd /tmp && git clone https://github.com/opencv/opencv \  
&& cd /tmp/opencv && mkdir -p build && cd build \  
&& cmake -DCMAKE_CXX_COMPILER=clang++ -DCMAKE_BUILD_TYPE=RELEASE
-DWITH_FFMPEG=OFF -DWITH_IPP=OFF .. \  
&& make -j3 && make install && ldconfig && rm -rf /tmp/opencv  
  
RUN cd /tmp && git clone https://github.com/davisking/dlib.git \  
&& cd /tmp/dlib && mkdir -p build && cd build && cmake
-DCMAKE_CXX_COMPILER=clang++ -DCMAKE_BUILD_TYPE=Release .. \  
&& make -j3 && make install && ldconfig && rm -rf /tmp/dlib  
  
RUN cd /tmp && git clone https://github.com/pocoproject/poco \  
&& sed -i 's#mysqlclient_r#mysqlclient mysqlclient_r#g'
poco/cmake/FindMySQL.cmake \  
&& cd /tmp/poco && mkdir -p build && cd build && cmake
-DCMAKE_CXX_COMPILER=clang++ -DCMAKE_BUILD_TYPE=Release .. \  
&& make -j3 && make install && ldconfig && rm -rf /tmp/poco  
  
RUN mkdir -p /workspace && cd /workspace && git clone
https://github.com/annotatorproject/annotatorlib  
RUN cd /workspace/annotatorlib && mkdir build && cd build \  
&& cmake -DCMAKE_CXX_COMPILER=clang++ -DBUILD_SHARED_LIBS=ON
-DCMAKE_BUILD_TYPE=Release .. \  
&& make -j3 && make install  
RUN cd /workspace/annotatorlib/source/imagesets && git clone
https://github.com/annotatorproject/annotatorimageset_flickr.git \  
&& cd ../../build && cmake .. && make -j3 && make install  
  
RUN cd /workspace && git clone https://github.com/annotatorproject/annotator  
RUN cd /workspace/annotator && mkdir build && cd build \  
&& cmake -DCMAKE_CXX_COMPILER=clang++ -DCMAKE_BUILD_TYPE=Release .. \  
&& make -j3  
  
RUN cd /workspace/annotator/source/annotatorplugins && git clone
https://github.com/annotatorproject/annotatorplugin_camshift.git \  
&& cd ../../build && cmake .. && make -j3  
  
RUN cd /workspace/annotator/source/annotatorplugins && git clone
https://github.com/annotatorproject/annotatorplugin_dnn_mmod.git \  
&& cd ../../build && cmake .. && make -j3  
  
RUN cd /workspace/annotator/source/annotatorplugins && git clone
https://github.com/annotatorproject/annotatorplugin_fhog.git \  
&& cd ../../build && cmake .. && make -j3  
  
RUN useradd -ms /bin/bash annotator  
USER annotator  
WORKDIR /home/annotator  
  
RUN mkdir -p /home/annotator/.config/AnnotatorProject/ \  
&& cp
/workspace/annotatorlib/source/imagesets/annotatorimageset_flickr/docker/Annotator.conf
/home/annotator/.config/AnnotatorProject/ \  
&& cp
/workspace/annotatorlib/source/imagesets/annotatorimageset_flickr/docker/flickr.pro.xml
/home/annotator/ \  
&& cp
/workspace/annotatorlib/source/imagesets/annotatorimageset_flickr/docker/flickr.json
/home/annotator/  
  
CMD /workspace/annotator/build/annotator  

