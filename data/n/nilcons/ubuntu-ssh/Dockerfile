FROM ubuntu:16.04  
MAINTAINER "Gergely Risko" <errge@nilcons.com>  
RUN apt-get update && apt-get install -y openssh-server sudo pwgen python &&
useradd -m -s /bin/bash ubuntu && echo 'ubuntu ALL=(ALL) NOPASSWD:ALL'
>/etc/sudoers.d/10-ubuntu-sudo && mkdir -p /var/run/sshd  
CMD PW=$(pwgen -1 -0 -A 8) ; echo "SSH password for ubuntu@$(hostname -i) is:
$PW" ; echo "ubuntu:$PW" | chpasswd ; unset PW ; /usr/sbin/sshd -D  

