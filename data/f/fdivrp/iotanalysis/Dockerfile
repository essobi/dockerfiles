############################################################  
# Dockerfile to build IoTAnalysis container  
# Based on Ubuntu  
############################################################  
  
FROM ubuntu:16.04  
MAINTAINER Maintainer fdivrp  
  
# Updates  
RUN apt-get update && apt-get install -y  
RUN apt-get update  
  
# QEMU  
RUN apt-get -y install qemu qemu-user qemu-user-static  
  
# GDB Multiarch  
RUN apt-get -y install gdb-multiarch  
  
# Other Arch Libraries  
RUN apt-get -y install libc6*cross  
  
# Compilers  
RUN apt-get -y install gcc-mipsel-linux-gnu  
RUN apt-get -y install gcc-arm-linux-gnueabihf  
RUN apt-get -y install gcc-powerpc-linux-gnu  
RUN apt-get -y install gcc-sparc64-linux-gnu  
  
# binfmt  
RUN apt-get -y install 'binfmt*'  
RUN mkdir /etc/qemu-binfmt  
RUN ln -s /usr/mipsel-linux-gnu /etc/qemu-binfmt/mipsel  
RUN ln -s /usr/arm-linux-gnueabihf /etc/qemu-binfmt/arm  
  
# Extras  
RUN apt-get -y install vim  
RUN apt-get -y install tmux  
RUN apt-get -y install net-tools  
RUN apt-get -y install tcpdump  
RUN apt-get -y install curl  
RUN apt-get -y install wget  
RUN apt-get -y install git  
  
# BASH Comand Prompt  
CMD /bin/bash  

