FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y curl apt-transport-https x11vnc xvfb  
  
RUN dpkg --add-architecture i386  
  
RUN curl https://dl.winehq.org/wine-builds/Release.key | apt-key add -  
  
RUN echo "deb https://dl.winehq.org/wine-builds/debian/ jessie main" >
/etc/apt/sources.list.d/wine.list  
  
RUN apt-get update && apt-get install -y --install-recommends winehq-devel  
  
RUN mkdir -p /usr/share/wine/mono /usr/share/wine/gecko  
  
RUN curl -o /usr/share/wine/mono/wine-mono-4.6.4.msi
http://dl.winehq.org/wine/wine-mono/4.6.4/wine-mono-4.6.4.msi  
  
RUN curl -o /usr/share/wine/gecko/wine_gecko-2.47-x86.msi
http://dl.winehq.org/wine/wine-gecko/2.47/wine_gecko-2.47-x86.msi  
  
RUN curl -o /usr/share/wine/gecko/wine_gecko-2.47-x86_64.msi
http://dl.winehq.org/wine/wine-gecko/2.47/wine_gecko-2.47-x86_64.msi  
  
RUN curl -o /usr/bin/winetricks
https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks
&& chmod +x /usr/bin/winetricks  
  
RUN echo 'Xvfb $DISPLAY -screen 0 1024x768x24 &' >> /root/.bashrc  
  
RUN echo 'x11vnc -forever -display $DISPLAY -bg -nopw -listen 0.0.0.0 -xkb' >>
/root/.bashrc  
  
ENV DISPLAY :1  
WORKDIR /root  

