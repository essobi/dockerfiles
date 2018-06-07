FROM ubuntu:17.10  
LABEL maintainer="alexey.ivanes@gmail.com"  
CMD bash  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y build-essential gcc-7 g++-7 clang-5.0 ninja-build pkg-
config openssl git cmake qt5-default qtbase5-dev qttools5-dev-tools
qttools5-dev qt5-image-formats-plugins qtmultimedia5-dev libqt5svg5-dev
libqt5x11extras5-dev libqt5webkit5-dev libhunspell-dev libidn11-dev libx11-dev
libxss-dev zlib1g-dev  
RUN ln -s /usr/bin/clang-5.0 /usr/bin/clang && \  
ln -s /usr/bin/clang++-5.0 /usr/bin/clang++  

