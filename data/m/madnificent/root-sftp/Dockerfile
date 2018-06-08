FROM ubuntu:14.04  
  
RUN apt-get update; apt-get install --assume-yes openssh-server; mkdir
/var/run/sshd; sed -i "s/^PermitRootLogin.*/PermitRootLogin yes/"
/etc/ssh/sshd_config  
  
COPY boot-script.sh /  
  
CMD sh /boot-script.sh

