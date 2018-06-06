FROM centos:7  
MAINTAINER Olexander Kutsenko <olexander.kutsenko@gmail.com>  
  
RUN yum upgrade -y  
RUN yum install -y epel-release  
RUN yum install -y git gcc nano  
RUN yum install -y mc curl unzip zip  
RUN yum install -y wget tmux net-tools  
RUN yum install -y python-setuptools libevent-devel  
RUN yum install -y python-pip python-devel libffi-devel  
RUN easy_install gevent  
RUN pip install --upgrade pip  
  
#Install supervisor  
RUN mkdir -p /etc/supervisor/conf.d  
RUN mkdir -p /var/log/supervisor  
COPY configs/supervisor/cron.conf /etc/supervisor/conf.d/cron.conf  
COPY configs/supervisor/supervisord.conf /etc/supervisor/  
RUN pip install supervisor  
  
# SSH service  
RUN yum install -y openssh-server openssh-client  
RUN mkdir /run/sshd  
RUN echo 'root:root' | chpasswd  
#change 'pass' to your secret password  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> sudo tee -a /etc/profile  
RUN /usr/bin/ssh-keygen -A  
  
#configs bash start  
COPY configs/autostart.sh /root/autostart.sh  
COPY configs/bashrc /etc/bashrc  
RUN chmod +x /root/autostart.sh  
  
#Add colorful command line  
RUN echo "force_color_prompt=yes" >> ~/.bashrc  
RUN echo "export
PS1='${debian_chroot:+($debian_chroot)}\\[\033[01;31m\\]\u\\[\033[01;33m\\]@\\[\033[01;36m\\]\h
\\[\033[01;33m\\]\w \\[\033[01;35m\\]\$ \\[\033[00m\\]'" >> ~/.bashrc  
  
#etcKeeper  
RUN mkdir -p /root/etckeeper  
COPY configs/etckeeper.sh /root  
COPY configs/etckeeper-hook.sh /root/etckeeper  
RUN chmod +x /root/*.sh  
RUN /root/etckeeper.sh  
  
#Dependencies for NATest.bin  
RUN yum -y install glibc.i686  
RUN yum -y install 'libstdc++.so.5'  
COPY configs/NATest.bin /home/  
RUN chmod +x /home/*.bin  
  
#open ports  
EXPOSE 80 22 5400  

