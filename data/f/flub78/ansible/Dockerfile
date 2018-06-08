# Minimal ansible target container  
#  
# docker run -d --name=ansible -v
$HOME/.ssh/id_rsa.public/:/root/.ssh/authorized_keys ansible  
FROM ubuntu:14.04  
MAINTAINER Frédéric Peignot frederic.peignot@free.fr  
  
ENV MAINTAINER "Frédéric Peignot"  
RUN apt-get update && apt-get install -y openssh-server && apt-get install -y
python \  
&& apt-get install -y python-apt  
RUN mkdir /var/run/sshd  
  
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

