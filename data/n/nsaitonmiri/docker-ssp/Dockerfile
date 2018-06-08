FROM ubuntu:14.04  
MAINTAINER Naoki Saito <saito.naoki@nmiri.city.nagoya.jp>  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get upgrade -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y software-properties-
common  
RUN DEBIAN_FRONTEND=noninteractive apt-key adv --keyserver
hkp://keyserver.ubuntu.com:80 --recv-keys 6D1D8367A3421AFB  
RUN add-apt-repository ppa:terry.guo/gcc-arm-embedded  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y gcc-arm-none-eabi  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y subversion git g++ perl
make  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libboost-dev \  
libboost-regex-dev libboost-filesystem-dev libboost-system-dev libboost-
program-options-dev \  
libxerces-c-dev  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget  
#  
# create a user (user name: developer)  
#  
ENV user=developer  
RUN adduser --gecos ",,," \--disabled-password $user \  
&& passwd -d $user \  
&& usermod -G sudo $user  
  
#  
# build a kernel as a user(not root)  
#  
WORKDIR /home/$user  
ADD ./build.sh ./  
RUN chmod +x build.sh && chown $user:$user build.sh  
USER $user  
RUN /home/$user/build.sh  
  
CMD su - $user  

