FROM ubuntu:16.04  
MAINTAINER whatsalinux  
RUN apt-get -yy update  
RUN apt-get -y install --no-install-recommends sudo fuse libfuse2 libx11-6
libx11-xcb1 libfontconfig1 supervisor xvfb x11vnc software-properties-common
openbox xterm menu  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN addgroup soulseek  
RUN useradd -m -s /bin/bash -g soulseek soulseek  
RUN echo "soulseek:soulseek" | /usr/sbin/chpasswd  
RUN echo "soulseek ALL=(ALL) ALL" >> /etc/sudoers  
WORKDIR /home/soulseek  
ADD SoulseekQt-2017-11-21-64bit /usr/bin/soulseek  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD menu.xml /etc/xdg/openbox/menu.xml  
RUN mkdir "/home/soulseek/Soulseek Downloads"  
RUN mkdir /home/soulseek/Downloads  
RUN mkdir /home/soulseek/Music  
RUN mkdir /home/soulseek/.SoulseekQt  
RUN chown soulseek:soulseek /usr/bin/soulseek*  
RUN chown soulseek:soulseek -R /home/soulseek  
ENV DISPLAY :1  
ADD start /bin/start  
USER soulseek  
EXPOSE 5950 6080  
CMD ["/bin/start"]  

