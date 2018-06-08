FROM ubuntu  
  
MAINTAINER yejune "kwon@yejune.com"  
ENV DEBIAN_FRONTEND noninteractive  
ENV USER root  
  
RUN sed -i 's/archive.ubuntu.com/ftp.daumkakao.com/g' /etc/apt/sources.list  
  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y man nano \  
x11-utils x11-common x11vnc xvfb xinit \  
fluxbox sudo \  
fonts-nanum fonts-nanum-coding \  
emacs git wget \  
chromium-browser firefox && \  
rm -rf /var/lib/apt/lists/*  
  
ENV APORT 5901  
RUN mkdir ~/.vnc  
  
RUN echo '/usr/bin/x11vnc -usepw -display :1 -autoport $APORT -forever &' >>
~/.xinitrc  
RUN echo "/usr/bin/startfluxbox" >> ~/.xinitrc  
  
RUN mkdir ~/.fluxbox/  
RUN bash -c 'echo "xterm &" >> ~/.fluxbox/startup'  
RUN echo "/usr/bin/fluxbox -log ~/.fluxbox/log " >> ~/.fluxbox/startup  
  
ADD run.sh /run.sh  
RUN chmod 777 /run.sh  
CMD /run.sh  
  
RUN echo 'alias chrome="chromium-browser --no-sandbox --user-data-dir=/tmp"'
>> ~/.bashrc  
  
EXPOSE $APORT  

