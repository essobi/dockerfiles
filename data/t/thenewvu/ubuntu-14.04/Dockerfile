FROM ubuntu:14.04  
MAINTAINER Vu Le "thenewvu@gmail.com"  
USER root  
  
# create a non-root user and it's home directory.  
# this use doesn't need to enter password when running commands with sudo.  
RUN useradd -m vu && \  
echo "vu ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/90-cloudimg-ubuntu  
  
# work under the non-root user from now.  
# all dockerfiles inherits from this will run all it's commands under this
user as well.  
USER vu  
  
# setup a nearby package repository (Viet Nam)  
RUN sudo sed -i "s/archive.ubuntu.com/opensource.xtdv.net/g"
/etc/apt/sources.list && \  
sudo apt-get update  
  
# install some utility packages  
RUN sudo apt-get install -y --no-install-recommends software-properties-common
\  
wget  
  
# clean up apt cached stuffs  
RUN sudo apt-get clean && \  
sudo rm -rf /var/lib/apt/lists/*  
  
# setup all locales to en_US.UTF-8  
RUN sudo locale-gen --no-purge en_US.UTF-8 && \  
sudo update-locale LANG=en_US.UTF-8 && \  
sudo dpkg-reconfigure locales  
  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# set timezone to Asia/Phnom_Penh  
RUN echo Asia/Phnom_Penh | sudo tee /etc/timezone && sudo dpkg-reconfigure
--frontend noninteractive tzdata  
  
# set up bashrc and source it at container start up  
COPY .bashrc /home/vu/.bashrc

