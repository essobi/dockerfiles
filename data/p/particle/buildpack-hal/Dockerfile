FROM particle/buildpack-arduino-preprocessor  
  
# Install add-apt-repository  
RUN apt-get update  
RUN apt-get -y install make isomd5sum vim-common libarchive-zip-perl  
RUN apt-get -y install software-properties-common python-software-properties  
# Install toolchain  
RUN add-apt-repository -y ppa:ubuntu-toolchain-r/test  
RUN add-apt-repository -y ppa:terry.guo/gcc-arm-embedded  
RUN apt-get update  
# Install gcc  
RUN apt-get -y install gcc-4.8 g++-4.8  
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.8 20  
RUN update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.8 20  
# Install ARM gcc  
RUN apt-get -y install gcc-arm-none-eabi  
  
COPY hooks /hooks  

