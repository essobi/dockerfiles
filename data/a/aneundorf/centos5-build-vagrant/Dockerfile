FROM aneundorf/centos5-build-openssh  
MAINTAINER juergen.wind@sharpreflections.com  
  
RUN yum update -y && \  
yum install sudo -y  
  
# setup the vagrant user  
RUN if ! getent passwd vagrant; then useradd -d /home/vagrant -m -s /bin/bash
vagrant; fi \  
&& echo vagrant:vagrant | chpasswd \  
&& echo 'vagrant ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers \  
&& mkdir -p /etc/sudoers.d \  
&& echo 'vagrant ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers.d/vagrant \  
&& chmod 0440 /etc/sudoers.d/vagrant  
  
# Don't require tty for sudo  
RUN sed -i s/requiretty/\\!requiretty/g /etc/sudoers  
  
# add the vagrant insecure public key  
RUN mkdir -p /home/vagrant/.ssh \  
&& chmod 0700 /home/vagrant/.ssh \  
&& wget --no-check-certificate \  
https://raw.github.com/mitchellh/vagrant/master/keys/vagrant.pub \  
-O /home/vagrant/.ssh/authorized_keys \  
&& chmod 0600 /home/vagrant/.ssh/authorized_keys \  
&& chown -R vagrant /home/vagrant/.ssh  
  
# change sshd config  
RUN echo 'RSAAuthentication yes' >> /etc/ssh/sshd_config \  
&& echo 'PubkeyAuthentication yes' >> /etc/ssh/sshd_config \  
&& echo 'GSSAPIAuthentication no' >> /etc/ssh/sshd_config \  
&& echo 'AuthorizedKeysFile .ssh/authorized_keys' >> /etc/ssh/sshd_config  
  
RUN chkconfig sshd on  
RUN service sshd start  
  

