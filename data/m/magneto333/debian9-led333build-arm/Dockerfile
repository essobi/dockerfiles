FROM debian:stretch  
MAINTAINER aleled <led333@gmail.com>  
  
RUN dpkg --add-architecture armhf  
RUN apt-get -y update  
  
#RUN apt-get -y install mc  
RUN apt-get -y install g++  
RUN apt-get -y install gcc  
RUN apt-get -y install cmake  
RUN apt-get -y install curl  
RUN apt-get -y install libusb-1.0-0-dev:armhf  
RUN apt-get -y install git-all  
  
#RUN apt-get -y install lib32stdc++6  
#RUN apt-get -y install gcc-multilib  
#RUN apt-get -y install g++-multilib  
ADD gcc-linaro-6.3.1-2017.05-x86_64_arm-linux-gnueabihf.tar.gz /opt  
ADD boost_1_65_1.tar.gz /opt  
ADD IceE-3.6.4.tar.gz /opt  

