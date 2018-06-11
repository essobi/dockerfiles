#  
# crosstool-NG Dockerfile  
#  
# https://github.com/walkerlee/dockerfile-crosstool-NG  
#  
# Pull base image.  
FROM ubuntu:14.04  
MAINTAINER Walker Lee <walkerlee.tw@gmail.com>  
  
# Install.  
RUN \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y wget bash-completion subversion && \  
apt-get install -y build-essential gperf bison flex texinfo gawk libtool
automake libncurses5-dev libexpat1-dev python-dev && \  
rm -rf /var/lib/apt/lists/*  
  
# Install crosstool-NG.  
RUN \  
wget http://crosstool-ng.org/download/crosstool-ng/crosstool-ng-1.20.0.tar.bz2
&& \  
tar xf crosstool-ng-*.tar.* && \  
cd crosstool-ng-* && \  
./configure && \  
make install && \  
cp ct-ng.comp /etc/bash_completion.d/ && \  
rm -rf ../crosstool-ng-*  
  
# Set environment variables.  
ENV USER crosstool-ng  
ENV HOME /home/$USER  
# Create new user  
RUN \  
useradd -m $USER && \  
echo "$USER ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/$USER  
  
# Define user name.  
USER $USER  
# Define working directory.  
WORKDIR $HOME  
  
# Define default command.  
CMD ["bash"]  

