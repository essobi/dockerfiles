# Debian jessie made vagrant-friendly.  
# http://github.com/iven/docker-images  
# docker pull iven/debian-vagrant:jessie  
FROM debian:jessie  
MAINTAINER Iven Hsu <ivenvd@gmail.com>  
  
# Basic upgrades; install sudo, supervisor and SSH.  
RUN apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get install --no-install-recommends -y \  
openssh-server \  
sudo \  
supervisor && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Setup SSH  
# See: https://docs.vagrantup.com/v2/boxes/base.html  
RUN mkdir /var/run/sshd && \  
sed -i 's/PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config && \  
echo 'PasswordAuthentication no' >> /etc/ssh/sshd_config && \  
echo 'UseDNS no' >> /etc/ssh/sshd_config  
  
# Setup supervisor  
ADD supervisor/*.conf /etc/supervisor/conf.d/  
  
# Remove the policy file once we're finished installing software.  
# This allows invoke-rc.d and friends to work as expected.  
RUN rm /usr/sbin/policy-rc.d  
  
# Add the Vagrant user and necessary passwords.  
RUN groupadd vagrant && \  
useradd -c "Vagrant" -g vagrant -d /home/vagrant -m -s /bin/bash vagrant && \  
echo 'root:vagrant' | chpasswd && \  
echo 'vagrant:vagrant' | chpasswd  
  
# Allow the vagrant user to use sudo without a password.  
RUN echo 'vagrant ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/vagrant  
  
# Install Vagrant's insecure public key so provisioning and 'vagrant ssh'
work.  
RUN mkdir /home/vagrant/.ssh  
ADD
https://raw.githubusercontent.com/mitchellh/vagrant/master/keys/vagrant.pub
/home/vagrant/.ssh/authorized_keys  
RUN chmod 0600 /home/vagrant/.ssh/authorized_keys && \  
chown -R vagrant:vagrant /home/vagrant/.ssh && \  
chmod 0700 /home/vagrant/.ssh  
  
CMD ["supervisord"]  
  

