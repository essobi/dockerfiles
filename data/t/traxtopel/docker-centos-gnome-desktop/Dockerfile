FROM traxtopel/centos  
MAINTAINER Grant Williamson <traxtopel@gmail.com>  
  
RUN echo tolerant=1 >> /etc/yum.conf  
RUN yum localinstall -y http://dl.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm  
RUN setarch i386 yum install -y tigervnc-server openssh-server sudo vim-
minimal which supervisor net-tools xorg-x11-server-Xvfb shadow-utils
xorg-x11-fonts-Type1 xorg-x11-fonts-misc dejavu-lgc-sans-fonts
xorg-x11-fonts-75dpi xorg-x11-fonts-100dpi xterm gnome-panel gnome-terminal
gnome-applets nautilus firefox libreoffice thunderbird ; setarch i386 yum
clean all  
  
# noVNC  
ADD noVNC /noVNC/  
ADD home /home/  
ADD startup.sh /  
ADD supervisord.conf /  
  
EXPOSE 6080  
EXPOSE 5900  
EXPOSE 3000  
EXPOSE 22  
WORKDIR /  
ENTRYPOINT ["/startup.sh"]  

