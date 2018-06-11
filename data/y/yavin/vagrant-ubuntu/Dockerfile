FROM ubuntu  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# create vagrant user  
RUN useradd --groups sudo --create-home --shell /bin/bash vagrant  
RUN echo 'root:vagrant' | chpasswd  
RUN echo 'vagrant:vagrant' | chpasswd  
RUN echo "vagrant ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/vagrant  
  
# install ssh server and sudo  
RUN apt-get update -y && \  
apt-get install -y openssh-server && \  
apt-get clean  
  
# setup ssh  
RUN sed -i 's/^UsePAM yes/UsePAM no/' /etc/ssh/sshd_config  
RUN mkdir /var/run/sshd  
  
# setup ssh for vagrant user  
ADD
https://raw.githubusercontent.com/mitchellh/vagrant/master/keys/vagrant.pub
/home/vagrant/.ssh/authorized_keys  
RUN chown -R vagrant:vagrant /home/vagrant/.ssh  
RUN chmod 0600 /home/vagrant/.ssh/authorized_keys  
RUN chmod 0700 /home/vagrant/.ssh  
  
# correct owner  
RUN chown -R root:root /usr/bin/sudo /etc/sudoers /etc/sudoers.d
/usr/lib/sudo/sudoers.so  
RUN chmod +s /usr/bin/sudo  
  
EXPOSE 22  
CMD /usr/sbin/sshd -D -e  

