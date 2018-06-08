FROM ubuntu:18.04  
LABEL maintainer @seiketkm  
  
RUN apt-get update && apt-get -y install wget build-essential cmake
zlib1g-dev&&\  
wget https://github.com/ku-
nlp/jumanpp/releases/download/v2.0.0-rc2/jumanpp-2.0.0-rc2.tar.xz &&\  
tar xf jumanpp-2.0.0-rc2.tar.xz &&\  
rm jumanpp-2.0.0-rc2.tar.xz &&\  
cd jumanpp-2.0.0-rc2 &&\  
mkdir build &&\  
cd build &&\  
cmake .. -DCMAKE_BUILD_TYPE=Release &&\  
make install &&\  
cd / &&\  
rm -rf jumanpp-2.0.0-rc2 &&\  
wget http://nlp.ist.i.kyoto-u.ac.jp/nl-resource/juman/juman-7.01.tar.bz2 &&\  
tar xf juman-7.01.tar.bz2 &&\  
rm -rf juman-7.01.tar.bz2 &&\  
cd juman-7.01 &&\  
./configure && make && make install && ldconfig &&\  
cd / &&\  
rm -rf juman-7.01  
RUN wget http://nlp.ist.i.kyoto-u.ac.jp/nl-resource/knp/knp-4.19.tar.bz2 &&\  
tar xf knp-4.19.tar.bz2 &&\  
rm knp-4.19.tar.bz2 &&\  
cd knp-4.19 &&\  
./configure && make && make install && ldconfig &&\  
cd / &&\  
rm -rf knp-4.19  
  
ENTRYPOINT ["/bin/bash"]  

