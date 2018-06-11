FROM fedora:latest  
  
# This image should be kept to the minimal requirements for vagrant  
# to be able to ssh into the container and run provisioners.  
#  
# openssh-server: let "vagrant ssh" work  
# openssh-clients: let scp work  
# sudo: for vagrant user to elevate privileges  
# passwd: to set password for vagrant user  
RUN dnf -y install \  
openssh-server \  
openssh-clients \  
sudo \  
passwd \  
&& dnf clean all  
  
# Disable unneeded services  
RUN ["/usr/bin/rm", "-f", \  
"/etc/systemd/system/basic.target.wants/dnf-makecache.timer", \  
"/etc/systemd/system/getty.target.wants/getty@tty1.service"]  
  
# Disable any getty spawning  
RUN ["/bin/sh", "-c", "echo -e NAutoVTs=0\\\\\\\nReserveVT=0 >>
/etc/systemd/logind.conf"]  
  
# These changes are explained here:  
# https://www.vagrantup.com/docs/boxes/base.html  
# Add a user named vagrant  
RUN adduser vagrant  
  
# Let vagrant have passwordless sudo  
RUN echo 'vagrant ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers  
  
# Do not require a tty  
RUN sed -r -e 's|^Defaults.*requiretty|#\0|' -i /etc/sudoers  
  
# Make ssh connect faster  
RUN echo 'UseDNS no' >> /etc/ssh/sshd_config  
  
# Set password to 'vagrant'  
RUN echo vagrant | passwd --stdin vagrant  
  
# Set up ssh key  
USER vagrant  
RUN mkdir /home/vagrant/.ssh  
RUN chmod og-rx /home/vagrant/.ssh  
RUN ["/bin/sh", "-c", "echo 'ssh-rsa
AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoPkcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0zQPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbUvxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCzRdK8jlqm8tehUc9c9WhQ==
vagrant insecure public key' > /home/vagrant/.ssh/authorized_keys"]  
  
USER root  
  
VOLUME /var/log  
  
ENV container=docker  
  
CMD ["/sbin/init"]  

