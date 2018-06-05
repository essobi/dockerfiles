#  
# Dockerfile for based games servers on LinuxGSM install scripts  
#  
# @see https://github.com/GameServerManagers/LinuxGSM  
#  
FROM ubuntu:14.04  
MAINTAINER Antoine Benevaut <antoine@bellum-industria.fr>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install Packages / Dependencies  
RUN dpkg --add-architecture i386 && apt-get update -y && apt-get upgrade -y &&
\  
apt-get install -qqy curl wget nano tmux mailutils postfix lib32gcc1 \  
gdb ca-certificates bsdmainutils unzip binutils libstdc++6:i386 \  
mysql-common bc  
  
RUN wget --no-check-certificate
https://ftp.de.debian.org/debian/pool/main/m/mariadb-client-
lgpl/libmariadb2_2.0.0-1_amd64.deb  
RUN dpkg -i libmariadb2_2.0.0-1_amd64.deb  
  
# FIX ( perl: warning: Please check that your locale settings: )  
# http://ubuntuforums.org/showthread.php?t=1346581  
RUN locale-gen en_US en_US.UTF-8 hu_HU hu_HU.UTF-8  
RUN dpkg-reconfigure locales  
  
# Cleanup  
RUN apt-get clean && \  
rm -fr /var/lib/apt/lists/* && \  
rm -fr /tmp/*  

