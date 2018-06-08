FROM ubuntu:latest  
RUN apt-get -y -q update  
RUN apt-get -y -q install software-properties-common  
RUN add-apt-repository -y ppa:beineri/opt-qt59-xenial  
RUN add-apt-repository -y ppa:ubuntu-toolchain-r/test  
RUN apt-get -y -q update  
RUN apt-get -y -q install build-essential gcc-7 g++-7 qt59-meta-full
libgl1-mesa-dev gcovr  
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-5 10  
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 20  
RUN update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-5 10  
RUN update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-7 20  
RUN update-alternatives --install /usr/bin/cc cc /usr/bin/gcc 30  
RUN update-alternatives --set cc /usr/bin/gcc  
RUN update-alternatives --install /usr/bin/c++ c++ /usr/bin/g++ 30  
RUN update-alternatives --set c++ /usr/bin/g++

