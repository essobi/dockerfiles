# Version: 0.0.1  
FROM akagelo/jenkins-slave-db  
MAINTAINER Oleg Vyukov <gelo@vyukov.ru>  
  
# обновляшки  
RUN apt-get update  
  
#xorg  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y xvfb x11-xkb-utils
xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic xserver-xorg-core
x11vnc fluxbox  
  
RUN mkdir /home/jenkins/.vnc && chown jenkins:jenkins /home/jenkins/.vnc &&
x11vnc -storepasswd jenkins /home/jenkins/.vnc/passwd && echo "export
DISPLAY=:0" >> /etc/bash.bashrc  
  
ENV DISPLAY :0  
#запуск сервисов через через самопальную систему иннициализации  
ADD etc/ /etc/  
  
#vnc порт  
EXPOSE 5900

