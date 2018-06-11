FROM sagu/ubuntu-gui:14.04  
ENV DEBIAN_FRONTEND noninteractive  
ENV WINE_MONO_VERSION 4.7.1  
ENV WINE_GECKO_VERSION 2.47  
RUN apt-get update && apt install sudo software-properties-common apt-
transport-https -y --no-install-recommends  
  
#RUN addgroup --system xusers  
RUN useradd --home /home/xclient -m --shell /bin/bash -U xclient && echo
"xclient:root" | chpasswd  
  
RUN usermod -a -G sudo xclient && echo "%sudo ALL=(ALL) NOPASSWD: ALL" >>
/etc/sudoers  
  
# Install packages required for connecting against X Server  
#RUN apt-get install -y --no-install-recommends \  
# xauth \  
# && rm -rf /var/lib/apt/lists/*  
USER root  
  
RUN apt-get -y update \  
&& DEBIAN_FRONTEND=${DEBIAN_FRONTEND} \  
&& apt-get -y install wget \  
&& mkdir -p /usr/share/wine/gecko \  
&& wget "http://dl.winehq.org/wine/wine-
gecko/${WINE_GECKO_VERSION}/wine_gecko-${WINE_GECKO_VERSION}-x86.msi" -O
/usr/share/wine/gecko/wine_gecko-${WINE_GECKO_VERSION}-x86.msi \  
&& chmod +x /usr/share/wine/gecko/wine_gecko-${WINE_GECKO_VERSION}-x86.msi \  
&& wget "http://dl.winehq.org/wine/wine-
gecko/${WINE_GECKO_VERSION}/wine_gecko-${WINE_GECKO_VERSION}-x86_64.msi" -O
/usr/share/wine/gecko/wine_gecko-${WINE_GECKO_VERSION}-x86_64.msi \  
&& chmod +x /usr/share/wine/gecko/wine_gecko-${WINE_GECKO_VERSION}-x86_64.msi
\  
&& mkdir -p /usr/share/wine/mono \  
&& wget "http://dl.winehq.org/wine/wine-mono/${WINE_MONO_VERSION}/wine-
mono-${WINE_MONO_VERSION}.msi" -O /usr/share/wine/mono/wine-
mono-${WINE_MONO_VERSION}.msi \  
&& chmod +x /usr/share/wine/mono/wine-mono-${WINE_MONO_VERSION}.msi \  
&& rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*  
  
# Install some tools required for creating the image  
RUN apt-get update && apt-get install -y --no-install-recommends \  
curl \  
unzip \  
dosbox \  
ca-certificates  
  
# Install wine and related packages  
RUN dpkg --add-architecture i386 \  
&& wget -nc https://dl.winehq.org/wine-builds/Release.key \  
&& apt-key add Release.key \  
&& apt-add-repository https://dl.winehq.org/wine-builds/ubuntu/ \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends winehq-stable  
  
RUN curl -O
https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks
&& chmod +x winetricks && sudo mv winetricks /usr/local/bin  
  
#-----------------------------------------------------------------------------  
# Cleanup Installation  
#-----------------------------------------------------------------------------  
RUN apt-get -y clean \  
&& rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*  
  
# Wine really doesn't like to be run as root, so let's use a non-root user  
USER xclient  
ENV HOME /home/xclient  
ENV WINEPREFIX /home/xclient/.wine  
ENV WINEARCH win32  
  
# Use xclient's home dir as working dir  
WORKDIR /home/xclient  
  
RUN sudo echo "alias winegui='wine explorer /desktop=DockerDesktop,1024x768'"
> ~/.bash_aliases  
# During startup we need to prepare connection to X11-Server container  
USER xclient  
ENTRYPOINT sudo /usr/sbin/sshd -D && echo If you want to run app as root use
sudo or login to root. password for both users is root && sudo apt-get update
-q

