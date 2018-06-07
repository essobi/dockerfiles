# This file creates a container that runs X11 and SSH services  
# The ssh is used to forward X11 and provide you encrypted data  
# communication between the docker container and your local  
# machine.  
#  
# Xpra allows to display the programs running inside of the  
# container such as Firefox, LibreOffice, xterm, etc.  
# with disconnection and reconnection capabilities  
#  
# Author: Rob Nelson guruvan@maza.club  
# Based on work by: Roberto Gandolfo Hashioka  
# Date: 07/28/2013  
FROM guruvan/desktop-base  
# IMAGE guruvan/desktop-gui  
MAINTAINER Rob Nelson "guruvan@maza.club"  
# FORKED FROM: Roberto G. Hashioka "roberto_hashioka@hotmail.com"  
RUN apt-get install -y xdm Xorg xserver-xorg-video-dummy  
  
RUN apt-get install -y imagemagick git-all default-jre default-jdk  
  
RUN apt-get install -y firefox xterm mrxvt \  
nautilus nautilus-pastebin nautilus-compare nautilus-actions \  
seahorse-nautilus seahorse deluge \  
bluefish meld diffuse xpra \  
pinentry-gtk2 xpad vim-gtk  
  
RUN apt-get install -y pidgin pidgin-otr pidgin-hotkeys \  
pidgin-guifications pidgin-twitter pidgin-themes \  
pidgin-openpgp  
  
RUN apt-get install -y chromium-browser  
  
# Configuring xdm to allow connections from any IP address and ssh to allow
X11 Forwarding.  
RUN sed -i 's/DisplayManager.requestPort/!DisplayManager.requestPort/g'
/etc/X11/xdm/xdm-config  
RUN sed -i '/#any host/c\\*' /etc/X11/xdm/Xaccess  
#RUN ln -s /usr/bin/Xorg /usr/bin/X  
RUN echo X11Forwarding yes >> /etc/ssh/ssh_config  
  
# Wine  
RUN add-apt-repository -y ppa:ubuntu-wine/ppa \  
&& dpkg --add-architecture i386 \  
&& apt-get update -y \  
&& apt-get upgrade -y \  
&& apt-get install -y wine1.7 winbind winetricks  
  
# Liclipse IDE (use eclipse +liclipse plugins instead)  
#RUN wget
https://googledrive.com/host/0BwwQN8QrgsRpLVlDeHRNemw3S1E/LiClipse%201.4.0/liclipse_1.4.0_linux.gtk.x86_64.tar.gz  
#RUN if [ "$(md5sum liclipse_1.4.0_linux.gtk.x86_64.tar.gz|awk '{print $1}')"
= "ce65311d12648a443f557f95b8e0fd59" ]; then tar -xpzvf
liclipse_1.4.0_linux.gtk.x86_64.tar.gz; fi  
# smartgit  
#RUN wget http://www.syntevo.com/downloads/smartgit/smartgit-6_5_7.deb  
# .deb file is a mess, do not use - installs to /usr/share?? dafuq  
RUN wget http://www.syntevo.com/downloads/smartgit/smartgit-
generic-6_5_7.tar.gz  
  
RUN if [ "$(md5sum smartgit-generic-6_5_7.tar.gz|awk '{print $1}')" =
"02b7216dd643d929049a2382905a24f7" ]; then mv smartgit-generic-6_5_7.tar.gz
/opt && cd /opt && tar -xpzvf smartgit-generic-6_5_7.tar.gz && ln -s
/opt/smartgit/bin/smartgit.sh /usr/local/bin/smartgit ; fi  
  
# eclipse kepler base  
RUN wget
http://mirrors.ibiblio.org/pub/mirrors/eclipse/technology/epp/downloads/release/kepler/SR2/eclipse-
standard-kepler-SR2-linux-gtk-x86_64.tar.gz  
RUN if [ "$(sha512sum eclipse-standard-kepler-SR2-linux-gtk-x86_64.tar.gz|awk
'{print $1}')" =
"38d53d51a9d8d2fee70c03a3ca0efd1ca80d090270d41d6f6c7d8e66b118d7e5c393c78ed5c7033a2273e10ba152fa8eaf31832e948e592a295a5b6e7f1de48f"
]; then test -d /opt || mkdir /opt && mv eclipse-standard-kepler-SR2-linux-
gtk-x86_64.tar.gz /opt && cd /opt && tar -xpzvf eclipse-standard-kepler-
SR2-linux-gtk-x86_64.tar.gz ; fi  
  
# liclipse update dl  
RUN wget
https://googledrive.com/host/0BwwQN8QrgsRpLVlDeHRNemw3S1E/LiClipse%201.4.0/UPDATE%20SITE%201.4.0.zip
\  
&& mv UPDATE\ SITE\ 1.4.0.zip /liclipse-UPDATE-SITE-1.4.0.zip  
  
RUN if [ "$(md5sum liclipse-UPDATE-SITE-1.4.0.zip |awk '{print $1}')" =
"42b470979959bdf0b6784e9e732f27ce" ]; then unzip liclipse-UPDATE-
SITE-1.4.0.zip; fi  
  
# Install pexpect for the cert script (it's handy too!)  
# Install pydev cert & liclipse plugins  
COPY . /  
#RUN pip install pexpect  
RUN /usr/local/bin/install_pydev_cert.sh \  
&& /usr/local/bin/install_pydev_plugin.sh  
  
#########################################  
# Set locale (fix the locale warnings)  
RUN localedef -v -c -i en_US -f UTF-8 en_US.UTF-8 || :  
  
# Copy the files into the container  
COPY . /src  
EXPOSE 22 9000  
# Start xdm and ssh services.  
CMD ["/bin/bash", "/src/startup.sh"]  

