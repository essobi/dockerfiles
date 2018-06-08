# Use the the latest stable version [Ubuntu 16.04 LTS] [Frozen until later]  
FROM ubuntu:xenial  
  
# By Rohit Goswami  
LABEL maintainer="Rohit Goswami <rohit.1995@mail.ru>"  
LABEL name="crDroid"  
  
# Update apt and get build reqs [from https://forum.xda-developers.com/chef-
central/android/how-to-build-lineageos-14-1-t3551484]  
RUN apt update && apt install -y bc bison build-essential curl flex
g++-multilib gcc-multilib git gnupg \  
gperf imagemagick lib32ncurses5-dev lib32readline6-dev lib32z1-dev libesd0-dev
liblz4-tool \  
libncurses5-dev libsdl1.2-dev libwxgtk3.0-dev libxml2 libxml2-utils lzop
pngcrush schedtool \  
squashfs-tools xsltproc zip zlib1g-dev \  
python openjdk-8-jdk ccache sudo megatools gcc-4.9 libstdc++6  
  
# Clean up APT when done. [Phusion]  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Download Repo  
ADD https://commondatastorage.googleapis.com/git-repo-downloads/repo
/usr/local/bin/  
RUN chmod 755 /usr/local/bin/*  
  
# Fix libfl.so.2.0.0 for uber toolchains  
RUN megadl 'https://mega.nz/#!FdFXkaQR!fGmtpzqveIlZMmqzkSst-
htQJbqo33Z6ZYZZF_iHV_4'  
RUN mv libfl.so.2.0.0 /usr/lib/libfl.so.2.0.0  
RUN chmod 755 /usr/lib/libfl.so.2.0.0  
RUN ln -s /usr/lib/libfl.so.2.0.0 /usr/lib/libfl.so --force  
RUN ln -s /usr/lib/libfl.so.2.0.0 /usr/lib/libfl.so.2 --force  
RUN ln -s /usr/lib/libfl.so.2.0.0 /usr/lib/x86_64-linux-gnu/libfl.so.2 --force  
  
# Switch to the new user by default and make ~/ the working dir  
ENV USER build  
WORKDIR /home/${USER}/  
  
# Add the build user, update password to build and add to sudo group  
RUN useradd --create-home ${USER} && echo "${USER}:${USER}" | chpasswd &&
adduser ${USER} sudo  
  
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

