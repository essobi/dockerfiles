FROM ubuntu:trusty  
MAINTAINER Cooper Maa <coopermaa77@gmail.com>  
  
ENV BR_VERSION 2015.02  
# Install Mandatory packages for buildroot, see: http://goo.gl/bmmWuE  
RUN DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install -y \  
curl wget build-essential libncurses-dev unzip bc rsync python git tree \  
syslinux genisoimage dnsutils qemu  
  
WORKDIR /tmp  
RUN wget -nv
http://buildroot.uclibc.org/downloads/buildroot-$BR_VERSION.tar.gz && \  
tar -zxf buildroot-$BR_VERSION.tar.gz && mv buildroot-$BR_VERSION buildroot &&
\  
rm buildroot-$BR_VERSION.tar.gz && \  
ln -s /tmp/buildroot /buildroot && \  
ln -s /tmp/buildroot/output/host/usr/bin /toolchain  
  
ENV PATH $PATH:/toolchain  
ENV TERM xterm-color  
ENV HOME /root  
  
WORKDIR /tmp/buildroot

