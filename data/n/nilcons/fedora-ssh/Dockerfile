FROM fedora:25  
MAINTAINER "Gergely Risko" <errge@nilcons.com>  
RUN dnf install -y openssh-server sudo pwgen hostname python python2-dnf &&
ssh-keygen -A && useradd -m -s /bin/bash fedora && echo 'fedora ALL=(ALL)
NOPASSWD:ALL' >/etc/sudoers.d/10-fedora-sudo  
CMD PW=$(pwgen -1 -0 -A 8) ; echo "SSH password for fedora@$(hostname -i) is:
$PW" ; echo "fedora:$PW" | chpasswd ; unset PW ; /usr/sbin/sshd -D  

