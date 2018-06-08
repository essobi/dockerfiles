###################################  
## Docker file ##  
## ##  
## Ubuntu 14.04 AOSP Build ##  
###################################  
  
##################################################  
## Source: ##  
## http://source.android.com/source.index.html ##  
##################################################  
  
## Ubuntu Version  
FROM ubuntu:14.04  
  
MAINTAINER Reaver385 <reaverdroiddeveloper@gmail.com>  
RUN sed -i 's/main$/main universe/' /etc/apt/sources.list  
RUN dpkg --add-architecture i386  
RUN sudo apt update  
  
##14.04 Required Packages  
RUN apt -y install git-core gnupg flex bison gperf build-essential zip curl
zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386 lib32ncurses5-dev
x11proto-core-dev libx11-dev lib32z-dev ccache libgl1-mesa-dev libxml2-utils
unzip sudo mc tig tree git libx11-dev:i386 mingw32 tofrodos python-markdown  
  
COPY gitconfig /home/aosp/.gitconfig  
COPY ssh /home/aosp/.ssh/config  
  
##python-networkx packages  
RUN apt -y install python-networkx libnss-sss:i386  
  
# Java 7: for Lollipop through Marshmallow  
RUN echo "Installing JDK 7"  
RUN apt -y install openjdk-7-jdk  
#  
# Java 8:  
#RUN apt -y install openjdk-8-jdk  
  
#Update Java Alternative  
RUN update-alternatives --config java  
RUN update-alternatives --config javac  
  
RUN echo "Installing Additional Packages"  
RUN apt -y install bc lzop u-boot-tools  
  
ADD gitconfig /home/aosp/.gitconfig  
ADD ssh /home/aosp/.ssh/config  
  
RUN chmod 755 /home/aosp/.gitconfig  
  
## Installing Repo  
RUN echo "Installing Repo"  
ADD https://commondatastorage.googleapis.com/git-repo-downloads/repo
/usr/local/bin/  
RUN chmod 755 /usr/local/bin/*  
  
RUN id aosp 2>/dev/null || useradd --uid 30000 --create-home --shell /bin/bash
aosp  
RUN echo "aosp ALL=(ALL) NOPASSWD: ALL" | tee -a /etc/sudoers  
  
USER aosp  
WORKDIR /home/aosp  
CMD "/bin/bash"  
  
ENTRYPOINT "/bin/bash"  
  
  

