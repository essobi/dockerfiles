# This Dockerfile is used to build an image containing basic stuff to be used
as a Jenkins slave build node.  
FROM tanglu/tanglu:chromodoris  
MAINTAINER Matthias Klumpp <mak@debian.org>  
  
# Make sure the image is up-to-date  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Install OpenSSH, JDK 8, sudo and some other stuff for Jenkins  
RUN apt-get -y install build-essential openjdk-8-jdk sudo openssh-client
openssh-server  
  
# Install dependencies needed for the tests  
RUN apt-get -y install konsole cppcheck transifex-client git  
  
# Install Calamares dependencies  
RUN apt-get -y install cmake debhelper extra-cmake-modules gettext
libatasmart-dev libboost-python-dev \  
libkf5config-dev libkf5coreaddons-dev libkf5i18n-dev libkf5solid-dev
libparted-dev \  
libpolkit-qt5-1-dev libqt5svg5-dev libyaml-cpp-dev os-prober pkg-config pkg-
kde-tools \  
python3-dev qtbase5-dev qtdeclarative5-dev qttools5-dev qttools5-dev-tools
libqt5webkit5-dev \  
libkf5parts-dev libkf5service-dev libkf5iconthemes-dev kio-dev  
  
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

