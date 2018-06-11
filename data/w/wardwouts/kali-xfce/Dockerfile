FROM kalilinux/kali-linux-docker:latest  
  
MAINTAINER Ward Wouts <ward@wouts.nl>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm-256color  
  
# Bring Kali up-to-date  
RUN rm -fR /var/lib/apt/  
RUN apt-get clean  
RUN apt-get update -y  
RUN apt-get upgrade -y  
RUN apt-get install -y software-properties-common && apt-get update -y  
  
RUN apt-get install -y git colordiff colortail unzip vim tmux xterm zsh curl
telnet strace ltrace tmate mlocate  
  
# Install a vnc server & openbox  
RUN apt-get install -y tigervnc-standalone-server openssh-server supervisor
xfce4 xfce4-places-plugin xfce4-goodies extra-xdg-menus  
  
# Install noVNC  
RUN apt-get -y install net-tools python python-numpy  
RUN cd /root && git clone https://github.com/kanaka/noVNC.git  
RUN cd /root/noVNC/utils && git clone https://github.com/kanaka/websockify
websockify  
RUN ln -s /root/noVNC/vnc.html /root/noVNC/index.html  
  
# Add Kali tools  
RUN apt-get install -y kali-linux-full --fix-missing  
# RUN apt-get install -y kali-linux-top10 --fix-missing  
# Add startup script  
ADD startup.sh /startup.sh  
RUN chmod 0755 /startup.sh  
  
ADD supervisord.conf /  
ADD root /root/  
  
RUN apt-get -y autoremove  
  
# Unzip rockyou if installed  
RUN if [ -e /usr/share/wordlists/rockyou.txt.gz ]; then cd
/usr/share/wordlists && gunzip rockyou.txt.gz ; fi  
  
# Kali stuff should end up in the menu's. Unfortunately this takes some
effort.  
RUN apt-get -y install menu-xdg  
RUN apt-get -y install --reinstall kali-menu  
RUN update-menus  
  
#RUN rm -rf /var/lib/apt/lists/*  
# Make locate work  
RUN updatedb  
  
EXPOSE 5900  
EXPOSE 6080  
EXPOSE 22  
ENTRYPOINT ["/startup.sh"]  

