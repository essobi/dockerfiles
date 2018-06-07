FROM debian:stable  
MAINTAINER Dogstudio <devs@dogstudio.be>  
  
ENV REMOTE_HOST sample.com  
ENV REMOTE_USER root  
ENV REMOTE_PORT 22  
ENV REMOTE_SERVICE 3306  
  
RUN useradd docker \  
&& mkdir /home/docker \  
&& chown docker:docker /home/docker \  
&& addgroup docker staff  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends openssh-client bindfs kmod
mysql-client\  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/  
  
RUN mkdir /home/docker/.ssh \  
&& mkdir /home/docker/.ssh-external \  
&& echo "bindfs#/home/docker/.ssh-external /home/docker/.ssh fuse force-
user=docker,force-group=docker,perms=0700 0 0" >> /etc/fstab  
  
RUN chown -R docker:docker /home/docker/.ssh-external  
  
CMD ssh -o ServerAliveInterval=30 -o ServerAliveCountMax=1 -o
StrictHostKeyChecking=no -o BatchMode=yes -i /home/docker/.ssh-external/id_rsa
-p $REMOTE_PORT -L *:$REMOTE_SERVICE:127.0.0.1:$REMOTE_SERVICE -N
$REMOTE_USER@$REMOTE_HOST  
  
EXPOSE $REMOTE_SERVICE  

