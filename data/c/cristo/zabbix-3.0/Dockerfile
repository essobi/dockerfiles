FROM ubuntu:14.04.4  
MAINTAINER Olexander Kutsenko <olexander.kutsenko@gmail.com>  
  
#install Software  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -y software-properties-common python-software-properties  
RUN apt-get install -y vim nano mc screen curl unzip wget tmux zip gzip  
  
#MySQL install + password  
RUN echo "mysql-server mysql-server/root_password password root" | debconf-
set-selections  
RUN echo "mysql-server mysql-server/root_password_again password root" |
debconf-set-selections  
RUN sudo apt-get install -y mysql-server mysql-client  
COPY configs/mysql/my.cnf /etc/mysql/my.cnf  
COPY configs/mysql/create.sql /home/create.sql  
  
#Install Zabbix  
RUN wget http://repo.zabbix.com/zabbix/3.0/ubuntu/pool/main/z/zabbix-
release/zabbix-release_3.0-1+trusty_all.deb  
RUN chmod +x zabbix-release_3.0-1+trusty_all.deb  
RUN dpkg -i zabbix-release_3.0-1+trusty_all.deb  
RUN apt-get update  
RUN apt-get install -y zabbix-server-mysql zabbix-frontend-php  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf  
COPY configs/php.ini /etc/php5/apache2/php.ini  
  
# SSH service  
RUN sudo apt-get install -y openssh-server openssh-client  
RUN sudo mkdir /var/run/sshd  
RUN echo 'root:root' | chpasswd  
#change 'pass' to your secret password  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
#configs bash start  
COPY configs/autostart.sh /root/autostart.sh  
RUN chmod +x /root/autostart.sh  
COPY configs/bash.bashrc /etc/bash.bashrc  
  
#Add colorful commandg line  
RUN echo "force_color_prompt=yes" >> .bashrc  
RUN echo "export
PS1='${debian_chroot:+($debian_chroot)}\\[\033[01;31m\\]\u\\[\033[01;33m\\]@\\[\033[01;36m\\]\h
\\[\033[01;33m\\]\w \\[\033[01;35m\\]\$ \\[\033[00m\\]'" >> .bashrc  
  
#Install locale  
RUN locale-gen en_US.UTF-8  
RUN dpkg-reconfigure locales  
  
#etcKeeper  
RUN mkdir -p /root/etckeeper  
COPY configs/etckeeper.sh /root  
COPY configs/files/etckeeper-hook.sh /root/etckeeper  
RUN chmod +x /root/etckeeper.sh  
RUN /root/etckeeper.sh  
  
#Create database  
RUN /root/autostart.sh  
  
#open ports  
EXPOSE 22 80 10051  

