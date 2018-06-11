# wine-base  
#  
# VERSION 0.0.1  
  
FROM ubuntu:16.04  
LABEL maintainer="allen7575@gmail.com"  
  
##  
## Ubuntu - Packages - Search  
##
https://packages.ubuntu.com/search?suite=xenial&section=all&arch=amd64&searchon=contents&keywords=Search  
##  
  
############  
# update package list  
############  
RUN apt update  
  
##############################  
#########################  
## install wine  
#########################  
##############################  
  
#  
# repository - How can I get apt to use a mirror close to me, or choose a
faster mirror? - Ask Ubuntu  
# https://askubuntu.com/questions/37753/how-can-i-get-apt-to-use-a-mirror-
close-to-me-or-choose-a-faster-mirror  
#  
# apt - Trouble downloading packages list due to a "Hash sum mismatch" error -
Ask Ubuntu  
# https://askubuntu.com/questions/41605/trouble-downloading-packages-list-due-
to-a-hash-sum-mismatch-error  
#  
# Because there is trouble in download due to "Hash sum mismatch" with default
mirror, change to other mirror  
#  
#RUN sed -i 's|archive.ubuntu.com|tw.archive.ubuntu.com|'
/etc/apt/sources.list && \  
# apt update  
  
  
#  
# How to Install Wine 2.0 Stable in Ubuntu 16.04, 14.04, 16.10 |
UbuntuHandbook  
# http://ubuntuhandbook.org/index.php/2017/01/install-
wine-2-0-ubuntu-16-04-14-04-16-10/  
#  
# Do following command before adding the PPA:  
#  
RUN apt install -y software-properties-common  
  
#  
# adding Ricotz’s PPA:  
# For 64-bit system, enable 32-bit architecture (if you haven’t already) via  
# sudo dpkg --add-architecture i386  
#  
# wine not initializing opengl - FedoraForum.org  
# https://forums.fedoraforum.org/showthread.php?t=231666  
#  
# err:wgl:X11DRV_WineGL_InitOpenglInfo couldn't initialize OpenGL, expect
problems  
#  
# This was because Wine is 32 bit and requires 32 bit OGL library (duh!)  
#  
RUN add-apt-repository -y ppa:ricotz/unstable && \  
dpkg --add-architecture i386 && \  
apt update && \  
apt install -y wine-stable  
  
#  
# WineHQ Forums • View topic - Error at launching game  
# https://forum.winehq.org/viewtopic.php?t=16162  
# Ierr:winediag:SECUR32_initNTLMSP ntlm_auth was not found or is outdated.
Make sure that ntlm_auth >= 3.0.25 is in your path. Usually, you can find it
in the winbind package of your distribution.  
#  
# Do what it says; install winbind. If you're not sure which package to
install, ask your distro.  
#  
RUN apt install -y winbind  
  
#  
# Wineskin: play your favorite Windows games on Mac OS X without needing
Microsoft Windows | Swords and Sandals: Crusader problems  
# http://wineskin.urgesoftware.com/tiki-
view_forum_thread.php?comments_parentId=3675  
#  
# _XSERVTransmkdir: ERROR: euid != 0,directory /tmp/.X11-unix will not be
created.  
#  
# 1\. mkdir /tmp/.X11-unix (make a directory)  
# 2\. sudo chmod a+rwx /tmp/.X11-unix (give it all rights)  
#  
RUN mkdir /tmp/.X11-unix && \  
chmod 1777 /tmp/.X11-unix  
  
  
##############################  
#########################  
## X11 GUI  
#########################  
##############################  
  
#############  
# install xeyes, xclock  
#############  
RUN apt install -y x11-apps  
  
###################  
# install VirtualGL  
###################  
# nvidia-virtualgl/Dockerfile at master · plumbee/nvidia-virtualgl  
# https://github.com/plumbee/nvidia-virtualgl/blob/master/Dockerfile  
  
#  
# install glxgears  
# How to Check 3D Acceleration (FPS) in Ubuntu/Linux Mint  
# http://www.upubuntu.com/2013/11/how-to-check-3d-acceleration-fps-in.html  
#  
# use following command to check  
# export LIBGL_DEBUG=verbose && glxgears  
#  
# How can i deal with 'libGL error: failed to load driver: swrast.' · Issue
#509 · openai/gym  
# https://github.com/openai/gym/issues/509  
#  
# Based on the dockerfile of nvidia/cuda, I can solve this problem.  
# https://gitlab.com/nvidia/cuda/blob/ubuntu16.04/8.0/runtime/Dockerfile  
#  
# Or you can just use it with nvidia-docker to create another container run
all the stuff without touching your OS environments.  
#  
# install mesa-utils for testing glxgear  
RUN apt install -y mesa-utils  
  
# install curl for download VirtualGL  
RUN apt install -y curl  
  
# download & install VirtualGL  
ENV VIRTUALGL_VERSION 2.5.2  
RUN curl -sSL
https://downloads.sourceforge.net/project/virtualgl/"${VIRTUALGL_VERSION}"/virtualgl_"${VIRTUALGL_VERSION}"_amd64.deb
-o virtualgl_"${VIRTUALGL_VERSION}"_amd64.deb && \  
dpkg -i virtualgl_*_amd64.deb && \  
rm virtualgl_*_amd64.deb  
  
# install libxv1 to avoid  
# glxgears: error while loading shared libraries: libXv.so.1: cannot open
shared object file: No such file or directory  
# when executed vglrun glxgears  
RUN apt install -y libxv1  
  
# Granting Access to the 3D X Server  
# https://cdn.rawgit.com/VirtualGL/virtualgl/2.5.2/doc/index.html#hd006001  
#RUN /opt/VirtualGL/bin/vglserver_config -config +s +f -t  
  
  
##############################  
#########################  
## nvidia-docker  
#########################  
##############################  
  
####################  
# nvidia-docker links  
####################  
# Image inspection · NVIDIA/nvidia-docker Wiki  
# https://github.com/NVIDIA/nvidia-docker/wiki/Image-inspection#nvidia-docker  
# when nvidia-docker run is used, we inspect the image specified on the
command-line. In this image,  
# we lookup the presence and the value of the label com.nvidia.volumes.needed  
  
# if you are using nvidia driver, you need to add this to avoid  
# libGL error: failed to load driver: swrast  
LABEL com.nvidia.volumes.needed="nvidia_driver"  
ENV PATH /usr/local/nvidia/bin:${PATH}  
ENV LD_LIBRARY_PATH
/usr/local/nvidia/lib:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH}  
  
# set PATH & LD_LIBRARY_PATH env variable for ssh login session  
# Env variable cannot be passed to container - General Discussions - Docker
Forums  
# https://forums.docker.com/t/env-variable-cannot-be-passed-to-
container/5298/6  
RUN echo 'export PATH=/usr/local/nvidia/bin:$PATH' >> /etc/profile.d/nvidia.sh
&& \  
echo 'export
LD_LIBRARY_PATH=/usr/local/nvidia/lib:/usr/local/nvidia/lib64:$LD_LIBRARY_PATH'
>> /etc/profile.d/nvidia.sh  
  
  
##############  
# upgrade  
##############  
RUN apt upgrade -y  
  
##############  
# cleanup  
##############  
# debian - clear apt-get list - Unix & Linux Stack Exchange  
# https://unix.stackexchange.com/questions/217369/clear-apt-get-list  
#  
# bash - autoremove option doesn't work with apt alias - Ask Ubuntu  
# https://askubuntu.com/questions/573624/autoremove-option-doesnt-work-with-
apt-alias  
#  
RUN apt-get autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
  
CMD ["bash"]

