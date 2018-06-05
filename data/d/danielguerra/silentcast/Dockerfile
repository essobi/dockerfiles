FROM ubuntu:14.04  
MAINTAINER Daniel Guerra  
#Install Packages  
RUN apt-get -yy update &&\  
apt-get -y install --no-install-recommends software-properties-common firefox
ca-certificates supervisor openbox xvfb x11vnc xterm xfce4-terminal docker vim
&&\  
add-apt-repository ppa:sethj/silentcast &&\  
apt-get -yy update &&\  
apt-get -yy install silentcast &&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /home/silentcast  
#User settings  
RUN addgroup silentcast  
RUN useradd -m -g silentcast -s /bin/bash silentcast  
RUN echo "silentcast:silentcast" > /tmp/pass && /usr/sbin/chpasswd < /tmp/pass  
RUN echo "silentcast ALL=(ALL) ALL" >> /etc/sudoers  
# cofigure supervisor  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
# cofigure openbox menu  
ADD menu.xml /etc/xdg/openbox/menu.xml  
# set mount point  
VOLUME /mnt  
# set env for rigth display  
ENV DISPLAY :1  
# port exposure  
EXPOSE 5900  
# set work dir  
WORKDIR /home/silentcast  
# set standard user  
USER silentcast  
#start supervisor  
CMD ["/usr/bin/supervisord","-c","/etc/supervisor/conf.d/supervisord.conf"]  

