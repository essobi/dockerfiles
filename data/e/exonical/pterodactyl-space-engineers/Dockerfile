FROM ubuntu:16.04  
  
MAINTAINER Bryce Anglin, <brycea@rapidnetworks.org>  
# Install Dependencies  
RUN dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get install -y \--no-install-recommends apt-transport-https software-
properties-common wget \  
&& wget -nc --no-check-certificate https://dl.winehq.org/wine-
builds/Release.key \  
&& apt-key add Release.key \  
&& apt-add-repository https://dl.winehq.org/wine-builds/ubuntu/ \  
&& apt-get update \  
&& wget
https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks
\  
&& chmod +x winetricks \  
&& cp winetricks /usr/local/bin \  
&& apt-get install -y \--no-install-recommends apt-utils winehq-stable x11vnc
xvfb cabextract p7zip zenity winbind python unzip \  
&& apt-get upgrade -y \  
&& WINEARCH=win32 winecfg \  
&& winetricks -q dotnet40 \  
&& winetricks -q msxml3 \  
&& useradd -m -d /home/container container \  
&& mkdir /home/container/drive_c \  
&& ln -s ~/.wine /home/container/drive_c  
  
RUN mkdir ~/.vnc \  
&& x11vnc -storepasswd 1234 ~/.vnc/passwd  
  
RUN winecfg && wine cmd.exe /c echo '%ProgramFiles%' && sleep 5  
  
ENV WINEPREFIX /home/container/.wine  
ENV WINEARCH win32  
  
USER container  
ENV HOME /home/container  
WORKDIR /home/container  
  
COPY ./entrypoint.sh /entrypoint.sh  
CMD ["/bin/bash", "/entrypoint.sh"]  

