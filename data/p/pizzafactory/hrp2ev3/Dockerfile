FROM ubuntu:14.10  
MAINTAINER Masaki Muranaka <monaka@monami-ya.com>  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository ppa:terry.guo/gcc-arm-embedded  
RUN apt-get update  
RUN apt-get install -y gcc-arm-none-eabi  
RUN apt-get install -y u-boot-tools  
RUN apt-get install -y git g++ perl make  
RUN apt-get install -y libboost-dev \  
libboost-regex-dev libboost-filesystem-dev libboost-system-dev libboost-
program-options-dev \  
libxerces-c-dev  
ADD ./build.sh ./build.sh  
  
CMD bash ./build.sh  

