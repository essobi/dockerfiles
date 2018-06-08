FROM fedora:26  
LABEL maintainer="KenjiTakahashi <kenji.sx>"  
  
RUN dnf install -y \  
iptables \  
openssh-server \  
rsync \  
vim \  
less \  
curl \  
psmisc \  
htop \  
procps-ng \  
iproute \  
zsh \  
ranger \  
&& rm -rf /etc/ssh/*key*  
  
RUN sed -i 's/locked//g' /etc/shadow \  
&& groupadd --gid 1100 rancher \  
&& groupadd --gid 1101 docker \  
&& useradd -u 1100 -g rancher -G docker,wheel -m -s /bin/zsh rancher \  
&& useradd -u 1101 -g docker -G docker,wheel -m -s /bin/bash docker \  
&& echo ClientAliveInterval 180 >> /etc/ssh/sshd_config  
  
COPY prompt.sh /etc/profile.d/  
  
ENTRYPOINT ["/usr/bin/ros", "entrypoint"]  

