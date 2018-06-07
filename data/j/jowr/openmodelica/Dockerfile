# This file creates a container that runs X11 and SSH services  
# The ssh is used to forward X11 and provide you encrypted data  
# communication between the docker container and your local  
# machine.  
#  
# Xpra allows to display the programs running inside of the  
# container such as Firefox, LibreOffice, xterm, etc.  
# with disconnection and reconnection capabilities  
#  
# Xephyr allows to display the programs running inside of the  
# container such as Firefox, LibreOffice, xterm, etc.  
#  
# Fluxbox and ROX-Filer creates a very minimalist way to  
# manages the windows and files.  
#  
# Author: Roberto Gandolfo Hashioka  
# Date: 07/28/2013  
#  
# This is a Dockerfile that creates a docker image with all  
# the necessary dependencies for OpenModelica.  
# It is hevily inspired by Micheal Tiller's docker image  
# see -
https://github.com/xogeny/ModelicaBook/blob/master/docker/OM/Dockerfile  
# and by the docker-desktop images by Roberto Gandolfo Hashioka  
# see - https://github.com/rogaha/docker-desktop  
#  
FROM ubuntu  
MAINTAINER Jorrit Wronski (jowr@ipu.dk)  
  
# Set the env variable DEBIAN_FRONTEND to noninteractive  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update index and install wget  
RUN apt-get update && apt-get install -y wget  
  
# Installing the environment required: xserver, xdm, flux box, roc-filer and
ssh  
RUN apt-get install -y xpra rox-filer openssh-server pwgen xserver-xephyr xdm
fluxbox xvfb sudo  
  
# Configuring xdm to allow connections from any IP address and ssh to allow
X11 Forwarding.  
RUN sed -i 's/DisplayManager.requestPort/!DisplayManager.requestPort/g'
/etc/X11/xdm/xdm-config  
RUN sed -i '/#any host/c\\*' /etc/X11/xdm/Xaccess  
RUN ln -s /usr/bin/Xorg /usr/bin/X  
RUN echo X11Forwarding yes >> /etc/ssh/ssh_config  
  
# Fix PAM login issue with sshd  
RUN sed -i 's/session required pam_loginuid.so/#session required
pam_loginuid.so/g' /etc/pam.d/sshd  
  
# Upstart and DBus have issues inside docker. We work around in order to
install firefox.  
RUN dpkg-divert --local \--rename --add /sbin/initctl && ln -sf /bin/true
/sbin/initctl  
  
# Installing fuse package (libreoffice-java dependency) and it's going to try
to create  
# a fuse device without success, due the container permissions. || : help us
to ignore it.  
# Then we are going to delete the postinst fuse file and try to install it
again!  
# Thanks Jerome for helping me with this workaround solution! :)  
# Now we are able to install the libreoffice-java package  
RUN apt-get -y install fuse || :  
RUN rm -rf /var/lib/dpkg/info/fuse.postinst  
RUN apt-get -y install fuse  
  
# Installing the apps: Firefox, flash player plugin, LibreOffice and xterm  
# libreoffice-base installs libreoffice-java mentioned before  
RUN apt-get install -y libreoffice-base firefox libreoffice-gtk libreoffice-
calc xterm  
  
# Set locale (fix the locale warnings)  
RUN localedef -v -c -i en_US -f UTF-8 en_US.UTF-8 || :  
  
# Copy the files into the container  
ADD . /src  
  
EXPOSE 22  
# Start xdm and ssh services.  
CMD ["/bin/bash", "/src/startup.sh"]  
  
# Add OpenModelica stable build  
RUN for deb in deb deb-src; do echo "$deb http://build.openmodelica.org/apt
`lsb_release -cs` stable"; done | sudo tee
/etc/apt/sources.list.d/openmodelica.list  
RUN wget -q http://build.openmodelica.org/apt/openmodelica.asc -O- | sudo apt-
key add -  
  
# Update index (again) and install OpenModelica  
RUN apt-get update && apt-get install -y openmodelica  

