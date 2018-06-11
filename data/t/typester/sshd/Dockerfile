FROM ubuntu:12.04  
MAINTAINER Daisuke Murase <typester@gmail.com>  
  
RUN echo 'deb http://archive.ubuntu.com/ubuntu precise main universe' >
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y openssh-server daemontools  
RUN echo 'PasswordAuthentication no' >> /etc/ssh/sshd_config  
  
RUN mkdir -p /var/run/sshd  
ADD docker.pub /root/.ssh/authorized_keys  
ADD sshd /service/sshd  
RUN chmod 400 /root/.ssh/authorized_keys && chown root
/root/.ssh/authorized_keys  
  
EXPOSE 22  
ENTRYPOINT ["/usr/bin/svscan", "/service"]  

