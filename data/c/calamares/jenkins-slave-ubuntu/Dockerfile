# This Dockerfile is used to build an image containing basic stuff to be used
as a Jenkins slave build node.  
FROM ubuntu:xenial  
MAINTAINER Teo Mrnjavac <teo@kde.org>  
  
# Add neon repo for non-ancient Qt  
RUN apt-get update  
RUN apt-get -y install curl  
RUN echo "deb http://archive.neon.kde.org/user/ xenial main" >
/etc/apt/sources.list.d/neon.list  
RUN curl -LO http://archive.neon.kde.org/public.key  
RUN apt-key add public.key  
  
# Make sure the package repository is up to date.  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Install OpenSSH, JDK 8, sudo and a bunch of other stuff for Calamares.  
RUN apt-get -y install build-essential openjdk-8-jdk sudo debhelper cmake
extra-cmake-modules qtbase5-dev \  
libqt5svg5-dev libqt5quick5 qtdeclarative5-dev extra-cmake-modules
libkf5i18n-dev \  
libkf5solid-dev libkf5coreaddons-dev python3-dev libboost-python-dev os-prober
qttools5-dev \  
libparted-dev libkf5config-dev gettext libyaml-cpp-dev pkg-config libatasmart-
dev \  
pkg-kde-tools qttools5-dev-tools transifex-client git libpolkit-qt5-1-dev
openssh-client \  
libqt5webkit5-dev libkf5parts-dev libkf5service-dev konsole openssh-server
cppcheck \  
libpythonqt-dev  
  
# Set up sshd.  
RUN sed -i 's|session required pam_loginuid.so|session optional
pam_loginuid.so|g' /etc/pam.d/sshd  
RUN mkdir -p /var/run/sshd  
  
# Add user jenkins to the image.  
RUN adduser --quiet jenkins  
# Set password for the jenkins user (you may want to alter this).  
RUN echo "jenkins:jenkins" | chpasswd  
# Allow the jenkins user to update the system.  
RUN echo "jenkins ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/jenkins  
  
# Standard SSH port  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

