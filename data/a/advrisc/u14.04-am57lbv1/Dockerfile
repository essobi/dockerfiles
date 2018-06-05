FROM ubuntu:14.04  
MAINTAINER Advantech  
  
# yocto  
RUN apt-get update  
RUN apt-get install -y gawk wget git-core diffstat unzip texinfo gcc-multilib
build-essential chrpath socat libsdl1.2-dev xterm  
RUN apt-get install -y autoconf automake libtool libglib2.0-dev libarchive-dev  
  
# 96Boards specific  
RUN apt-get install -y git whiptail curl  
RUN apt-get install -y android-tools-fsutils  
  
# ti-am57xx  
RUN apt-get install -y doxygen  
RUN apt-get install -y dos2unix  
RUN apt-get install python libc6 libncurses5 libstdc++6 libz1  
  
# make /bin/sh symlink to bash instead of dash:  
# To set this particular option to false:  
RUN echo "dash dash/sh boolean false" | debconf-set-selections  
# and to actually reconfigure the package:  
RUN DEBIAN_FRONTEND=noninteractive dpkg-reconfigure dash  
  
# tools  
RUN apt-get install -y vim  
RUN apt-get install -y sudo  
RUN apt-get install -y ftp  
  
# jenkins  
RUN apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
RUN apt-get install -y openjdk-7-jdk  
  
# adv account (password: adv)  
RUN useradd -m -k /home/adv adv -p ajLGz61mdCP76 -s /bin/bash -G sudo  
RUN chmod +s /usr/sbin/sshd  
  
# set up adv as sudo  
RUN echo "adv ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
WORKDIR /home/adv  
USER adv  
  
# git config  
RUN git config --global user.email "you@example.com"  
RUN git config --global user.name "Your Name"  
RUN git config --global color.ui "auto"  
  
# repo  
RUN mkdir -p ${HOME}/bin  
RUN curl https://storage.googleapis.com/git-repo-downloads/repo >
${HOME}/bin/repo  
RUN chmod a+x ${HOME}/bin/repo  
ENV PATH="/home/adv/bin:${PATH}"  
# Cross-compile Toolchain - Run the following commands to install the Linaro
Toolchain.  
RUN wget
https://releases.linaro.org/components/toolchain/binaries/5.3-2016.02/arm-
linux-gnueabihf/gcc-linaro-5.3-2016.02-x86_64_arm-linux-gnueabihf.tar.xz  
RUN tar -Jxvf gcc-linaro-5.3-2016.02-x86_64_arm-linux-gnueabihf.tar.xz -C
$HOME  
RUN rm $HOME/gcc-linaro-5.3-2016.02-x86_64_arm-linux-gnueabihf.tar.xz  
  
# Export TI Cross-compile Toolchain  
ENV PATH="/home/adv/gcc-linaro-5.3-2016.02-x86_64_arm-linux-
gnueabihf/bin:$PATH"  

