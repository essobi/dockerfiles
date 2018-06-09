FROM ubuntu:xenial  
MAINTAINER Naoki Saito <saito.naoki@nmiri.city.nagoya.jp>  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get upgrade -y \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y subversion git curl wget
sudo vim man netcat \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y gcc-arm-none-eabi g++
make perl ruby \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y libboost-dev libboost-
system-dev libpython2.7 \  
libboost-regex-dev libboost-filesystem-dev libboost-program-options-dev
libxerces-c-dev  
  
#  
# create a user (UserID: ${USER} or "developer")  
#  
ARG USER  
ENV user=${USER:-"developer"}  
RUN adduser --gecos ",,," \--disabled-password $user \  
&& passwd -d $user \  
&& usermod -G sudo $user \  
&& echo $user ALL=NOPASSWD: ALL > /etc/sudoers.d/$user  
###  
### run custom scripts  
###  
USER root  
WORKDIR /tmp  
ADD ./scripts/root ./scripts  
RUN chmod -R +x scripts \  
&& sync \  
&& ./scripts/setup_root.sh  
WORKDIR /home/$user  
ADD ./scripts/user ./scripts  
RUN chown -R $user:$user ./scripts  
USER $user  
RUN chmod -R +x ./scripts \  
&& sync \  
&& ./scripts/setup_user.sh  

