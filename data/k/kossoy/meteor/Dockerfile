FROM ubuntu:utopic  
MAINTAINER Oleg Kossoy <oleg@kossoy.com>  
  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -y install supervisor git vim pwgen mc openssh-server samba curl  
  
# Install ssh  
RUN mkdir -p /var/run/sshd && sed -i
"s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config
&& sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config && sed -i
"s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config  
ADD set_root_pw.sh /set_root_pw.sh  
  
# Install node  
RUN curl -sL https://deb.nodesource.com/setup | sudo bash -  
RUN apt-get install nodejs -y  
  
# Install meteor  
RUN curl https://install.meteor.com/ | sh  
  
# Add run script  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
  
# Install samba  
ADD smb.cfg /etc/samba/smb.conf  
  
WORKDIR /apps  
  
VOLUME ["/apps"]  
  
ENV PORT 3000  
EXPOSE 22 445 3000  
CMD ["/run.sh"]  
  
# docker build -t <image_name> .  
# docker run -d -p 2222:22 -p 445:445 -p 3000:3000 --name <container>
<image_name>  

