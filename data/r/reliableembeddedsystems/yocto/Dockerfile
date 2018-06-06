#  
# yocto Dockerfile  
#  
# https://github.com/RobertBerger/yocto  
#  
# Pull base image.  
FROM reliableembeddedsystems/ubuntu-base:pyro-2017-05-29  
#FROM reslocal/ubuntu-base  
# Ubuntu and Debian Yocto dependencies:  
# The essential and graphical support packages (older) you need for a
supported Ubuntu or Debian distribution are shown in the following command:  
RUN sudo apt-get install -y gawk wget git-core diffstat unzip texinfo gcc-
multilib build-essential chrpath libsdl1.2-dev xterm  
  
# Essentials (Morty) Packages needed to build an image on a headless system:  
RUN sudo apt-get install -y gawk wget git-core diffstat unzip texinfo gcc-
multilib build-essential chrpath socat cpio python python3 python3-pip
python3-pexpect xz-utils debianutils  
  
# qemu dependencies  
RUN sudo apt-get install -y iptables  
  
# u-boot might need this e.g. for imx28  
RUN sudo apt-get install -y libssl-dev  
  
# kernel compilation rpi needs this  
RUN sudo apt-get install -y bc libncursesw5-dev  
  
# Y-AB/bitbake complain  
RUN sudo apt-get install -y cpio  
  
# Y-AB ping missing  
RUN sudo apt-get install -y iputils-ping  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  

