FROM sflyr/ubuntu  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -y update  
RUN apt-get -y install ubuntu-desktop  
RUN apt-get -y install xfce4 xrdp  
RUN apt-get -y install xfce4 xfce4-goodies  
RUN apt-get -y install openssh-server  
  
EXPOSE 3389  
  
RUN useradd -ms /bin/bash ubuntu  
RUN adduser ubuntu sudo  
USER ubuntu  
WORKDIR /home/ubuntu  
RUN echo xfce4-session > /home/ubuntu/.xsession  
  
USER root  
WORKDIR /  
  
# must import .ssh from your host (via -v)  
# RUN sed -i "s/#PasswordAuthentication yes/PasswordAuthentication no/"
/etc/ssh/sshd_config  
RUN rm -v /etc/ssh/ssh_host_*  
  
CMD echo "ubuntu:$PASSWORD" | chpasswd && \  
dpkg-reconfigure openssh-server && \  
service ssh start && \  
service xrdp start && \  
tail -f /var/log/xrdp-sesman.log  
  
# This script follows: https://aws.amazon.com/es/premiumsupport/knowledge-
center/connect-to-linux-desktop-from-windows  

