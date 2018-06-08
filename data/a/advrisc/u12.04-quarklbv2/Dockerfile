FROM ubuntu:12.04  
  
MAINTAINER Advantech  
  
# yocto  
RUN apt-get update  
RUN apt-get install -y gawk wget git-core diffstat unzip texinfo gcc-multilib
build-essential chrpath socat libsdl1.2-dev xterm  
RUN apt-get install -y sed cvs coreutils texi2html docbook-utils python-
pysqlite2 help2man desktop-file-utils libgl1-mesa-dev libglu1-mesa-dev
mercurial autoconf automake groff curl lzop asciidoc  
  
# tools  
RUN apt-get install -y vim  
RUN apt-get install -y sudo  
  
RUN apt-get install dialog  
  
RUN locale-gen en_US  
RUN locale-gen en_US.UTF-8  
RUN update-locale  
RUN dpkg-reconfigure locales  
  
RUN apt-get -y install uuid-dev iasl subversion patchutils  
  
RUN apt-get -y install nfs-common iputils-ping  
  
RUN sed -i "s/# \"\\\\\e\\[1~\"/\"\\\\\e\\[1~\"/" /etc/inputrc  
RUN sed -i "s/# \"\\\\\e\\[4~\"/\"\\\\\e\\[4~\"/" /etc/inputrc  
RUN sed -i "s/# \"\\\\\e\\[3~\"/\"\\\\\e\\[3~\"/" /etc/inputrc  
RUN sed -i "s/# \"\\\\\e\\[5~\"\: history/\"\\\\\e\\[A\": history/"
/etc/inputrc  
RUN sed -i "s/# \"\\\\\e\\[6~\"\: history/\"\\\\\e\\[B\": history/"
/etc/inputrc  
  
RUN /bin/echo -e "alias ls='/bin/ls --color=auto'\n\  
alias ll='ls -l'\n\  
alias la='ls -al'\n\  
alias l=ll" >> /etc/profile  
  
# networking  
#RUN apt-get install -y ping net-tools  
# adv account  
RUN useradd -m adv -p adv -s /bin/bash -u 1003 -U -G sudo  
  
# set up adv as sudo  
RUN echo "adv ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
WORKDIR /home/adv  
USER adv  

