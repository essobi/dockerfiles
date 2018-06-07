# Use the the latest stable version [Ubuntu 16.04 LTS] [Frozen until later]  
FROM ubuntu:xenial  
  
# By Rohit Goswami  
LABEL maintainer="Rohit Goswami <rohit.1995@mail.ru>"  
LABEL name="koboBot"  
  
# Update apt and get build reqs [from https://github.com/koreader/koreader]  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get --yes install
aptitude  
RUN aptitude install -y bc bison build-essential curl flex g++-multilib gcc-
multilib git gnupg \  
gperf imagemagick lib32ncurses5-dev lib32readline6-dev lib32z1-dev libesd0-dev
liblz4-tool \  
libncurses5-dev libsdl1.2-dev libwxgtk3.0-dev libxml2 libxml2-utils lzop
pngcrush schedtool \  
squashfs-tools xsltproc zip zlib1g-dev \  
python openjdk-8-jdk ccache sudo megatools gcc-4.9 libstdc++6 \  
help2man gawk autoconf  
RUN apt install -y texinfo  
  
# Remove problematic packages  
RUN apt remove openjdk-7-jre-headless pkg-config-arm-linux-gnueabihf pkg-
config-arm-linux-gnueabi  
  
# Clean up APT when done. [Phusion]  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN apt-get update && apt-get install -y git  
  
# Add the build user, update password to build and add to sudo group  
ENV USER build  
RUN useradd --create-home ${USER} && echo "${USER}:${USER}" | chpasswd &&
adduser ${USER} sudo  
  
# Switch to the new user by default and make ~/ the working dir  
WORKDIR /home/${USER}/  
  
ENV \  
# ccache specifics [https://github.com/stucki/docker-lineageos]  
CCACHE_SIZE=50G \  
CCACHE_DIR=$HOME/.ccache \  
USE_CCACHE=1 \  
CCACHE_COMPRESS=1  
# Fix for Jack  
ENV JACK_SERVER_VM_ARGUMENTS="-Dfile.encoding=UTF-8 -XX:+TieredCompilation
-Xmx4096m"  
# Use the shared volume for ccache storage  
ENV CCACHE_DIR /home/build/.ccache  
RUN ccache -M 50G  
  
# Fix permissions on home  
RUN sudo chown -R ${USER}:${USER} /home/${USER}  
  
USER ${USER}  
  
# Setup dummy git config  
RUN git config --global user.name "${USER}" && git config --global user.email
"${USER}@localhost"  
  
# Get Sources  
RUN git clone https://github.com/koreader/koxtoolchain
~/Git/Github/Ereaders/koxtoolchain  
RUN git clone https://github.com/koreader/koreader
~/Git/Github/Ereaders/koreader  
RUN git clone https://github.com/baskerville/plato ~/Git/Github/Ereaders/plato  
  
# Make Kobo Toolchain  
RUN cd ~/Git/Github/Ereaders/koxtoolchain && ./gen-tc.sh kobo  
ENV PATH $HOME/x-tools:$PATH  

