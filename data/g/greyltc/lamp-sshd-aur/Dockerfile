FROM greyltc/lamp-aur  
MAINTAINER Grey Christoforo <grey@christoforo.net>  
  
# setup ssh server  
ADD https://raw.githubusercontent.com/greyltc/docker-sshd/master/setup-
openssh.sh /usr/sbin/add-sshd  
RUN chmod +x /usr/sbin/add-sshd  
RUN add-sshd  
ADD https://raw.githubusercontent.com/greyltc/docker-sshd/master/run-sshd.sh
/usr/sbin/run-sshd  
RUN chmod +x /usr/sbin/run-sshd  
  
CMD run-sshd; start-servers; sleep infinity  

