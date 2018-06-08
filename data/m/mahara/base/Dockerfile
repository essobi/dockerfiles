FROM mahara/base:latest  
  
MAINTAINER tech@spindletop.software  
  
RUN apt-get update \  
&& apt-get install -y openssh-server sudo \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /var/run/sshd  
  
ARG user=spindletop  
ARG group=spindletop  
ARG uid=1000  
ARG gid=1000  
ENV HOME_DIRECTORY /home/$user  
RUN groupadd -g ${gid} ${group} \  
&& useradd -d "$HOME_DIRECTORY" -u ${uid} -g ${gid} -m -s /bin/bash ${user} \  
&& echo $user:qwert123 | chpasswd  
  
COPY sudoers_custom /etc/sudoers.d/sudoers_custom  
COPY ssh.conf /etc/supervisor/conf.d/ssh.conf  
  
ENTRYPOINT ["/usr/bin/supervisord"]  

