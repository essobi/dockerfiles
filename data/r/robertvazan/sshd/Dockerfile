FROM robertvazan/ubuntu  
RUN apt-get -y update && \  
apt-get -y install openssh-server  
ENTRYPOINT ["/usr/sbin/sshd", "-D"]  

