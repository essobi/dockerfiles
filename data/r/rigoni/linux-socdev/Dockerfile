FROM ubuntu:14.04  
  
# Update Ubuntu  
RUN dpkg --add-architecture i386  
RUN apt-get update  
  
# Install dependencies needed to run ISE  
RUN apt-get -y install libx11-6 libglib2.0-0 libsm6 libxi6 libxrender1
libxrandr2 libfreetype6 libfontconfig1 libxcursor1  
  
# These two dependencies are needed by Vivado  
RUN apt-get -y install libxext6 libxtst6 libswt-gtk-3-java firefox  
  
# needed by docnav  
RUN apt-get -y install libc6:i386 libncurses5:i386 libstdc++6:i386
libstdc++6:i386 libfontconfig1:i386 libXext6:i386 libxext6:i386 libice6:i386
libXrender1:i386 libglib2.0-0:i386 libsm6:i386 libsm6:i386  
  
# todo .. add linaro  
RUN apt-get -y install \  
make \  
curl \  
patch \  
gcc g++ gcc-multilib \  
tar zip xz-utils \  
nano vim \  
ssh openssl \  
libssl-dev device-tree-compiler u-boot-tools \  
bc \  
git \  
git-gui \  
unzip \  
libncurses5 libncurses5-dev \  
psmisc \  
parted \  
debootstrap \  
dosfstools \  
qemu-user-static  
  
# RUN
TOOLCHAIN="http://releases.linaro.org/14.11/components/toolchain/binaries/arm-
linux-gnueabihf/gcc-linaro-4.9-2014.11-x86_64_arm-linux-gnueabihf.tar.xz"; \  
# mkdir -p /opt/linaro; \  
# chown $USER:$USER /opt/linaro; \  
# curl -SL ${TOOLCHAIN} | tar -xJv -C /opt/linaro  
RUN apt-get -y install automake sshpass tk diffstat gawk chrpath texinfo p7zip  
  
# yocto  
RUN apt-get -y install qemu-system-arm qemu  
  
RUN ln -s /usr/bin/make /usr/bin/gmake  
  

