FROM ubuntu:latest  
MAINTAINER Fabiano Menegidio  
  
RUN apt-get update -y  
RUN apt-get upgrade -y  
  
# Set the env variable DEBIAN_FRONTEND to noninteractive  
ENV DEBIAN_FRONTEND noninteractive  
  
# Installing the environment required: xserver, xdm, flux box, roc-filer and
ssh  
RUN apt-get install -y xpra rox-filer openssh-server pwgen xserver-xephyr xdm
fluxbox xvfb sudo git \  
&& sed -i 's/DisplayManager.requestPort/!DisplayManager.requestPort/g'
/etc/X11/xdm/xdm-config \  
&& sed -i '/ \  
&& ln -s /usr/bin/Xorg /usr/bin/X \  
&& echo X11Forwarding yes >> /etc/ssh/ssh_config \  
&& sed -i 's/session required pam_loginuid.so/ \  
&& dpkg-divert --local --rename --add /sbin/initctl && ln -sf /bin/true
/sbin/initctl \  
&& apt-get -y install fuse || : \  
&& rm -rf /var/lib/dpkg/info/fuse.postinst \  
&& apt-get -y install fuse \  
&& apt-get install -y xterm \  
&& localedef -v -c -i en_US -f UTF-8 en_US.UTF-8 || :  
  
ADD . /src  
EXPOSE 22  
CMD ["/bin/bash", "/src/startup.sh"]  

