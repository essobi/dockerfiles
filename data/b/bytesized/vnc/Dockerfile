FROM bytesized/debian-base  
MAINTAINER maran@bytesized-hosting.com  
  
RUN mkdir -p /data /config/.vnc && \  
apt-get clean && apt-get update && \  
apt-get install -y xvfb xauth tightvncserver xfce4-goodies xfce4 git gnome-
icon-theme picard handbrake iceweasel net-tools && \  
mkdir /app && git clone \--depth 1 git://github.com/kanaka/noVNC /app/novnc  
  
VOLUME /data /config  
  
COPY /static /  
COPY /files/ /app/  
  
EXPOSE 5900 6080  

