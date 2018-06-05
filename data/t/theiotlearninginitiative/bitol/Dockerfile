FROM ubuntu:16.04  
MAINTAINER Abraham Arce <xe1gyq@gmail.com>  
  
ENV TIMEZONE America/Mexico_City  
ENV USER root  
  
# RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN groupadd user && \  
useradd -g user -s /bin/bash -d /home/user -m user && \  
( umask 226 && echo "user ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/50_user )  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y tightvncserver && \  
apt-get install -y --no-install-recommends ubuntu-desktop && \  
apt-get install -y gnome-panel gnome-settings-daemon metacity nautilus gnome-
terminal && \  
rm -rf /var/lib/apt/lists/*  
RUN mkdir /root/.vnc  
  
ADD xstartup /root/.vnc/xstartup  
ADD passwd /root/.vnc/passwd  
  
RUN chmod 600 /root/.vnc/passwd  
# RUN useradd -ms /bin/bash user  
# USER user  
# WORKDIR /home/user  
# CMD ["bash"]  
CMD /usr/bin/vncserver :1 -geometry 1280x800 -depth 24 && tail -f
/root/.vnc/*:1.log  
  
EXPOSE 5901  

