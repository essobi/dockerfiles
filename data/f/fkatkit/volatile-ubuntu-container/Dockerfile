FROM ubuntu:xenial  
  
COPY generate-ssh-keyfiles.sh /usr/local/bin/  
COPY display_secret.sh /usr/local/bin/  
  
RUN apt-get update -q -y \  
&& apt-get install -y -q ssh sudo vim nano curl wget git cron \  
&& adduser -q --disabled-password --gecos "" ubuntu \  
&& echo "ubuntu:ubuntu" | chpasswd \  
&& gpasswd -a ubuntu sudo \  
&& echo "ubuntu ALL=NOPASSWD: ALL" >> /etc/sudoers \  
&& sed -i "s/#PasswordAuthentication yes/PasswordAuthentication no/"
/etc/ssh/sshd_config \  
&& su -c "/usr/local/bin/generate-ssh-keyfiles.sh" ubuntu \  
&& mkdir /var/run/sshd  
  
EXPOSE 22  
CMD /usr/sbin/service cron start && /usr/sbin/service ssh start && /bin/sh
/usr/local/bin/display_secret.sh  

