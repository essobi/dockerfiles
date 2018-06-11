# Run Wireshark in a container  
FROM ubuntu:xenial  
MAINTAINER Andrey Arapov <andrey.arapov@nixaid.com>  
  
# To avoid problems with Dialog and curses wizards  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get -y --no-install-recommends install \  
ca-certificates wireshark && \  
rm -rf -- /var/lib/apt/lists  
  
ENV USER user  
ENV UID 1000  
ENV HOME /home/$USER  
ENV LC_ALL C.UTF-8  
RUN useradd -u $UID -m -d $HOME -s /usr/sbin/nologin $USER  
  
# Allow a non-privileged user to use the wireshark  
# https://wiki.wireshark.org/CaptureSetup/CapturePrivileges  
RUN setcap 'CAP_NET_RAW+eip CAP_NET_ADMIN+eip' /usr/bin/dumpcap  
  
USER $USER  
WORKDIR $HOME  
ENTRYPOINT [ "wireshark" ]  
  
# Just an alternative way to start wireshark  
# RUN echo "$USER ALL=NOPASSWD:SETENV:/usr/bin/wireshark" | tee
/etc/sudoers.d/$USER  
# ENTRYPOINT [ "sudo", "-E", "wireshark" ]  
# xhost +; wireshark; xhost -  

