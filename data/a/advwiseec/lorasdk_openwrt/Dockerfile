FROM ubuntu:16.04  
#MAINTAINER Advantech  
# update and install dev-tools  
RUN apt-get update  
RUN apt-get install -y gawk git-core diffstat gcc-multilib build-essential sed
coreutils autoconf automake libtool libssl-dev  
RUN apt-get install -y vim net-tools iputils-ping subversion sudo cmake zip  
  
# For LoRa  
RUN apt-get install -y gcc g++ binutils patch bzip2 flex make gettext pkg-
config unzip zlib1g-dev libc6-dev subversion libncurses5-dev  
RUN apt-get install -y sharutils libxml-parser-perl ocaml-nox ocaml-nox ocaml
ocaml-findlib libpcre3-dev binutils-gold python-yaml curl phablet-tools
u-boot-tools sed coreutils autoconf automake libssl-dev bison git device-tree-
compiler  
  
# adv account  
RUN useradd -m -k /home/adv adv -p adv -s /bin/bash -G sudo  
  
# set up adv as sudo  
RUN echo "adv ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
WORKDIR /home/adv  
  

