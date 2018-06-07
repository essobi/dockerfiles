#######################################################  
# This dockerfile builds a clean ubuntu 14.04 and #  
# including ssh, git, vim, etc..., basic apps. #  
# #  
# Author: Demon Tsai #  
# Repository: demontsai/ubuntu64:14.04 #  
# Version: 1.0 #  
# #  
#######################################################  
  
FROM ubuntu:14.04  
  
MAINTAINER Demon Tsai demontsai@estinet.com  
  
  
##### Adjust time zone  
RUN echo "Asia/Taipei" > /etc/timezone  
RUN dpkg-reconfigure --frontend noninteractive tzdata  
  
##### Update system and install apps  
RUN apt-get -qq update  
RUN apt-get -qqy install vim git wget curl  
  
##### Create an user account and assign password to it  
RUN useradd -m estinet && adduser estinet sudo && chsh -s /bin/bash estinet  
RUN echo "estinet:estinet" | chpasswd  
  
##### Join the user to sudoers  
RUN echo 'estinet ALL=(ALL) NOPASSWD:ALL' > /tmp/estinet  
RUN echo 'Defaults:estinet !requiretty' >> /tmp/estinet  
RUN chmod 0440 /tmp/estinet  
RUN chown root:root /tmp/estinet  
RUN mv /tmp/estinet /etc/sudoers.d/estinet  
  
##### SSH setting  
#RUN sudo -u estinet /usr/bin/ssh-keygen -t ecdsa -N "" -f
/home/estinet/.ssh/id_ecdsa  
#RUN sudo -u estinet /usr/bin/ssh-keygen -t rsa -N "" -f
/home/estinet/.ssh/id_rsa  
#RUN mkdir -p /var/run/sshd  
#EXPOSE 22  
  
##### Screen setting  
#COPY screenrc /etc/  
#RUN mkdir -p /var/run/screen  
#RUN chmod 0777 /var/run/screen  
  
##### Vim  
COPY vimrc.local /etc/vim/  
  
##### Clean  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
##### User  
#USER estinet  
#ENV HOME /home/estinet  
#ENV CODE_PATH $HOME/code  
#ENV INSTALL_PATH $HOME/installation  
#WORKDIR $HOME  
ENV ENTRYPOINT /root/entrypoint.sh  
  
COPY bashrc /home/estinet/.bashrc  
RUN chmod 0644 /home/estinet/.bashrc  
RUN chown estinet:estinet /home/estinet/.bashrc  
RUN mkdir /home/estinet/code  
RUN mkdir /home/estinet/installation  
  
COPY bashrc /root/.bashrc  
RUN chmod 0644 /root/.bashrc  
RUN chown root:root /root/.bashrc  
RUN mkdir /root/code  
RUN mkdir /root/installation  
  
RUN touch $ENTRYPOINT  
RUN chmod 755 $ENTRYPOINT  
RUN echo "#!/bin/sh" >> $ENTRYPOINT  
  
WORKDIR /root  
RUN echo "root:root" | chpasswd  
  

