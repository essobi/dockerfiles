FROM debian:jessie  
  
#ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /root  
  
RUN apt-get update  
RUN apt-get install -y acl vim wget curl git subversion htop  
RUN apt-get install -y zip  
  
# install ssh  
RUN apt-get install -y openssh-server  
  
# config ssh for easy access  
RUN sed -i 's/^PermitRootLogin/# PermitRootlogin/' /etc/ssh/sshd_config  
RUN echo 'root:pMwe9bse' | chpasswd  
RUN mkdir -p /root/.ssh  
  
# install supervisor  
#RUN apt-get install -y supervisor  
#RUN mkdir -p /var/run/sshd /var/log/supervisor  
# Set locale  
RUN apt-get -qqy install locales  
RUN sed -i 's/# fr_FR.UTF-8 UTF-8/fr_FR.UTF-8 UTF-8/' /etc/locale.gen  
RUN /usr/sbin/locale-gen  
ENV LANG fr_FR.UTF-8  
ENV LANGUAGE fr_FR:fr  
ENV LC_ALL fr_FR.UTF-8  
# Add johnsnow user for deployment - force uid to 1000 as it is johnsnow uid
on host (mapping necessary for nice rights sharing)  
RUN useradd --system --uid=1000 -s /bin/bash -m -d /home/johnsnow johnsnow  
RUN echo 'johnsnow:lorotad8' | chpasswd  
RUN mkdir -p /home/johnsnow/.ssh  
#RUN mkdir -p /home/johnsnow/medias  
#RUN chown -R johnsnow:johnsnow /home/profideo/.ssh /home/profideo/medias  
#Install useful apps  
RUN apt-get install -y -q emacs  
RUN apt-get install -y -q tree  
COPY ./files/emacs.conf /home/johnsnow/.emacs  
COPY ./files/vimrc.conf /etc/vim/vimrc  
COPY ./files/gitconfig /home/johnsnow/.gitconfig  
  
EXPOSE 22  

