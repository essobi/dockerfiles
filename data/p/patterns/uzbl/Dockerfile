FROM ubuntu:zesty  
  
MAINTAINER 興怡  
ARG VNC_PASSWORD=secret  
ENV VNC_PASSWORD ${VNC_PASSWORD}  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y \  
supervisor \  
openssh-server \  
dbus-x11 x11-utils x11vnc xvfb \  
dwm suckless-tools dmenu stterm \  
uzbl \  
ca-certificates \  
&& apt-get autoclean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /etc/supervisor/conf.d \  
&& x11vnc -storepasswd $VNC_PASSWORD /etc/vncsecret \  
&& chmod 444 /etc/vncsecret  
COPY supervisord.conf /etc/supervisor/conf.d  
EXPOSE 5900  
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/conf.d/supervisord.conf"]  
  

