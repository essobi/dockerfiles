FROM ubuntu:wily  
MAINTAINER Tom Strickx tom@strickx.com  
  
RUN \  
apt-get -q -y update ;\  
apt-get install -y python-software-properties python-pip;\  
apt-get install -y locales openssh-server weechat tmux ;\  
apt-get install -y mosh ;\  
apt-get install -y vim ;\  
mkdir /var/run/sshd ;\  
useradd -m docker -s /bin/bash ;\  
pip install websocket-client ;\  
locale-gen en_US.UTF-8  
  
# SSH port  
EXPOSE 22  
# Mosh UDP ports  
EXPOSE 60000-60050/UDP  
  
# Weechat api relay port  
EXPOSE 9001  
# Weechat irc relay port  
EXPOSE 9002  
ADD bashrc /home/docker/.bashrc  
ADD startup.sh /usr/bin/startup.sh  
ADD tmux.conf /home/docker/.tmux.conf  
  
RUN chmod 755 /usr/bin/startup.sh  
  
# The argument is the user as set up above  
CMD ["/usr/bin/startup.sh", "docker"]  

