FROM debian:7  
  
MAINTAINER mrlesmithjr@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
apt-utils openssh-server sudo wget && \  
apt-get install -y python-simplejson && \  
apt-get clean -y && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir /var/run/sshd  
  
RUN useradd -p vagrant vagrant -s /bin/bash && \  
usermod -aG sudo vagrant && \  
sed -i 's/^%sudo.*/%sudo ALL=(ALL:ALL) NOPASSWD:ALL/g' /etc/sudoers  
  
RUN date > /etc/vagrant_box_build_time && \  
mkdir -pm 700 /home/vagrant/.ssh && \  
wget --no-check-certificate \  
'https://raw.github.com/mitchellh/vagrant/master/keys/vagrant.pub' \  
-O /home/vagrant/.ssh/authorized_keys && \  
chmod 0600 /home/vagrant/.ssh/authorized_keys && \  
chown -R vagrant /home/vagrant  
  
ENV DEBIAN_FRONTEND teletype  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

