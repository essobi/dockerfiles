FROM ubuntu:14.04  
  
MAINTAINER <herve leclerc> herve.leclerc@alterway.fr  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y openssh-server python sudo
&& \  
apt-get clean && \  
/etc/init.d/ssh start && \  
/etc/init.d/ssh stop  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

