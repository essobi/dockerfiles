FROM debian:stretch  
MAINTAINER Julian Haupt <julian.haupt@hauptmedia.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -qq && \  
apt-get install wget ca-certificates xterm fluxbox eterm supervisor curl
chromium xvfb x11vnc gnupg unzip \  
-y --no-install-recommends && \  
apt-get --reinstall install xfonts-base -y && \  
apt-get clean autoclean && \  
apt-get autoremove --yes && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
#install nodejs  
RUN (curl -L https://deb.nodesource.com/setup_7.x | bash -) && \  
apt-get install -y nodejs && \  
ln -s /usr/bin/nodejs /usr/local/bin/node  
  
ADD novnc /opt/novnc  
  
RUN cd /opt/novnc && npm install  
  
ENV DISPLAY :99  
ENV SCREEN_SIZE 1280x1024  
  
ENV VNC_PASSWORD changeme  
  
ADD chromium-run /usr/local/bin/chromium-run  
ADD etc/supervisor/conf.d/ /etc/supervisor/conf.d/  
  
CMD ["/usr/bin/supervisord"]  
  

