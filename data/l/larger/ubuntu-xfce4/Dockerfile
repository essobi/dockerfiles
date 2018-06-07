FROM ubuntu:14.04  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
RUN mkdir -p /var/run/sshd  
RUN apt-get update \  
&& apt-get install -y supervisor \  
openssh-server nano \  
xfce4 xfce4-goodies \  
x11vnc xvfb \  
firefox \  
&& apt-get autoclean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /root  
  
ADD supervisord.conf ./  
  
EXPOSE 5900  
EXPOSE 22  
#CMD ["/usr/bin/supervisord","-c","/root/supervisord.conf"]

