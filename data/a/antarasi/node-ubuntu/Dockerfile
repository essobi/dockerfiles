FROM ubuntu:16.04  
MAINTAINER ANTARA IT Systems "contact@antara.pl"  
ENV HOME /root  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update \  
&& apt-get -qq update \  
&& apt-get -y install sudo git curl openssh-server \  
&& mkdir /var/run/sshd \  
&& echo 'root:root' | chpasswd \  
&& sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config \  
&& sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - \  
&& apt-get update && apt-get install -y nodejs \  
&& npm install npm@5.2.0 -g  
  
RUN apt-get install -y ufw  
  
RUN node -v && npm -v  
  
RUN ssh-keygen -q -f ~/.ssh/id_rsa -t rsa -b 4096 -N '' -C 'root@ubuntu16'  
  
#allow services to start automatically from this point  
#https://askubuntu.com/questions/365911/why-the-services-do-not-start-at-
installation  
RUN printf '#!/bin/sh\nexit 0\n' > /usr/sbin/policy-rc.d  
  
CMD ["/bin/bash"]  
WORKDIR /project  
VOLUME ["/project"]  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]

