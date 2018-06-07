# Arch Linux container with a ssh server  
FROM greyltc/archlinux  
MAINTAINER Grey Christoforo <grey@christoforo.net>  
  
# install openssh  
ADD setup-openssh.sh /usr/sbin/setup-openssh  
RUN setup-openssh  
  
ADD run-sshd.sh /usr/bin/run-sshd  
  
CMD run-sshd && sleep infinity  

