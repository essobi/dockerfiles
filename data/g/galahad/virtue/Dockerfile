FROM centos:centos7  
MAINTAINER Kyle Stapp <kyle.stapp@starlab.io>  
  
# Update  
RUN yum update -y  
  
# Install Infrastructure  
RUN yum install -y openssh-server wget curl bzip2 cloud-init  
  
# Install XPRA  
RUN rpm --import https://winswitch.org/gpg.asc && \  
curl http://xpra.org/dists/CentOS/winswitch.repo >
/etc/yum.repos.d/winswitch.repo && \  
yum install -y xpra  
  
RUN yum install -y epel-release  
RUN yum install -y python-pip python-uinput  
RUN pip install websockify netifaces  
  
#Install Sample Apps  
RUN yum install -y gedit  
RUN yum install -y firefox  
  
#Debug Tools  
RUN yum install -y vim  
  
#Create virtue user for sshd, xpra, and target app  
RUN useradd -ms /bin/bash virtue  
USER virtue  
WORKDIR /home/virtue  
  
#Configure ssh stuff  
RUN mkdir ~/.ssh && \  
chmod 700 ~/.ssh  
RUN ssh-keygen -t dsa -f ~/.ssh/ssh_host_dsa_key && \  
ssh-keygen -t rsa -f ~/.ssh/ssh_host_rsa_key && \  
ssh-keygen -t ecdsa -f ~/.ssh/ssh_host_ecdsa_key  
  
#Fixup xpra environment  
RUN echo "export XDG_RUNTIME_DIR=~/.xpra" >> /home/virtue/.bashrc  
  
#Configure ssh to allow key based auth and grab key from env  
COPY sshd_config /home/virtue/  
COPY *.sh /home/virtue/  
  
#Install User Local apps  
#RUN wget
https://mirror.clarkson.edu/blender/release/Blender2.79/blender-2.79-linux-
glibc219-x86_64.tar.bz2 && \  
# tar -xvjf blender-2.79-linux-glibc219-x86_64.tar.bz2  
#TBD Restrict SSH to only run the one xpra command  
#Auto start command  
CMD /home/virtue/kickoff.sh  
#CMD /bin/bash  
# Expose ports for ssh/apps  
EXPOSE 2022  
EXPOSE 2023  
EXPOSE 2024  
#USER root  
#WORKDIR /root  
#CMD /bin/bash  

