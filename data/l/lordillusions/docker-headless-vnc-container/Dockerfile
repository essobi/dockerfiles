# This Dockerfile is used to build an headles vnc image based on Ubuntu  
FROM ubuntu:14.04  
MAINTAINER Wellington Chaves "lordillusions@gmail.com"  
ENV REFRESHED_AT 2017-01-23  
LABEL io.k8s.description="Headless VNC Container with Xfce window manager,
firefox and chromium" \  
io.k8s.display-name="Headless VNC Container based on Ubuntu" \  
io.openshift.expose-services="5901:xvnc" \  
io.openshift.tags="vnc, ubuntu, xfce" \  
io.openshift.non-scalable=true  
  
## Connection ports for controlling the UI:  
# VNC port:5901  
ENV DISPLAY :1  
ENV VNC_PORT 5901  
EXPOSE $VNC_PORT  
  
#ENV HOME /headless  
#WORKDIR $HOME  
### Envrionment config  
ENV DEBIAN_FRONTEND noninteractive  
ENV VNC_COL_DEPTH 24  
ENV VNC_RESOLUTION 1280x1024  
ENV VNC_PW vncpassword  
  
### Add all install scripts for further steps  
#ENV INST_SCRIPTS $HOME/install  
#ADD ./src/common/install/ $INST_SCRIPTS/  
#ADD ./src/ubuntu/install/ $INST_SCRIPTS/  
#RUN find $INST_SCRIPTS -name '*.sh' -exec chmod a+x {} +  
### Install some common tools  
#RUN $INST_SCRIPTS/tools.sh  
### Install xvnc-server  
#RUN $INST_SCRIPTS/tigervnc.sh  
############### xvnc / xfce installation  
RUN apt-get update && apt-get upgrade -y && apt-get install -y supervisor vim
xfce4 vnc4server wget && rm -rf /var/lib/apt/  
  
### Install firfox  
RUN apt-get update \  
&& apt-get install -y firefox \  
&& rm -rf /var/lib/apt/  
  
# Inspired by monokrome/wine  
ENV WINE_MONO_VERSION 0.0.8  
USER root  
  
# Install some tools required for creating the image  
RUN apt-get update \  
&& apt-get install -y \  
curl \  
unzip \  
ca-certificates  
# Install wine and related packages  
RUN dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get install -y \  
wine \  
&& rm -rf /var/lib/apt/lists/*  
  
# Use the latest version of winetricks  
RUN curl -SL
'https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks'
-o /usr/local/bin/winetricks \  
&& chmod +x /usr/local/bin/winetricks  
  
# Get latest version of mono for wine  
RUN mkdir -p /usr/share/wine/mono \  
&& curl -SL
'http://sourceforge.net/projects/wine/files/Wine%20Mono/$WINE_MONO_VERSION/wine-
mono-$WINE_MONO_VERSION.msi/download' -o /usr/share/wine/mono/wine-
mono-$WINE_MONO_VERSION.msi \  
&& chmod +x /usr/share/wine/mono/wine-mono-$WINE_MONO_VERSION.msi  
  
# Wine really doesn't like to be run as root, so let's use a non-root user
USER xclient ENV HOME /home/xclient ENV WINEPREFIX /home/xclient/.wine ENV
WINEARCH win32 # Use xclient's home dir as working dir WORKDIR /home/xclient  
RUN echo "alias winegui='wine explorer /desktop=DockerDesktop,1024x768'" >
~/.bash_aliases  
  
ADD .vnc /root/.vnc  
ADD .config /root/.config  
ADD Desktop /root/Desktop  
ADD scripts /root/scripts  
RUN chmod +x /root/.vnc/xstartup /etc/X11/xinit/xinitrc /root/scripts/*.sh
/root/Desktop/*.desktop  
ENTRYPOINT ["/root/scripts/vnc_startup.sh"]  
CMD ["--tail-log"]  
  

