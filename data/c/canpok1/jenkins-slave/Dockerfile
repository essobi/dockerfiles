FROM node:8.4  
RUN \  
  
echo deb http://ftp.de.debian.org/debian jessie-backports main >>
/etc/apt/sources.list; \  
apt-get update -y; \  
apt-get install -y openssh-server initscripts passwd git postgresql-client
locales; \  
apt install -y -t jessie-backports openjdk-8-jre-headless ca-certificates-
java; \  
groupadd jenkins && useradd -d /home/jenkins -s /bin/sh -g jenkins jenkins; \  
echo "jenkins:jenkins" | chpasswd; \  
mkdir /var/run/sshd; \  
echo "session required pam_mkhomedir.so skel=/etc/skel/ umask=0022" >>
/etc/pam.d/sshd; \  
locale-gen ja_JP.UTF-8;  
  
ENV LANG ja_JP.UTF-8  
ENV LANGUAGE ja_JP:en  
ENV LC_ALL ja_JP.UTF-8  
EXPOSE 22  
CMD /usr/sbin/sshd -D  

