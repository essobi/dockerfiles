FROM centos:6.9  
MAINTAINER Tron Thongsringklee <thanandorn@gmail.com>  
  
RUN yum -y install openssh-server openssh-clients hostname crontabs
initscripts  
RUN yum -y update; yum clean all  
RUN chkconfig --level 3 sshd on  
RUN service sshd start  
  
# Add vagrant user and key  
RUN yum -y install sudo  
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
RUN sed -i -e 's#^\\(UsePAM \\)yes#\1 no#' /etc/ssh/sshd_config  
RUN echo 'LC_ALL=en_US.utf-8' >> /etc/locale.conf  
CMD ["/usr/sbin/sshd", "-D"]  

