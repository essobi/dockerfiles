# stolen from:  
# - https://registry.hub.docker.com/u/fedora/ssh/dockerfile  
# - https://github.com/fedora-cloud/Fedora-Dockerfiles/tree/master/ssh  
# not sure why, but the registry version can't be used for some reason  
FROM fedora  
MAINTAINER Ron Waldon <jokeyrhyme@gmail.com>  
  
RUN yum -y update; yum clean all  
RUN yum -y install openssh-server; yum clean all  
ADD ./start.sh /start.sh  
RUN mkdir /var/run/sshd  
  
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N ''  
  
RUN chmod 755 /start.sh  
EXPOSE 22  
RUN ./start.sh  
ENTRYPOINT ["/usr/sbin/sshd", "-D"]  

