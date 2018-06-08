FROM ubuntu:14.04  
MAINTAINER Albert Alvarez "albert@alvarezbruned.com"  
ENV DEBIAN_FRONTEND noninteractive  
ENV DISPLAY :1  
ENV VNC_COL_DEPTH 24  
ENV VNC_RESOLUTION 1280x1024  
ENV VNC_PW vncpassword  
ENV INSTALL ""  
############### xvnc / xfce installation  
RUN apt-get update && apt-get upgrade -y && apt-get install -y supervisor nano
vnc4server wget  
  
# xvnc server porst, if $DISPLAY=:1 port will be 5901  
EXPOSE 5901  
COPY vnc_startup.sh /root  
RUN mkdir /root/scripts  
COPY scripts/* /root/scripts/  
  
RUN mkdir /root/java  
  
RUN chmod +x /etc/X11/xinit/xinitrc /root/*.sh /root/scripts/*  
  
ENTRYPOINT ["/root/vnc_startup.sh"]  
CMD ["--tail-log"]  

