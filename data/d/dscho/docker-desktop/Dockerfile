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
FROM stackbrew/ubuntu:13.10  
MAINTAINER Roberto G. Hashioka "roberto_hashioka@hotmail.com"  
RUN apt-get update  
  
# Set the env variable DEBIAN_FRONTEND to noninteractive  
ENV DEBIAN_FRONTEND noninteractive  
  
# Installing the environment required: xserver, flux box, roc-filer and ssh  
RUN apt-get install -y xpra rox-filer ssh xserver-xorg-video-dummy fluxbox  
  
# Configuring ssh to allow X11 Forwarding.  
RUN echo X11Forwarding yes >> /etc/ssh/ssh_config  
  
## Upstart and DBus have issues inside docker. We work around in order to
install firefox.  
#RUN dpkg-divert --local --rename --add /sbin/initctl && ln -s /bin/true
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
  
# Create the directory needed to run the dbus daemon  
RUN mkdir /var/run/dbus  
  
# Create the directory needed to run the sshd daemon  
RUN mkdir /var/run/sshd  
  
# Allow non-root to connect via ssh  
RUN rm -f /etc/nologin  
  
# Make login uid optional  
RUN sed -i '/pam_loginuid/s/required/optional/' /etc/pam.d/sshd  
  
# Add docker user  
RUN useradd -m -d /home/docker -s /bin/bash -G adm,sudo docker  
  
# Upgrade xpra and Xdummy  
ADD http://winswitch.org/gpg.asc /root/winswitch.org.gpg.asc  
RUN apt-key add /root/winswitch.org.gpg.asc  
RUN echo "deb http://winswitch.org/ saucy main" >
/etc/apt/sources.list.d/winswitch.list  
RUN apt-get update  
RUN apt-get install -y xpra xserver-xorg-video-dummy  
  
# Install the gnome desktop so that gnome-terminal is available  
RUN apt-get install -y gnome-desktop-environment  
  
# Install socat for experimenting with unix sockets  
RUN apt-get install socat  
  
# Copy the files into the container  
ADD config/ /home/docker  
  
EXPOSE 22  
# Start dbus, ssh and Xpra services.  
CMD rsyslogd && dbus-daemon --system --fork && /usr/sbin/sshd && su -c
"./docker-desktop" -l docker && bash --login -i  

