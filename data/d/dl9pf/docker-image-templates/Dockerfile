FROM debian:jessie  
MAINTAINER Jan-Simon Moeller <dl9pf@gmx.de>  
  
# Install packages  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y -u dist-
upgrade && DEBIAN_FRONTEND=noninteractive apt-get -y install openssh-server
pwgen  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install gawk wget git-core
diffstat unzip texinfo gcc-multilib build-essential chrpath socat
libsdl1.2-dev xterm file cpio default-jre  
RUN mkdir -p /var/run/sshd && sed -i
"s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config
&& sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config && sed -i
"s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config  
  
ADD set_root_pw.sh /set_root_pw.sh  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
  
ENV AUTHORIZED_KEYS **None**  
  
# Set user jenkins to the image  
RUN adduser --quiet jenkins && echo "jenkins:jenkinspass" | chpasswd  
  
# Standard SSH port  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  
  
#EXPOSE 22  
#CMD ["bash"]  

