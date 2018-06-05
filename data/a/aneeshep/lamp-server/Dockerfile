FROM ubuntu:14.04  
RUN apt-get update && bash -c "apt-get install -y rsync openssh-client lamp-
server^"  
COPY files/id_rsa.pub /root/.ssh/id_rsa.pub  
COPY files/id_rsa /root/.ssh/id_rsa  
RUN chmod 0600 /root/.ssh/id_rsa && chmod 0600 /root/.ssh/id_rsa.pub  
  
CMD /usr/sbin/apache2ctl -D FOREGROUND  

