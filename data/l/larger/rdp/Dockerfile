FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -y --force-yes xrdp xvfb lxde git vim mc
lxtask firefox && apt-get clean  
  
RUN ln -fs /usr/bin/Xvfb /etc/X11/X  
  
RUN useradd -mp docker -s /bin/bash -G sudo nio  
  
RUN echo 'pgrep -U $(id -u) lxsession | grep -v ^$_LXSESSION_PID | xargs --no-
run-if-empty kill' > /bin/lxcleanup.sh  
RUN chmod +x /bin/lxcleanup.sh  
RUN echo '@lxcleanup.sh' >> /etc/xdg/lxsession/LXDE/autostart  
  
RUN echo '#!/bin/sh -xe\nrm -rf /tmp/* /var/run/xrdp/* && service xrdp start
&& startx' > /bin/rdp.sh  
RUN chmod +x /bin/rdp.sh  
  
CMD ["rdp.sh"]  
  
EXPOSE 3389

