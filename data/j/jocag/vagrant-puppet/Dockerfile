FROM centos:7  
MAINTAINER "jocag@uma.es"  
ENV container docker  
ENV PATH=/opt/puppetlabs/puppet/bin:/opt/puppetlabs/bin:$PATH  
  
# Enable systemd -- See https://hub.docker.com/_/centos/  
# Systemd is now included in centos7 base containers, but it is not active by
default.  
# In order to use systemd, you will need to include:  
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
# Install Puppet 3  
RUN rpm -ivh https://yum.puppetlabs.com/puppetlabs-release-el-7.noarch.rpm &&
\  
yum upgrade -y && \  
yum update -y && \  
yum install -y openssh-server openssh-clients hostname sudo \  
crontabs initscripts puppet\  
yum install -y && \  
yum clean all  
  
# Add default vagrant user  
RUN useradd --create-home -s /bin/bash vagrant  
RUN echo -n 'vagrant:vagrant' | chpasswd  
RUN echo 'vagrant ALL = NOPASSWD: ALL' > /etc/sudoers.d/vagrant  
RUN chmod 440 /etc/sudoers.d/vagrant  
RUN mkdir -p /home/vagrant/.ssh  
RUN chmod 700 /home/vagrant/.ssh  
RUN echo "ssh-rsa
AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoPkcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0zQPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbUvxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCzRdK8jlqm8tehUc9c9WhQ==
vagrant insecure public key" > /home/vagrant/.ssh/authorized_keys  
RUN chmod 600 /home/vagrant/.ssh/authorized_keys  
RUN chown -R vagrant:vagrant /home/vagrant/.ssh  
RUN sed -i -e 's/Defaults.*requiretty/#&/' /etc/sudoers  
RUN sed -i -e 's/\\(UsePAM \\)yes/\1 no/' /etc/ssh/sshd_config  
RUN echo 'LC_ALL=en_US.utf-8' >> /etc/locale.conf  
RUN systemctl enable sshd.service  
  
VOLUME [ "/sys/fs/cgroup" ]  
CMD ["/usr/sbin/init"]  

