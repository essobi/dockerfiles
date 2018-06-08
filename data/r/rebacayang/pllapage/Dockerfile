######################################  
# Dockerfile build pllapage codes  
# in slosh/infrastructure  
# The codes were maintained at  
# https://rebacayang@bitbucket.org/plla_taiwan/pllapage.git  
# This file should be paced in root  
# of pllapage  
#######################################  
# Base image to slosh/infrastructure  
# FROM slosh/infrastructure:V0.1  
FROM ubuntu:16.04  
# Author  
MAINTAINER Li-Ren Chien (ccumouse@gmail.com)  
  
ENV container docker  
ENV sloshpath /usr/slosh  
RUN systemctl set-default multi-user.target  
  
# Don't start any optional services except for the few we need.  
RUN find /etc/systemd/system \  
/lib/systemd/system \  
-path '*.wants/*' \  
-not -name '*journald*' \  
-not -name '*systemd-tmpfiles*' \  
-not -name '*systemd-user-sessions*' \  
-exec rm \\{} \;  
RUN apt-get -qq update; apt-get -y install apt-utils python openssh-server
openssh-client nano sudo curl; apt-get clean  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -  
RUN apt-get -qq update;apt-get install -y nodejs; apt-get clean  
RUN npm install -g express-generator  
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN echo 'root:docker' | chpasswd  
RUN systemctl enable ssh.service  
RUN useradd -ms /bin/bash slosh  
RUN adduser slosh sudo  
RUN echo 'slosh:slosher' | chpasswd  
  
VOLUME ["/sys/fs/cgroup"]  
VOLUME ["/run"]  
  
WORKDIR ${sloshpath}  
COPY . /usr/slosh  
COPY ./nodejs/sloshinfra.service /lib/systemd/system/  
COPY ./nodejs/frontend.service /lib/systemd/system/  
  
RUN systemctl enable sloshinfra.service  
RUN systemctl enable frontend.service  
  
EXPOSE 22 3050 7070  
CMD ["/sbin/init"]  

