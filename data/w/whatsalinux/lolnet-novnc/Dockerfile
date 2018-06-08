FROM ubuntu:16.04  
MAINTAINER whatsalinux  
RUN apt-get -yy update  
RUN apt-get -y install --install-recommends unzip sudo libfuse2 libx11-6
libx11-xcb1 libfontconfig1 supervisor xvfb x11vnc software-properties-common
openbox xterm libvncclient1 net-tools  
RUN addgroup novnc  
RUN useradd -m -d /home/novnc -s /bin/bash -g novnc novnc  
RUN echo "novnc:novnc" | /usr/sbin/chpasswd  
RUN echo "novnc ALL=(ALL) ALL" >> /etc/sudoers  
ADD noVNC.zip /home/novnc/noVNC.zip  
ADD create_novnc_init.sh /home/novnc/create_novnc_init.sh  
ADD menu_test.sh /bin/menu_test  
RUN chmod 755 /home/novnc/create_novnc_init.sh  
RUN unzip -n /home/novnc/noVNC.zip -d /home/novnc/  
RUN mkdir -p /home/novnc/config  
ADD supervisord.conf /home/novnc/supervisord.conf.backup  
ADD menu.xml /home/novnc/menu.xml.backup  
RUN chown novnc:novnc -R /home/novnc/menu.xml.backup
/home/novnc/supervisord.conf.backup /home/novnc/noVNC
/home/novnc/create_novnc_init.sh  
ADD start /bin/start  
USER novnc  
CMD ["/home/novnc/create_novnc_init.sh"]  
USER root  
CMD ["/bin/menu_test"]  
USER novnc  
ENV DISPLAY :1  
EXPOSE 5909  
CMD ["/bin/start"]  

