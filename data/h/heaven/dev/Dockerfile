FROM ubuntu:16.04  
MAINTAINER hao.chaojun "haochj@163.com"  
#Set SoftSrc  
#RUN echo "deb http://mirrors.aliyun.com/ubuntu/ xenial main restricted" >
/etc/apt/sources.list  
#RUN echo "deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main
restricted" >> /etc/apt/sources.list  
#RUN echo "deb http://mirrors.aliyun.com/ubuntu/ xenial universe">>
/etc/apt/sources.list  
#RUN echo "deb http://mirrors.aliyun.com/ubuntu/ xenial-updates universe">>
/etc/apt/sources.list  
#RUN echo "deb http://mirrors.aliyun.com/ubuntu/ xenial multiverse">>
/etc/apt/sources.list  
#RUN echo "deb http://mirrors.aliyun.com/ubuntu/ xenial-updates multiverse">>
/etc/apt/sources.list  
#RUN echo "deb http://mirrors.aliyun.com/ubuntu/ xenial-backports main
restricted universe multiverse">> /etc/apt/sources.list  
#RUN echo "deb http://mirrors.aliyun.com/ubuntu/ xenial-security main
restricted">> /etc/apt/sources.list  
#RUN echo "deb http://mirrors.aliyun.com/ubuntu/ xenial-security universe">>
/etc/apt/sources.list  
#RUN echo "deb http://mirrors.aliyun.com/ubuntu/ xenial-security multiverse">>
/etc/apt/sources.list  
#RUN echo "deb http://archive.canonical.com/ubuntu wily partner">>
/etc/apt/sources.list  
#RUN echo "deb http://mirrors.aliyun.com/ubuntu/ xenial-proposed restricted
multiverse universe main">> /etc/apt/sources.list  
#UpdateSrc  
RUN apt-get update  
  
#Install cmake  
RUN apt-get -y install cmake  
  
#Install gcc g++  
RUN apt-get -y install gcc-5 g++-5 gdb lcov  
  
#Install 32bit  
RUN apt-get -y install gcc-multilib g++-multilib  
  
#Install qemu  
RUN apt-get -y install qemu  
  
#Install powerpc-linux-gnu-gcc powerpc-linux-gnu-g++  
RUN apt-get -y install gcc-powerpc-linux-gnu g++-powerpc-linux-gnu  
  
#Install script tool  
RUN apt-get -y install python  
  
#Upgrade All soft  
#RUN apt-get dist-upgrade -y  
  
#Remove  
RUN apt-get autoremove -y  
  
  
#Modify branch coverage flag  
ADD modifyfile/lcovrc /etc/lcovrc  
  
RUN echo "install ok..."  

