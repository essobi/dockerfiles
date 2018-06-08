# Run Simplicity Studio v4 from a container  
FROM ubuntu:14.04  
LABEL maintainer "Matthew W-S <matt.woodcock-smith@relectrify.com>"  
  
# Install build dependencies  
RUN dpkg --add-architecture i386  
RUN apt-get update \  
&& apt-get install -y git wget unzip python make  
  
RUN apt-get install lib32z1 lib32ncurses5 \  
libstdc++6:i386 libuuid1:i386 libc6-i386 libgtk2.0-0:i386 \  
libxtst6:i386 libusb-1.0-0:i386 libxt6:i386 libasound2:i386 \  
libdbus-glib-1-2:i386 libgl1-mesa-glx:i386 \  
libqtgui4:i386 libqt4-svg:i386 libusb-0.1-4:i386 \  
gtk2-engines-murrine:i386 \  
libelf1:i386 libphysfs1 libopenal1 libsdl-image1.2 \  
libsdl1.2debian libgles2-mesa-dev:i386 qtbase5-dev:i386 \  
default-jre libwebkitgtk-1.0-0 -y  
  
RUN apt-get install libgnome2-0 libbonobo2-0 liborbit2 libidl0 libidl-common
cpp cpp-4.8 libgnomeui-0 -y  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN mkdir -p /simplicity && cd /simplicity/  
RUN wget --load-cookies /tmp/cookies.txt
"https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-
cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate
'https://docs.google.com/uc?export=download&id=1r8a3mWAlxk-
CiCLLXpy2UPmuDcukIdt9' -O- | sed -rn 's/.*confirm=([0-9A-Za-
z_]+).*/\1\n/p')&id=1r8a3mWAlxk-CiCLLXpy2UPmuDcukIdt9" -O /simplicity/IDE.tar
&& rm -rf /tmp/cookies.txt  
RUN cd /simplicity/ && tar -xf IDE.tar  
ENV XDG_RUNTIME_DIR /tmp  
ENV PATH="/simplicity/SimplicityStudio_v4/support/common/wine/usr/bin:${PATH}"  
RUN mkdir -p /simplicity/Workspace  
RUN mkdir -p /root  
  
WORKDIR /simplicity/  
  

