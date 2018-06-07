FROM ubuntu:latest  
MAINTAINER Mike Wilson <geekinutah@gmail.com>  
  
ENV TERM=xterm-256color  
  
RUN apt-get -q update >/dev/null \  
&& apt-get install -y openssh-server \  
&& mkdir /var/run/sshd \  
  
# Cleanup  
&& apt-get clean autoclean \  
&& apt-get autoremove --yes \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
VOLUME ["/keys"]  
  
COPY start_ssh_server.sh /usr/bin/start_ssh_server.sh  
  
ENTRYPOINT ["/usr/bin/start_ssh_server.sh"]  

