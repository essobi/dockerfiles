FROM ubuntu:latest  
MAINTAINER Mayur Ahir "https://github.com/ahirmayur"  
# Default lang is REAL English ;)  
ENV LANG C.UTF-8  
RUN echo "LC_ALL=en_GB.UTF-8" >> /etc/default/locale  
RUN locale-gen en_GB.UTF-8  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Surpress Upstart errors/warning  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -q update  
RUN apt-get install -y libreadline6 libreadline6-dev \  
software-properties-common python-software-properties \  
sudo apt-utils  
  
RUN add-apt-repository -y ppa:git-core/ppa  
  
RUN apt-get -q update  
RUN apt-get -y -q dist-upgrade  
  
RUN apt-get install -y openssh-server vim wget curl \  
htop git-core zip unzip  
  
RUN mkdir /var/run/sshd  
  
RUN echo 'root:root' |chpasswd  
  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
RUN sed -ri 's/#force_color_prompt=yes/force_color_prompt=yes/g' /root/.bashrc  
RUN source /root/.bashrc  
  
RUN apt-get -q autoremove && apt-get -q autoclean  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

